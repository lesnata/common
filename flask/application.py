# import os
# import requests

from flask import Flask, session, render_template, request, redirect

app = Flask(__name__)


# # Check for environment variable
# if not os.getenv("DATABASE_URL"):
#     raise RuntimeError("DATABASE_URL is not set")
#
# # Set up database
# engine = create_engine(os.getenv("DATABASE_URL"))
# db = scoped_session(sessionmaker(bind=engine))

fruits_list = ['Melon', 'Apple', 'Strawberry', 'Grape']
vegetables_list = ['Beans', 'Carrot', 'Beetroot', 'Cucumber']

@app.route("/")
def home():
    global vegetables_list, fruits_list
    total_list = vegetables_list + fruits_list
    return render_template("home.html", total_list=total_list)


@app.route("/vegetables", methods=['GET', 'POST'])
def vegetables():
    global vegetables_list
    return render_template("vegetables.html", vegetables_list=vegetables_list)


@app.route("/fruits", methods=['GET', 'POST'])
def fruits():
    global fruits_list
    return render_template("fruits.html", fruits_list=fruits_list)


@app.route("/search", methods=['GET', 'POST'])
def search():
    pass


@app.route("/404", methods=['GET', 'POST'])
def page404():
    return redirect("404.html", code=404)


app.run(debug=True)
