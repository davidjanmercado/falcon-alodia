#coding: utf-8

import os
import config

from flask import Flask, request
from bot import bot


app = Flask(__name__)


@app.route("/", methods=['POST'])
def root():
    return bot(request)


app.run(port=os.environ['PORT'])

# from __future__ import print_function
# import recastai

# client = recastai.Client('87a01f56c6f1cb0a2020b6568f6b80c5', 'en')
# response = client.request.analyse_text('hello')

# if response.intent:
#     print(response.intent.slug)
# if response.intent.slug == 'YOUR_EXPECTED_INTENT':
#     """Do your code..."""
