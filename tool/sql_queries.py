
import pandas as pd
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

def get_top_five (likes_retweets_replies):
    query = f"""SELECT tweet, name, {likes_retweets_replies} FROM queen_sentiment
	ORDER BY {likes_retweets_replies} DESC
    LIMIT 10"""
    df = pd.read_sql_query(query, engine)
    return df.to_dict(orient="records")


def insert_one_row (name, tweet, compound):
    query = f"""INSERT INTO queen_sentiment
    (name, tweet, compound) 
    VALUES ({name}, '{tweet}', '{compound}');
    """
    engine.execute(query)
    return f"Correctly introduced!"