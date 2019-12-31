from flask import Flask, render_template
from utils import get_data

app = Flask(__name__)


@app.route('/')
def get_home_page():
    return render_template("home.html", data=get_data())


@app.route('/object/<idnum>')
def get_object(idnum):
    img = idnum + ".jpg"
    for item in get_data():
        if idnum == item['title'].replace(' ', "_").lower():
            count = item['text'].count(" ")
            return render_template("object.html", title=item['title'], text=item['text'], count=count, img=img)


@app.route('/author')
def get_author():
    return render_template('author.html')


if __name__ == "__main__":
    app.run(debug=True)

