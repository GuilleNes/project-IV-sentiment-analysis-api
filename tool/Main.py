# Modules for connecting with the API

from flask import Flask, request, jsonify
import markdown.extensions.fenced_code
import sql_queries as esecuele


# Functions for connecting to the API

app = Flask(__name__)

# Render the markdwon
@app.route("/")
def readme ():
    readme_file = open("README.md", encoding='utf-8')
    return markdown.markdown(readme_file.read(), extensions = ["fenced_code"])

# GET ENDPOINTS: SQL 


# SQL get everything
@app.route("/sql/")
def sql ():
    return jsonify(esecuele.get_everything())

# SQL get the positive sentiment tweets
@app.route("/sql/pos/<numberpos>", )
def positive_tweets (numberpos):
    return jsonify(esecuele.get_some_positive(numberpos))

# SQL get the positive sentiment tweets
@app.route("/sql/neg/<numberneg>", )
def negative_tweets (numberneg):
    return jsonify(esecuele.get_some_negative(numberneg))

# SQL get the tweets related to a given person
@app.route("/sql/people/<name>", )
def get_average (name): 
    return jsonify(esecuele.get_avg_name(name))

# SQL get a list of the top 10 tweets for number of likes, replies or retweets
@app.route("/sql/count/<likes_retweets_replies>", )
def get_top (likes_retweets_replies): 
    return jsonify(esecuele.get_top_five(likes_retweets_replies))


####### POST

@app.route("/insertrow", methods=["POST"])
def try_post ():
# Decoding params       
    my_params = request.args
    name = my_params["name"]
    tweet = my_params["tweet"]
    compound = my_params["compound"]


# Passing to my function: do the insert
    esecuele.insert_one_row(name, tweet, compound)
    return "Query succesfully inserted"

if __name__ == "__main__":
    app.run(port=9000, debug=True)





