# Modules for connecting with the API

# import random
# import markdown.extensions.fenced_code
import numpy as np
import pandas as pd
# import requests
from flask import Flask, jsonify, request
# import tool.sql_queries as esecuele
# from nltk.sentiment.vader import SentimentIntensityAnalyzer
from sql_connection import engine


def get_everything ():
    query = """SELECT tweet, compound, username FROM queen_sentiment;"""
    df = pd.read_sql_query(query, engine)
    return df.to_dict(orient="records")

def get_some_positive (numberpos):
    query = f"""SELECT tweet, compound, pos, username 
    FROM queen_sentiment
    WHERE pos >  {numberpos};"""
    df = pd.read_sql_query(query, engine)
    return df.to_dict(orient="records")

def get_some_negative (numberneg):
    query = f"""SELECT tweet, compound, neg, username 
    FROM queen_sentiment
    WHERE neg > {numberneg};"""
    df = pd.read_sql_query(query, engine)
    return df.to_dict(orient="records")

def get_avg_name (name):
    query = f"""SELECT ROUND(AVG(compound), 3) as {name} FROM queen_sentiment
	WHERE tweet LIKE '%%{name}%%';"""
    df = pd.read_sql_query(query, engine)
    return df.to_dict(orient="records")


# def insert_one_row (scene, character_name, dialogue):
#     query = f"""INSERT INTO users
#     (scene, character_name, dialogue) 
#     VALUES ({scene}, '{character_name}', '{dialogue}');
#     """
#     engine.execute(query)
#     return f"Correctly introduced!"