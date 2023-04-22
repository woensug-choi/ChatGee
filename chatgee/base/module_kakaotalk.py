# -*- coding: utf-8 -*-
"""Kakatalk Module for ChatGee"""

from copy import deepcopy

# Kakaotalk default respond format
base_response = {'version': '2.0', 'template': {
    'outputs': [], 'quickReplies': []}}
carouselbase_response = {'version': '2.0', 'template': {'outputs': [
    {"carousel": {"type": "basicCard", "items": []}}], 'quickReplies': []}}

class ChatGee_KakaoTalk:
    """KakaoTalk Module Class Object"""

    # Bare text respond function
    @staticmethod
    def insert_text(text):
        """Insert text to response"""
        new_response = deepcopy(base_response)
        new_response['template']['outputs'] = [{"simpleText": {"text": text}}]
        return new_response

    # Make quick reply content
    @staticmethod
    def make_reply(label, message):
        """Make quick reply content"""
        return {'action': 'message', 'label': label, 'messageText': message}

    # Make quick reply content
    @staticmethod
    def make_reply_labelOnly(label):
        """Make quick reply content"""
        return {'action': 'message', 'label': label}

    # Add quick reply button
    @staticmethod
    def insert_replies(new_response, reply):
        """Add quick reply button"""
        new_response['template']['quickReplies'].append(reply)
        return new_response

    # Card response
    @staticmethod
    def insert_card(title, description, image_url=None, width=None, height=None):
        """Card response"""
        new_response = deepcopy(base_response)
        if image_url is not None:
            if width is not None and height is not None:
                new_response['template']['outputs'] = [{'basicCard': {
                    'title': title,
                    'description': description,
                    'thumbnail': {"imageUrl": image_url, 'fixedRatio': True,
                                  'width': width, 'height': height},
                    'buttons': []
                }}]
            else:
                new_response['template']['outputs'] = [{'basicCard': {
                    'title': title,
                    'description': description,
                    'thumbnail': {"imageUrl": image_url},
                    'buttons': []
                }}]
        else:
            new_response['template']['outputs'] = [{'basicCard': {
                'title': title,
                'description': description,
                'buttons': []
            }}]
        return new_response

    # Add additional card respond
    @staticmethod
    def plus_card(new_response, title, description, image_url=None, width=None, height=None):
        """Add additional card respond"""
        if image_url is not None:
            if width is not None and height is not None:
                new_response['template']['outputs'].append({'basicCard': {
                    'title': title,
                    'description': description,
                    'thumbnail': {"imageUrl": image_url, 'fixedRatio': True,
                                  'width': width, 'height': height},
                    'buttons': []
                }})
            else:
                new_response['template']['outputs'].append({'basicCard': {
                    'title': title,
                    'description': description,
                    'thumbnail': {"imageUrl": image_url},
                    'buttons': []
                }})
        else:
            new_response['template']['outputs'].append({'basicCard': {
                'title': title,
                'description': description,
                'buttons': []
            }})
        return new_response

    # Add url buttom to card
    @staticmethod
    def insert_button_url(new_response, label, web_url):
        """Add url buttom to card"""
        new_response['template']['outputs'][-1]['basicCard']['buttons'].append({
            "action": "webLink",
            "label": label,
            "webLinkUrl": web_url
        })
        return new_response

    # Add text button to card
    @staticmethod
    def insert_button_text(new_response, label, text):
        """Add text button to card"""
        new_response['template']['outputs'][-1]['basicCard']['buttons'].append({
            "action": "message",
            "label": label,
            "messageText": text
        })
        return new_response

    # Add text button to card
    @staticmethod
    def insert_button_text_empty(new_response, label):
        """Add text button to card"""
        new_response['template']['outputs'][-1]['basicCard']['buttons'].append({
            "action": "message",
            "label": label,
            "messageText": None
        })
        return new_response

    # List Response
    @staticmethod
    def insert_list(title):
        """List Response"""
        new_response = deepcopy(base_response)
        new_response['template']['outputs'] = [{'listCard': {
            'header': {"title": title},
            'items': [],
            'buttons': []
        }}]
        return new_response

    # List Response Add Item
    @staticmethod
    def insert_list_item(new_response, title, web_url, description=" ", imageUrl=None):
        """List Response Add Item"""
        if imageUrl is not None:
            new_response['template']['outputs'][0]['listCard']['items'].append({
                "title": title,
                "description": description,
                "imageUrl": imageUrl,
                "link": {"web": web_url}
            })
        else:
            new_response['template']['outputs'][0]['listCard']['items'].append({
                "title": title,
                "description": description,
                "link": {"web": web_url}
            })
        return new_response

    # List Reponse Add Button
    @staticmethod
    def insert_list_button(new_response, label, web_url):
        """List Reponse Add Button"""
        new_response['template']['outputs'][0]['listCard']['buttons'].append({
            "action": "webLink",
            "label": label,
            "webLinkUrl": web_url
        })
        return new_response

    # Carousel Card
    @staticmethod
    def insert_carousel_card(title=None, description=None, image_url=None, width=None, height=None):
        """Carousel Card"""
        new_response = deepcopy(carouselbase_response)
        if image_url is not None:
            if width is not None and height is not None:
                new_response['template']['outputs'][-1]['carousel']['items'].append({
                    'title': title,
                    'description': description,
                    'thumbnail': {"imageUrl": image_url, 'fixedRatio': True,
                                  'width': width, 'height': height},
                    'buttons': []
                })
            else:
                new_response['template']['outputs'][-1]['carousel']['items'].append({
                    'title': title,
                    'description': description,
                    'thumbnail': {"imageUrl": image_url},
                    'buttons': []
                })
        else:
            new_response['template']['outputs'][-1]['carousel']['items'].append({
                'title': title,
                'description': description,
                'buttons': []
            })
        return new_response

    # Carousel Card Add Another
    @staticmethod
    def plus_carousel_card(new_response, title=None, description=None,
                           image_url=None, width=None, height=None):
        """Carousel Card Add Another"""
        if image_url is not None:
            if width is not None and height is not None:
                new_response['template']['outputs'][-1]['carousel']['items'].append({
                    'title': title,
                    'description': description,
                    'thumbnail': {"imageUrl": image_url, 'fixedRatio': True,
                                  'width': width, 'height': height},
                    'buttons': []
                })
            else:
                new_response['template']['outputs'][-1]['carousel']['items'].append({
                    'title': title,
                    'description': description,
                    'thumbnail': {"imageUrl": image_url},
                    'buttons': []
                })
        else:
            new_response['template']['outputs'][-1]['carousel']['items'].append({
                'title': title,
                'description': description,
                'buttons': []
            })
        return new_response


    # Carousel Card Add Head Section
    @staticmethod
    def insert_carousel_head(new_response, title, description, image_url):
        """Carousel Card Add Head Section"""
        new_response['template']['outputs'][-1]['carousel']["header"] = {
            "title": title,
            "description": description,
            "thumbnail": {
                "imageUrl": image_url
            }
        }
        return new_response

    # Carousel url button
    @staticmethod
    def insert_carousel_button_url(new_response, label, web_url):
        """Carousel url button"""
        new_response['template']['outputs'][-1]['carousel']['items'][-1]['buttons'].append({
            "action": "webLink",
            "label": label,
            "webLinkUrl": web_url
        })
        return new_response


    # Carousel text button
    @staticmethod
    def insert_carousel_button_text(new_response, label, text):
        """Carousel text button"""
        new_response['template']['outputs'][-1]['carousel']['items'][-1]['buttons'].append({
            "action": "message",
            "label": label,
            "messageText": text
        })
        return new_response
