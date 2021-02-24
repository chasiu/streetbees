from flask import Flask, render_template, request, redirect, jsonify
from joblib import load
import pymongo
from config import DB_URI, CLASSES, ENV

client = pymongo.MongoClient(DB_URI)
db = client["streetbees"]
logs = db.logs


app = Flask(__name__)

clf = load("models/base_model.joblib")
vectorizer = load("models/vectorizer.joblib")
classes = CLASSES


@app.route("/")
def data_entry():
    pred = ""
    return render_template("index.html", pred=pred)


@app.route("/results", methods=["POST"])
def identify():
    string = [request.form["data"]]
    # TODO Cleaning script
    vec = vectorizer.transform(string)
    pred = clf.predict(vec)[0]
    text = "Name entered: {}".format(string[0])
    result = "Predicted class: {}".format(classes[pred])
    log = {"text": str(string[0]), "predicted_class": int(pred)}
    logs.insert_one(log).inserted_id
    return render_template("index.html", pred=result, text=text)


@app.route("/api/v1/names/classify", methods=["GET"])
def classify_api():
    if "name" in request.args:
        name = str(request.args["name"])
    else:
        return "Error. Please no name field provied. Please provide a name."

    vec = vectorizer.transform([name])
    pred = clf.predict(vec)[0]
    log = {"text": str(name[0]), "predicted_class": int(pred)}
    logs.insert_one(log).inserted_id
    result = {name: classes[pred]}

    return jsonify(result)


if __name__ == "__main__":
    if ENV == "DEV":
        app.run(debug=True)
    elif ENV == "PROD":
        app.run(port=5000)