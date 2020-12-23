import requests

from flask import Flask, render_template, request, redirect

BASE_URL = "https://hn.algolia.com/api/v1"

# This URL gets the newest stories.
NEW = f"{BASE_URL}/search_by_date?tags=story"

# This URL gets the most popular stories
POPULAR = f"{BASE_URL}/search?tags=story"


# This function makes the URL to get the detail of a storie by id.
# Heres the documentation: https://hn.algolia.com/api
def make_detail_url(id):
    return f"{BASE_URL}/items/{id}"


db = {}
app = Flask("DayNine")

@app.route("/search")
def new():
    order = "new"
    data = requests.get(NEW).json()
    # print(data['hits'])
    # for story in data['hits']:
    #     print(story['title'])
    # return render_template("index.html",order_by=order, data=data.get['hits'])
    return render_template("new.html", order_by=order, stories=data.get('hits'))

@app.route("/<id>")
def detail(id):
    url=f"https://hn.algolia.com/api/v1/items/{id}"
    comments=requests.get(url).json()
    return render_template("detail.html", comments=comments)

# @app.route("/detail")
# def detail():
#     item=request.args.get('item')
#     print(item)
#     url=f"https://hn.algolia.com/api/v1/items/{item}"
#     # url = make_detail_url(id)
#     # url=f"https://hn.algolia.com/api/v1/items/{item}"
#     # d=requests.get(make_detail_url(id)).json()['children']
#     d = requests.get(url).json()
#     # children=d['children']
#     # for child in d:
#     #     print(child['text'])
#     # return render_template("detail.html")
#     return render_template("detail.html", comments=d)
#     # return redirect("/")
#

@app.route("/")
def home():
    order = "popular"
    data = requests.get(POPULAR).json()
    # print(data['hits'])
    # for story in data['hits']:
    #     print(story['title'])
    # return render_template("index.html",order_by=order, data=data.get['hits'])
    return render_template("index.html", order_by=order, stories=data.get('hits'))


app.run(host="localhost")
# app.run(host="0.0.0.0")
