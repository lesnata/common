from datetime import timedelta

from flask import Flask, render_template, session
from blueprint.products.products_main import products
from blueprint.supermarkets.supermarkets_main import supermarkets
from config import Config


app = Flask(__name__)
app.config["SECRET_KEY"] = "super_secret_key"
app.register_blueprint(products)
app.register_blueprint(supermarkets)
app.permanent_session_lifetime = timedelta(seconds=10)


@app.route('/home')
def get_home():
    return render_template("home.html")


@app.errorhandler(404)
def handle_404(error):
    return render_template("error_404.html")


if __name__ == '__main__':
    app.run(debug=True)

