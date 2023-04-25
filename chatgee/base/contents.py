# -*- coding: utf-8 -*-
"""
Contents Generator For Kakaotalk Messages
"""

from base.module_kakaotalk import ChatGee_KakaoTalk


# Greetings
def generate_greetings(ChatGee_Config, content):
    """New user message"""
    response = ChatGee_KakaoTalk.insert_card(
        title=ChatGee_Config['CONTENTS']['GREETINGS']['TITLE'],
        description=ChatGee_Config['CONTENTS']['GREETINGS']['TEXTS'])
    try:
        content = content['userRequest']['utterance']
        content = ''.join(str(e) for e in content)
        response = ChatGee_KakaoTalk.insert_button_text(response, '📓 사용설명서 보기', '📓 사용설명서')
        response = ChatGee_KakaoTalk.insert_button_text(response, '이전 말 다시 적기 ✍🏻', content)
    except KeyError:
        response = ChatGee_KakaoTalk.insert_button_text(response, '📓 사용설명서 보기', '📓 사용설명서')
        response = ChatGee_KakaoTalk.insert_button_text(response, '넌 뭐니??!', "넌 뭐니??!")

    return response

# Advertisement
def generate_advertisement(ChatGee_Config, response):
    """Advertisement message"""
    response = ChatGee_KakaoTalk.plus_card(response, title='',
                                description=ChatGee_Config['CONTENTS']['ADVERTISEMENT']['TEXTS'])
    response = ChatGee_KakaoTalk.insert_button_url(
        response, '더알고 싶으시면 🚀', ChatGee_Config['CONTENTS']['ADVERTISEMENT']['LINK'])
    if len(ChatGee_Config['CONTENTS']['SUPPORT_LINK']) != 0:
        ChatGee_KakaoTalk.insert_button_url(
            response, '후원하기🧋🧋', ChatGee_Config['CONTENTS']['SUPPORT_LINK'])

    return response

# Document
def generate_documents(ChatGee_Config):
    """How-to Document message"""
    response = ChatGee_KakaoTalk.insert_carousel_card(title = '📓 사용설명서 for 🌱🐤',
                                    description = '아는만큼 잘 부려먹는 AI챗봇🥺\n이것만 보면 사용법은 완벽 😎👀',
                                    width=30, height=None)

    response = ChatGee_KakaoTalk.plus_carousel_card(response, title = "",
                                    description = ChatGee_Config['CONTENTS']['EXPLAIN']['TEXTS'])
    if len(ChatGee_Config['CONTENTS']['SUPPORT_LINK']) != 0:
        ChatGee_KakaoTalk.insert_carousel_button_url(
            response, '후원하기🧋🧋', ChatGee_Config['CONTENTS']['SUPPORT_LINK'])

    response = ChatGee_KakaoTalk.plus_carousel_card(response,title = '',
                                    description =
                                    '🤖 챗지가 사람보다 훨~씬 나아요\n'
                                    '   ‣ 어려운 말도 자연스럽게 척척해요\n'
                                    '   ‣ 철학도 과학도 어려울수록 더 잘해요\n'
                                    '💩 챗지는 가끔 상식이 없어요.\n'
                                    '   ‣ 거짓말도 수준급이예요\n'
                                    '   ‣ 21년 이후는 몰라요🐢'
                                    ,width=None, height=None)
    ChatGee_KakaoTalk.insert_carousel_button_text(response, '현재 대통령이 문재인이라구?', '지금 한국 대통령 알려줘')
    ChatGee_KakaoTalk.insert_carousel_button_text(response, '가짜회사 "허씨초콜릿"', '허씨초콜릿 역사 알려줘')

    response = ChatGee_KakaoTalk.plus_carousel_card(response, title = "",
                                    description =
                                    '🧠 챗지는 이전 대화를 기억해요\n'
                                    '   ‣ 최대 10개 대화 핑퐁을 기억 🤓\n'
                                    '   ‣ 대화를 이어가다 요약해보세요\n'
                                    '     "이제까지의 대화를 요약해줘"\n\n'
                                    '🪄✨💆‍♂️ 기억 리셑\n'
                                    '   ‣ 💫 새로운 시작 = 이전기억 삭제',
                                    image_url=None, width=None, height=None)
    ChatGee_KakaoTalk.insert_carousel_button_text(response, '💫 새로운 시작', '💫 새로운 시작')

    response = ChatGee_KakaoTalk.plus_carousel_card(response, title = "",
                                    description =
                                    '본 챗봇는 "챗지" 카카오톡 챗봇을\n'
                                    '기반으로 만들어졌습니다!😊\n\n'
                                    '오픈소스로🧐 소스코드 공개!,'
                                    '가장 재밌는 AI챗봇이 되길\n'
                                    '희망합니다✨✨✨\n'
                                    '문의사항 : talkchatgpt@지메일',
                                    image_url=None, width=None, height=None)

    ChatGee_KakaoTalk.insert_carousel_button_url(
        response, '챗지 구경가기 🧐', 'https://pf.kakao.com/_RxoCkxj')
    ChatGee_KakaoTalk.insert_carousel_button_url(
        response, '챗지 대화해보기 🤖', 'https://pf.kakao.com/_RxoCkxj/chat')

    return response
