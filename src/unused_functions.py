# Modules for connecting with the API
# import random
# import markdown.extensions.fenced_code
# import numpy as np
# import requests
# from flask import Flask, jsonify, request
# from nltk.sentiment.vader import SentimentIntensityAnalyzer

@app.route("/sql/<numberneg>/", )
def sa_from_character (name):
    everything = esecuele.get_just_dialogue(name)
    #return jsonify(everything)
    return jsonify([sia.polarity_scores(i["dialogue"])["compound"] for i in everything])