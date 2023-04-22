# -*- coding: utf-8 -*-
"""OpenAI Module for ChatGee"""

from datetime import datetime

import backoff
import openai

class ChatGee_OpenAI:
    """OpenAI Module Class Object"""

    def __init__(self,**kwargs):
        """Initialize OpenAI Module Class Object"""
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
        """Chat Completion with Backoff"""
        response = openai.ChatCompletion.create(**kwargs)
        return response

    # Define a function to ask questions to OpenAI GPT
    def Ask_ChatGPT(self, prompt, perform = True):
        """Ask questions to OpenAI GPT"""
        if perform:
            try:
                # The main ChatGPT call function wrapped to defend RateLimitError
                response = self.chat_completions_with_backoff(
                    model=self.model,
                    messages = prompt,
                    temperature = self.hyper_temperature,
                    top_p = self.hyper_top_p,
                    max_tokens= 4096 - self.max_user_prompt_history_tokens
                                - self.system_prompt_tokens_estimate,
                )
            except openai.error.Timeout as e:
                #Handle timeout error, e.g. retry or log
                with open(self.openai_api_error_log, "a+", encoding="utf-8") as f:
                    f.write(f"OpenAI API request timed out: {e}\n")
            except openai.error.APIError as e:
                #Handle API error, e.g. retry or log
                with open(self.openai_api_error_log, "a+", encoding="utf-8") as f:
                    f.write(f"OpenAI API returned an API Error: {e}\n")
            except openai.error.APIConnectionError as e:
                #Handle connection error, e.g. check network or log
                with open(self.openai_api_error_log, "a+", encoding="utf-8") as f:
                    f.write(f"{datetime.now()} OpenAI API request failed to connect: {e}\n")
            except openai.error.InvalidRequestError as e:
                #Handle invalid request error, e.g. validate parameters or log
                with open(self.openai_api_error_log, "a+", encoding="utf-8") as f:
                    f.write(f"{datetime.now()} OpenAI API request was invalid: {e}\n")
            except openai.error.AuthenticationError as e:
                #Handle authentication error, e.g. check credentials or log
                with open(self.openai_api_error_log, "a+", encoding="utf-8") as f:
                    f.write(f"{datetime.now()} OpenAI API request was not authorized: {e}\n")
            except openai.error.PermissionError as e:
                #Handle permission error, e.g. check scope or log
                with open(self.openai_api_error_log, "a+", encoding="utf-8") as f:
                    f.write(f"{datetime.now()} OpenAI API request was not permitted: {e}\n")
            except openai.error.RateLimitError as e:
                #Handle rate limit error, e.g. wait or log
                with open(self.openai_api_error_log, "a+", encoding="utf-8") as f:
                    f.write(f"{datetime.now()} OpenAI API request exceeded rate limit: {e}\n")

            message = response.choices[0].message.content
            return message.strip(), response.usage.prompt_tokens, response.usage.completion_tokens
        # if not perform, return empty string
        return "", 0, 0

# To Test:
# print(ask_gpt([{"role": "user", "content": "How are you?"}]))
