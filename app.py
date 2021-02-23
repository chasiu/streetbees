from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.route("/")
def data_entry():
    return render_template("index.html")


@app.route("/identify", methods=["POST"])
def identify():
    data = request.form["data"]

    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)