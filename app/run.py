#!/usr/bin/env python
# -*- coding: utf-8 -*-

import flask
from flask import request, make_response

import appconfig
import utils

v = appconfig.VOIKKO

app = flask.Flask(__name__)

@app.route("/")
def hello():
    return "Welcome to Voikko API!"

@app.route('/lemmatize/', methods=['GET'])
def get_lemmas():
    if 'text' in request.args:
        text = request.args['text']
    else:
        return make_response("Request cannot be processed. Make sure you have provided a text parameter.", 400)

    return utils.lemmatizeText(text)

@app.route('/tokenize/', methods=['GET'])
def get_tokens():
    if 'text' in request.args:
        text = request.args['text']
    else:
        return make_response("Request cannot be processed. Make sure you have provided a text parameter.", 400)

    return utils.tokenizeText(text)

@app.route('/analyze/', methods=['GET'])
def get_analysis():
    if 'text' in request.args:
        text = request.args['text']
    else:
        return make_response("Request cannot be processed. Make sure you have provided a text parameter.", 400)

    return utils.analyzeText(text)

@app.route('/health/', methods=['GET'])
def check_health():
    return make_response("OK", 200)