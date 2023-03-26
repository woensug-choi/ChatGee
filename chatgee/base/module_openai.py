# -*- coding: utf-8 -*-

import tiktoken
import backoff
import openai
from datetime import datetime
import json

class ChatGee_OpenAI:

    def __init__(self,**kwargs):
        self.api_key = kwargs['api_key']
        self.model = kwargs['model']
        self.hyper_top_p = kwargs['hyper_top_p']
        self.hyper_temperature = kwargs['hyper_temperature']
        self.max_user_prompt_history_tokens = kwargs['max_user_prompt_history_tokens']
        self.system_prompt_tokens_estimate = kwargs['system_prompt_tokens_estimate']
        self.openai_api_error_log = kwargs['openai_api_error_log']
        openai.api_key = self.api_key

    @backoff.on_exception(backoff.expo, openai.error.RateLimitError)
    def chat_completions_with_backoff(self, **kwargs):
        response = openai.ChatCompletion.create(**kwargs)
        return response

    # Define a function to ask questions to OpenAI GPT
    def Ask_ChatGPT(self, prompt, perform = True):
        if perform:
            try:
                # The main ChatGPT call function wrapped to defend RateLimitError
                response = self.chat_completions_with_backoff(
                    model=self.model,
                    messages = prompt,
                    temperature = self.hyper_temperature,
                    top_p = self.hyper_top_p,
                    max_tokens= 4096 - self.max_user_prompt_history_tokens - self.system_prompt_tokens_estimate,
                )
            except openai.error.Timeout as e:
                #Handle timeout error, e.g. retry or log
                with open(self.openai_api_error_log, "a+") as f:
                    f.write(f"OpenAI API request timed out: {e}\n")
                pass
            except openai.error.APIError as e:
                #Handle API error, e.g. retry or log
                with open(self.openai_api_error_log, "a+") as f:
                    f.write(f"OpenAI API returned an API Error: {e}\n")
                pass
            except openai.error.APIConnectionError as e:
                #Handle connection error, e.g. check network or log
                with open(self.openai_api_error_log, "a+") as f:
                    f.write(f"{datetime.now()} OpenAI API request failed to connect: {e}\n")
                pass
            except openai.error.InvalidRequestError as e:
                #Handle invalid request error, e.g. validate parameters or log
                with open(self.openai_api_error_log, "a+") as f:
                    f.write(f"{datetime.now()} OpenAI API request was invalid: {e}\n")
                pass
            except openai.error.AuthenticationError as e:
                #Handle authentication error, e.g. check credentials or log
                with open(self.openai_api_error_log, "a+") as f:
                    f.write(f"{datetime.now()} OpenAI API request was not authorized: {e}\n")
                pass
            except openai.error.PermissionError as e:
                #Handle permission error, e.g. check scope or log
                with open(self.openai_api_error_log, "a+") as f:
                    f.write(f"{datetime.now()} OpenAI API request was not permitted: {e}\n")
                pass
            except openai.error.RateLimitError as e:
                #Handle rate limit error, e.g. wait or log
                with open(self.openai_api_error_log, "a+") as f:
                    f.write(f"{datetime.now()} OpenAI API request exceeded rate limit: {e}\n")
                pass

            message = response.choices[0].message.content
            return message.strip(), response.usage.prompt_tokens, response.usage.completion_tokens
        else:
            return 

# To Test:
# print(ask_gpt([{"role": "user", "content": "How are you?"}]))