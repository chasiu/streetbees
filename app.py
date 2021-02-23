from flask import Flask, render_template, request, redirect
from joblib import load

app = Flask(__name__)

clf = load("models/base_model.joblib")
vectorizer = load("models/vectorizer.joblib")
f = open("data/classes.txt", "r")
classes = {}
c = 1
for i in f:
    classes[c] = i.strip("\n")
    c += 1


@app.route("/")
def data_entry():
    pred = ""
    return render_template("index.html", pred=pred)


@app.route("/identify", methods=["POST"])
def identify():
    string = [request.form["data"]]
    # TODO Cleaning script
    vec = vectorizer.transform(string)
    pred = clf.predict(vec)[0]
    result = "Predicted class: {}".format(classes[pred])
    return render_template("index.html", pred=result)


if __name__ == "__main__":
    app.run(debug=True)