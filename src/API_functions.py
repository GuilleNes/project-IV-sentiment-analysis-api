# from flask import Flask, request, jsonify
import random
import pandas as pd
import requests as re
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from src.sql_connection import engine

sia = SentimentIntensityAnalyzer()


# With this function, we search for the compound of a specific person named on the tweets
def compound_by_name(name):
    try:
        url = f"http://127.0.0.1:9000/sql/people/{name}"
        test = re.get(url).json()[0]
        df = pd.DataFrame.from_dict([test])
        return df
    except Exception:
        return "Seems that the value you have entered is not correct; try again"  


# With this function, we search for the top ten tweets for the number of the given kind (likes, replies or retweets) and we add the compound
def get_top_tweets(x):
    try:
        url = f"http://127.0.0.1:9000/sql/count/{x}"
        test = re.get(url).json()
        df = pd.json_normalize(test)
        df["compound"] = [sia.polarity_scores(i["tweet"])["compound"] for i in test]
        return df 
    except Exception:
        return "Seems that the value you have entered is not correct; try again"


# With this function we look for the tweets with a positive index greater than the given number 

def get_pos(numberpos):  # sourcery skip: inline-immediately-returned-variable
    try:
        url = f"http://127.0.0.1:9000/sql/pos/{numberpos}"
        return pd.json_normalize(re.get(url).json())
    except Exception:
        return "Seems that the value you have entered is not correct; try again"


# With this function we look for the tweets with a negative index greater than the given number 

def get_neg(numberneg):
    try:
        url = f"http://127.0.0.1:9000/sql/neg/{numberneg}"
        return pd.json_normalize(re.get(url).json())
    except Exception:
        return "Seems that the value you have entered is not correct; try again"


# We get a random tweet from our database

def get_random_():
    url = "http://127.0.0.1:9000/sql"
    df = pd.DataFrame.from_dict(re.get(url).json())
    random_index = random.randint(0, len(pd.json_normalize(re.get(url).json())))
    return df.iloc[random_index]

# Function for check if the insert row has worked

def check_new_row ():
    query = """SELECT * FROM queen_sentiment
	ORDER BY id ASC
    LIMIT 1;
    """
    df = pd.read_sql_query(query, engine)
    return df.to_dict(orient="records")
    

