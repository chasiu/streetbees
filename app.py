from flask import Flask, render_template, request, redirect, jsonify
from joblib import load
import pymongo
from config import DB_URI, CLASSES, ENV
import text_processing as tp
import nltk

client = pymongo.MongoClient(DB_URI)
db = client["streetbees"]
logs = db.logs
stopwords = nltk.corpus.stopwords.words("english")

app = Flask(__name__)

pipe = load("models/model.joblib")

classes = CLASSES


@app.route("/")
def data_entry():
    pred = ""
    return render_template("index.html", pred=pred)


@app.route("/results", methods=["POST"])
def identify():
    raw_name = request.form["data"]
    name = raw_name.lower()
    name = tp.drop_stop(name, stopwords)
    name = tp.drop_chars(name)
    name = tp.drop_whitespace(name)
    pred = pipe.predict([name])[0]
    text = "Name entered: {}".format(raw_name)
    result = "Predicted class: {}".format(classes[pred])
    log = {"text": str(raw_name), "predicted_class": int(pred)}
    logs.insert_one(log).inserted_id
    return render_template("index.html", pred=result, text=text)


@app.route("/api/v1/names/classify", methods=["GET"])
def classify_api():
    if "name" in request.args:
        raw_name = str(request.args["name"])
    else:
        return "Error. Please no name field provied. Please provide a name."
    name = raw_name.lower()
    name = tp.drop_stop(name, stopwords)
    name = tp.drop_chars(name)
    name = tp.drop_whitespace(name)
    pred = pipe.predict([name])[0]
    log = {"text": str(raw_name), "predicted_class": int(pred)}
    logs.insert_one(log).inserted_id
    result = {name: classes[pred]}

    return jsonify(result)


if __name__ == "__main__":
    if ENV == "DEV":
        app.run(debug=True)
    elif ENV == "PROD":
        app.run(port=5000)