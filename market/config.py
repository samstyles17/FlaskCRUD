import os

class Config:
    # Define the root directory of your Flask application
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    # Specify the path to the database file
    DATABASE_PATH = os.path.join(BASE_DIR, 'instance', 'market.db')
    # Set the SQLALCHEMY_DATABASE_URI using the path to the database file
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + DATABASE_PATH
    # Optionally, you can set other configuration variables here
    # For example:
    # DEBUG = True
    SECRET_KEY = '471464f6924ede99aa7ddc5e'
