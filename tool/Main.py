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

@app.route("/sql/pos/<numberpos>", )
def positive_tweets (numberpos):
    return jsonify(esecuele.get_some_positive(numberpos))

@app.route("/sql/neg/<numberneg>", )
def negative_tweets (numberneg):
    return jsonify(esecuele.get_some_negative(numberneg))

@app.route("/sql/people/<name>", )
def get_average (name): 
    return jsonify(esecuele.get_avg_name(name))

# @app.route("/sql/<numberneg>/", )
# def sa_from_character (name):
#     everything = esecuele.get_just_dialogue(name)
#     #return jsonify(everything)
#     return jsonify([sia.polarity_scores(i["dialogue"])["compound"] for i in everything])

####### POST
@app.route("/insertrow", methods=["POST"])
def try_post ():
    # Decoding params
    my_params = request.args
    scene = my_params["scene"]
    character_name = my_params["character_name"]
    dialogue = my_params["dialogue"]

    # Passing to my function: do the inserr
    esecuele.insert_one_row(scene, character_name, dialogue)
    return "Query succesfully inserted"

if __name__ == "__main__":
    app.run(port=9000, debug=True)





