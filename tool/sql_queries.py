# Modules for connecting with the API

from flask import Flask, request, jsonify
import random
import numpy as np
import markdown.extensions.fenced_code
import requests

# import tool.sql_queries as esecuele
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from sql_connection import engine
import pandas as pd


def get_everything ():
    query = """SELECT * FROM queen_sentiment;"""
    df = pd.read_sql_query(query, engine)
    return df.to_dict(orient="records")

def get_some_positive (number):
    query = f"""SELECT * 
    FROM queen_sentiment
    WHERE pos >  {number};"""

def get_some_negative (number):
    query = f"""SELECT * 
    FROM queen_sentiment
    WHERE neg >  {number};"""

    df = pd.read_sql_query(query, engine)
    return df.to_dict(orient="records")

def get_avg_name (name):
    query = f"""SELECT ROUND(AVG(compound), 3) FROM queen_sentiment
	WHERE tweet LIKE '%{name}%';"""
    df = pd.read_sql_query(query, engine)
    return df.to_dict(orient="records")


# def insert_one_row (scene, character_name, dialogue):
#     query = f"""INSERT INTO users
#     (scene, character_name, dialogue) 
#     VALUES ({scene}, '{character_name}', '{dialogue}');
#     """
    # engine.execute(query)
    # return f"Correctly introduced!"