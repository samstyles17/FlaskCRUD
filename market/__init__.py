from flask import Flask
from market.config import Config  # Importing Config class from config.py
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)


# Using the Config class to configure the Flask app
app.config.from_object(Config)

# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///instance/market.db'

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager()
from market import routes
