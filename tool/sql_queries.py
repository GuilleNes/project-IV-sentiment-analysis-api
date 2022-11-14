
import pandas as pd
from sql_connection import engine


# We make the query to get all the values in MySQL database

def get_everything ():
    query = """SELECT tweet, compound, username FROM queen_sentiment;"""
    df = pd.read_sql_query(query, engine)
    return df.to_dict(orient="records")

# We make the query to get the values in MySQL database with a positive index of more than the given number

def get_some_positive (numberpos):
    query = f"""SELECT tweet, pos, username 
    FROM queen_sentiment
    WHERE pos >=  {numberpos}
    AND pos < 1
    ORDER BY pos DESC;"""
    df = pd.read_sql_query(query, engine)
    return df.to_dict(orient="records")


# We make the query to get the values in MySQL database with a negative index of more than the given number

def get_some_negative (numberneg):
    query = f"""SELECT tweet, neg, username 
    FROM queen_sentiment
    WHERE neg > {numberneg}
    ORDER BY neg DESC;"""
    df = pd.read_sql_query(query, engine)
    return df.to_dict(orient="records")

## We make the query to get the compound value in MySQL database for a given name(of a person, member of the Royal Family)

def get_avg_name (name):
    query = f"""SELECT ROUND(AVG(compound), 3) as {name} FROM queen_sentiment
	WHERE tweet LIKE '%%{name}%%';"""
    df = pd.read_sql_query(query, engine)
    return df.to_dict(orient="records")


# We make the query to get the top then tweets in MySQL database for number of retweets, replies or likes (and its compound)

def get_top_ten (likes_retweets_replies):
    query = f"""SELECT tweet, tweet_cleaned, name, {likes_retweets_replies} FROM queen_sentiment
	ORDER BY {likes_retweets_replies} DESC
    LIMIT 10"""
    df = pd.read_sql_query(query, engine)
    return df.to_dict(orient="records")


# POST

def insert_one_row (name, tweet, compound):
    query = f"""INSERT INTO queen_sentiment
    (name, tweet, compound) 
    VALUES ('{name}', '{tweet}', '{compound}');
    """
    engine.execute(query)
    return "Correctly introduced!"




