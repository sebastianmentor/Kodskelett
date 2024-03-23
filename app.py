from flask import Flask, render_template, redirect, url_for, request
from flask_migrate import Migrate, upgrade
from models import db, seed_data, Employee
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv('LOCAL_DATABASE_URI')

db.init_app(app)

migrate = Migrate(app, db)

@app.route("/")
def home_page():
    text = "Hello world"
    return render_template('index.html', text=text)

if __name__ == '__main__':
    with app.app_context():
        upgrade()
        seed_data(db)

    app.run(debug=True)