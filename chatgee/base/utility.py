# -*- coding: utf-8 -*-

import json
import yaml

def read_json(file_path):
    with open(file_path, "r") as f:
        return json.load(f)

def read_yaml(file_path):
    with open(file_path, "r") as f:
        return yaml.safe_load(f)

import requests
import time
def send_query_local(query, ChatGee_Config):

    # Define the JSON data
    data = {
        'bot': {
            'id': '6401a27b63ae0753a0e9c49d',
            'name': 'ChatGPT'
        },
        'intent': {
            'id': '6401a27c63ae0753a0e9c49d',
            'name': '폴백 블록',
            'extra': {
                'reason': {
                    'code': 1,
                    'message': 'OK'
                }
            }
        },
        'action': {
            'id': '6401a740e4f95c1f693cdc73',
            'name': 'ChatGPT Response',
            'params': {
                'prompt': query
            },
            'detailParams': {
                'prompt': {
                    'groupName': '',
                    'origin': query,
                    'value': query
                }
            },
            'clientExtra': {}
        },
        'userRequest': {
            'block': {
                'id': '6401a27c63ae0753a0e9c49d',
                'name': '폴백 블록'
            },
            'user': {
                'id': '3efb9a2e72368e6de7bda1960ae7c79c0b61bebac9c9f467ba621e9d5ae644f9b2',
                'type': 'botUserKey',
                'properties': {
                    'botUserKey': '3efb9a2e72368e6de7bda1960ae7c79c0b61bebac9c9f467ba621e9d5ae644f9b2',
                    'isFriend': True,
                    'plusfriendUserKey': 'Hr9Qhm9PRazi',
                    'bot_user_key': '3efb9a2e72368e6de7bda1960ae7c79c0b61bebac9c9f467ba621e9d5ae644f9b2',
                    'plusfriend_user_key': 'Hr9Qhm9PRazi'
                }
            },
            'utterance': 'ㅏ',
            'params': {
                'surface': 'Kakaotalk.plusfriend'
            },
            'lang': 'ko',
            'timezone': 'Asia/Seoul'
        },
        'contexts': []
    }

    # Send the JSON data as a POST request
    url = 'http://localhost:' + str(ChatGee_Config['SERVER']['PORT_NUMBER']) + '/prompt'
    response = requests.post(url, json=data)
    try:
        return json.loads(response.text)['template']['outputs'][0]['simpleText']['text']
    except:
        pass
