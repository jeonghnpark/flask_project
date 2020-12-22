from flask import Flask, render_template, request

app = Flask("First")


@app.route("/")
def home():
    # word3=request.args.get("word3")
    return render_template("potato.html")


@app.route("/contact")
def potato():
    return "potato"


@app.route("/<username>")
def name(username):
    return f"who is {username}?"


@app.route("/report")
def rep():
    word_to_get = request.args.get("word2")
    return render_template("report1.html", word_from_query=word_to_get)


app.run(host="localhost")
