#!/usr/bin/env python
# -*- coding: utf-8 -*-
from libvoikko import Voikko
import appconfig
from flask import jsonify

v = appconfig.VOIKKO

def lemmatizeText(text):
    baseforms = []
    for token in v.tokens(text):
        if str(token.tokenType) == '1':
            analysis = v.analyze(token.tokenText)
            try:
                baseform = analysis[0]['BASEFORM']
                if analysis[0]['CLASS'] == 'kieltosana':
                    baseform = analysis[0]['BASEFORM'].replace('ei', ' ei').strip()
                baseforms.append(baseform)
            except:
                baseforms.append(token.tokenText)
    return ' '.join(baseforms)

def tokenizeText(text):
    wordforms = []
    for token in v.tokens(text):
        if str(token.tokenType) == '1':
            wordforms.append(token.tokenText)
    return ' '.join(wordforms)

def analyzeText(text):
    analysis_list = []
    for token in v.tokens(text):
        if str(token.tokenType) == '1':
            analysis = v.analyze(token.tokenText)

            word = {'word': token.tokenText }
            try:
                word.update(analysis[0])
                analysis_list.append(word)
            except:
                analysis_list.append(word)
    return jsonify(analysis_list)