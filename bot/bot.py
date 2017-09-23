# coding: utf-8

import os
import recastai

from flask import jsonify

# request_token = os.environ['REQUEST_TOKEN']
token = '87a01f56c6f1cb0a2020b6568f6b80c5'


def bot(payload):
    connect = recastai.Connect(token=token, language='en')
    request = recastai.Request(token=token)

    answer = request.post('https://api.recast.ai/v2/request',
                          {'text': 'hey I am mainak'})

    message = connect.parse_message(payload)
    print(message)
    response = request.converse_text(message.content,
                                     conversation_token=message.sender_id)

    replies = [{'type': 'text', 'content': r} for r in response.replies]
    connect.send_message(replies, message.conversation_id)

    return jsonify(status=200)
