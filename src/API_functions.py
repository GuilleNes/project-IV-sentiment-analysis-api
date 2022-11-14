import requests as re
import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from flask import Flask, request, jsonify
import random
sia = SentimentIntensityAnalyzer()


# With this function, we search for the compound of a specific person named on the tweets
def compound_by_name():
    new_dict = {}
    name = input("Which name would you like to look for?: ")
    try:
        url = f"http://127.0.0.1:9000/sql/people/{name}"
        new_dict[name] = re.get(url).json()
        return pd.DataFrame.from_dict(new_dict, orient="index")     

    except:
        return "Seems that the value you have entered is not correct; try again"


# With this function, we search for the top ten tweets for the number of the given kind (likes, replies or retweets) and we add the compound
def get_top_tweets(kind):
    try:
        url = f"http://127.0.0.1:9000/sql/count/{x}"
        test = re.get(url).json()
        df = pd.json_normalize(test)
        df["compound"] = [sia.polarity_scores(i["tweet"])["compound"] for i in test]
        return df 
    except:
        return "Seems that the value you have entered is not correct; try again"


# With this function we look for the tweets with a positive index greater than the given number 

def get_pos(numberpos):
    try:
        url = f"http://127.0.0.1:9000/sql/pos/{numberpos}"
        df = pd.json_normalize(re.get(url).json())
        return df 
    except:
        return "Seems that the value you have entered is not correct; try again"


# With this function we look for the tweets with a negative index greater than the given number 

def get_neg(numberneg):
    try:
        url = f"http://127.0.0.1:9000/sql/neg/{numberneg}"
        df = pd.json_normalize(re.get(url).json())
        return df 
    except:
        
        return "Seems that the value you have entered is not correct; try again"

def get_random_():
    url = f"http://127.0.0.1:9000/sql"
    df = pd.json_normalize(re.get(url).json())
    random_index = random.randint(0, len(df))
    return df.iloc[random_index]


    
