import pandas as pd
import os

import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.corpus import stopwords

from wordcloud import WordCloud, STOPWORDS
from langdetect import detect
from textblob import TextBlob

import sqlalchemy as alch
from getpass import getpass
import cleaning_functions as cleafun

import numpy as np
from PIL import Image
import matplotlib.pyplot as plt


# First of all we import the df from CSV with all the tweets

df = pd.read_csv("../data/queen.csv")

# We apply the first function to delete the columns we are not going to need

cleafun.drop_column(df, ["conversation_id", "timezone", "created_at", "user_id", 'place', 'mentions', 'urls', 'photos', 'hashtags','cashtags', 'link',"retweet", 'quote_url', 'video','thumbnail', 'near', 'geo', 'source', 'user_rt_id', 'user_rt', 'retweet_id', 'reply_to', 'retweet_date', 'translate', 'trans_src', 'trans_dest'])


# Unfortunately, some of the values on the df have emojis and this causes a problem when trying to upload SQL with the data, so we apply regex to clean them.
df.iloc[[4181]]

cleafun.regex_column(df, "name")
cleafun.regex_column(df, "tweet")


# Now we have our data cleaned.
df.iloc[[4181]]

# We save our df and upload it to MySQL.
df.to_csv("../data/queen_cleaned.csv", index= False)

# We bring all the data to a dataframe from MySQL 

password = os.getenv("password_mysql")
dbName = "project_4"
connectionData=f"mysql+pymysql://root:{password}@localhost/{dbName}"
engine = alch.create_engine(connectionData)

# Using stopwords, we filter and clean all the common words that are not going to add any value to our Sentiment Analysis

nltk.download('stopwords')
stop = stopwords.words('english')

cleafun.words_filter(df, "tweet_cleaned", "tweet", stop)

nltk.downloader.download('vader_lexicon')

sia = SentimentIntensityAnalyzer()

df[['neg', 'neu', 'pos', 'compound']] = df['tweet_cleaned'].apply(sia.polarity_scores).apply(pd.Series)


# Finally, we save this DF with the new Sentiment Analysis columns and we upload it to SQL

df.to_csv("../data/queen_sentiment.csv", index= False)



# The last step we are going to do is a Wordcloud image with the most common words from one of the tweets.

mask = np.array(Image.open("../data/Queen.jpg"))

text = df['tweet_cleaned'][4]
                
wordcloud = WordCloud(
    mask = mask,
    background_color = "black",
    height = mask.shape[0],
    max_font_size = 500,
    width = mask.shape[1]
    ).generate(text)

# Display the generated image:
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()

plt.savefig("../Data/queen_figure.png", dpi=300)