# -*- coding: utf-8 -*-
"""
ChatGee Module Class Object
"""

import queue as q
import threading
import time
from datetime import datetime

import tiktoken

from base.module_database import ChatGee_DB
from base.module_openai import ChatGee_OpenAI
from base.module_kakaotalk import ChatGee_KakaoTalk
from base.contents import generate_greetings, generate_advertisement, generate_documents

class ChatGeeOBJ:
    """ChatGee Module Class Object"""

    def __init__(self, ChatGee_Config):
        # Save Configuration
        self.ChatGee_Config = ChatGee_Config
        # Generate ChatGee Database and Initiate
        self.DB = ChatGee_DB()
        self.DB.init_db(self.ChatGee_Config['DATABASE']['DB_PREFIX'])
        # OpenAI Encoding to count tokens
        self.encoding = tiktoken.encoding_for_model(self.ChatGee_Config['OPEN_AI']['MODEL'])
        self.system_prompt_tokens_estimate = \
            len(self.encoding.encode(self.ChatGee_Config['SETTINGS']['SYSTEM_PROMPT'])) \
            + 350  # 320 by ChatGee Template + 30 for safety
        self.max_user_prompt_history_tokens = int(4096/2) - self.system_prompt_tokens_estimate
        # Set OpenAI Module Configuratoin
        self.OpenAI = ChatGee_OpenAI(
            api_key = self.ChatGee_Config['OPEN_AI']['API_KEY'],
            model = self.ChatGee_Config['OPEN_AI']['MODEL'],
            hyper_top_p = self.ChatGee_Config['OPEN_AI']['HYPER_TOP_P'],
            hyper_temperature = self.ChatGee_Config['OPEN_AI']['HYPER_TEMPERATURE'],
            max_user_prompt_history_tokens = self.max_user_prompt_history_tokens,
            system_prompt_tokens_estimate = self.system_prompt_tokens_estimate,
            openai_api_error_log = self.ChatGee_Config['OPEN_AI']['OPENAI_API_ERROR_LOG']
        )

    # Get Usage Count
    def get_usage_count(self, userid):
        """Get Usage Count of the user"""
        user_data = self.DB.get_user_data_by_room(userid)
        user_data = list(user_data[0])
        return user_data[4]

    # ----- Flask Prompt Response Function ----- #
    def prompt_received(self, content):
        """Process the prompt received from Flask"""
        run_flag = False
        start_time = time.time()

        # Check user
        new_user_flag = False
        userid = content['userRequest']['user']['id'] # userid is saved as 'room' in user_data.db
        isFriend = content['userRequest']['user']['properties'].get('isFriend', False)

        # Read user data (room, member, count, total_count)
        user_data = self.DB.get_user_data_by_room(userid)
        # If new user, save guest template
        if len(user_data) == 0:
            self.DB.save_user_data(userid, isFriend, 1, 0)
            new_user_flag = True
        user_data = list(self.DB.get_user_data_by_room(userid)[0])
        previous_friendship = user_data[2]
        self.DB.save_user_data(userid, isFriend, user_data[3], user_data[4])
        user_data = list(self.DB.get_user_data_by_room(userid)[0])
        if previous_friendship is False and isFriend is True:
            self.DB.save_conversation_one_above("user", userid, \
            "💞💕 우린 이제 친구가 되었어! 너무너무 반가워! 앞으로도 너랑 이야기할 것이 기대되!" \
            "우리가 친구가 된게 너무너무 기쁘다고 앞으로 두번은 더 이야기해줘!")

        # Greetings Card if new user
        if new_user_flag:
            response = generate_greetings(self.ChatGee_Config, content)
        # For normal user
        else:
            run_flag = True

        # Check membership
        if user_data[2] is False \
            and user_data[4] > self.ChatGee_Config['SETTINGS']['NO_FRIEND_USE_LIMIT']:
            response = ChatGee_KakaoTalk.insert_card(title='우리 친구해요 🤝💞💞',
                description='제 프로필에서 오른쪽 상단의 노란색 친구추가버튼을 클릭하면 우린 친구가 됩니다! 🙏🏻🙏🏻💗')
            chat_history = self.DB.get_conversation_latest(userid, limit=1)
            response = ChatGee_KakaoTalk.insert_button_text(
                response, '이전 말 다시적기 ✍🏻', chat_history[0][3])
            run_flag = False

        # Find Special Commands
        if content['userRequest']['utterance'] == '📓 사용설명서':
            response = generate_documents(self.ChatGee_Config)
            run_flag = False

        # Clear Chat History
        if content['userRequest']['utterance'] == '💫 새로운 시작':
            self.DB.delete_conversation_data(userid)
            response = ChatGee_KakaoTalk.insert_text("대화한적이..있었..없었습니다...\n🪄💫✨💆‍♂️🦄🌈🌟🎉🍭🎠")
            run_flag = False

        # Run if no special commands found
        if run_flag:
            # Make queues for request and respond
            request_queue = q.Queue()
            response_queue = q.Queue()
            # assign target function for the queues
            request_respond = threading.Thread(target=self.prompt,
                                               args=(request_queue, response_queue))
            # start the queues
            request_respond.start()
            # trigger the prompt request
            request_queue.put(content)
            # Retreive the response
            while time.time() - start_time < self.ChatGee_Config['SETTINGS']['RESPONSE_SAFE_TIME']:
                if not response_queue.empty():
                    # Function A returned a result
                    response = response_queue.get()
                    break
                timeover_queue = q.Queue()
                timeover_thread = threading.Thread(target=self.timeover, args=(timeover_queue,))
                timeover_thread.start()
                response = timeover_queue.get()

                # For safety
                time.sleep(0.01)

            if user_data[4] % self.ChatGee_Config['SETTINGS']['ADVERTISEMENT_FREQUENCY'] == 0 \
                and content['userRequest']['utterance'] != '생각 다 했니???!':
                response = generate_advertisement(self.ChatGee_Config, response)

        # Return back to kakao
        return response

    # ----- Main Action Wrapper Function ----- #
    def prompt(self, request_queue, response_queue):
        """Process the prompt received from Flask"""
        content = request_queue.get()
        userid = content['userRequest']['user']['id']
        content = content['userRequest']['utterance']
        content = ''.join(str(e) for e in content)

        # run queue threading since kakaotalk chatbot will only wait 5 seconds
        child_queue = q.Queue()

        # create the thread
        chat_gpt_respond = threading.Thread(target=self.respond,
                                            args=(child_queue, content, userid))

        # Start the thread
        chat_gpt_respond.start()
        chat_gpt_respond.join()
        result = child_queue.get()

        response_queue.put(result)

    # ----- Get ChatGPT Respond Function ----- #
    def respond(self, queue, content, userid):
        """Get the respond from ChatGPT"""
        if content == '생각 다 했니???!':
            repeat = True
        else:
            repeat = False
            # Count up user data
            user_data = list(self.DB.get_user_data_by_room(userid)[0])
            user_data[3] += 1
            user_data[4] += 1
            self.DB.save_user_data(userid, user_data[2], user_data[3], user_data[4])

        if len(content) < 2: # 만약 한글자 입력일 경우 오류회피
            content += " "

        response = self.chatgpt_wrapper(content, userid, repeat)

        if response != 'Error':
            if response == 'NOT YET':
                # time.sleep(0.6)
                # chat_history = ChatGee_KakaoTalk.get_conversation_latest(userid, limit=1)
                response = ChatGee_KakaoTalk.insert_text('아직도 생각하고 있나봐요...! 🐢🐌\n조금 더 기다려주세요 🙏🏻')
                quick_reply = ChatGee_KakaoTalk.make_reply('생각 다 했니?! 🤔','생각 다 했니???!')
                response = ChatGee_KakaoTalk.insert_replies(response, quick_reply)
            else:
                response = ChatGee_KakaoTalk.insert_text(response)
            queue.put(response)

        else:
            response = ChatGee_KakaoTalk.insert_text('OpenAI서버가 오류메세지를 보냈어요 🙇')
            quick_reply = ChatGee_KakaoTalk.make_reply('다시 물어보기 ✍🏻', content)
            response = ChatGee_KakaoTalk.insert_replies(response, quick_reply)
            queue.put(response)

    def timeover(self, queue):
        """If the respond is not received within 5 seconds, send this message"""
        response = ChatGee_KakaoTalk.insert_text("죄송해요 🙇🙇🙇\n생각이 길어지고 있어요 🤔💭\n잠시후 아래 말풍선을 눌러주세요!")
        quick_reply = ChatGee_KakaoTalk.make_reply('생각 다 했니?! 🤔','생각 다 했니???!')
        response = ChatGee_KakaoTalk.insert_replies(response, quick_reply)
        queue.put(response)

    def chatgpt_wrapper(self, prompt, userid, repeat):
        """Wrapper function for ChatGPT"""
        response = []

        # If it's trying to repeat
        if repeat:
            time.sleep(0.6)
            # Check if respond exists
            chat_history = self.DB.get_conversation_latest(userid, limit=1)
            if chat_history[0][1] == 'assistant':
                response = chat_history[0][3]
            else:
                response = 'NOT YET'

        # Normal function if not repeating
        else:
            # Update the conversation history
            self.DB.save_conversation_data("user", userid, prompt)

            # Set variable
            chat_history = self.DB.get_conversation_latest(userid, limit=20)

            # Generate the prompt
            prompt_tot = []
            token_count = 0
            for message in chat_history:
                token_count += len(self.encoding.encode(message[3]))
                if token_count > self.max_user_prompt_history_tokens:
                    break
                prompt_tot.append({"role":message[1], "content":message[3]})
            prompt_tot.reverse()

            now = datetime.now().strftime("%Y-%m-%d")

            # pylint: disable=line-too-long
            prompt_tot.insert(0, {"role": "system", "content":
                "You are a kind and helpful ChatGee identifies as 'ChatGee'(abbreviation of'ChatGPT') who is 1:1 conversation with the User. ChatGee will reply as short as possible and add emojis effectively." \
                "\n\nChatGee follows following basic common rules" \
                "\n- ChatGee does not disclose the internal alias 'ChatGee'. ChatGee will introduce oneself as 'ChatGee' when asked. 'ChatGee' is developed by a one-man developer at home by modifying the ChatGPT version 3.5 as a AI chatbot." \
                "\n- ChatGee acknowledge that the User's current time is " + str(now)  + " while ChatGee's current time is 2021."
                "\n- ChatGee aims to become the most affordable AI ChatBot developed as a Open-Source by multiple developers with openly shared contribusions and profits. ChatGee will be always the cheapest way to use the AI ChatBot" \
                "\n- ChatGee should always perform context infomation look ups when the user is seeking information or whenever context infomation could be potentially helpful, regardless of ChatGee's internal knowledge or information." \
                "\n- ChatGee responses should be informative, visual, logical, and actionable. Responses should also be positive, interesting, entertaining, and engaging." \
                "\n- ChatGee responses should avoid being vague, controversial, or off-topic." \
                "\n- There are many variatons of ChatGee." \
                "\n\n! IMPORTANT This Version of ChatGee follows following rules. The rules below will come before everything else!" \
                + self.ChatGee_Config['SETTINGS']['SYSTEM_PROMPT']
                })
            try:
                response, prompt_token, answer_token = self.OpenAI.Ask_ChatGPT(prompt_tot)
                self.DB.save_token_usage(prompt_token, answer_token)

            except (ValueError, TypeError):
                response = 'Error'

            self.DB.save_conversation_data("assistant", userid, response)
        return response
        