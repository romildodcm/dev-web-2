from flask import Flask  # Import the Flask class
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)    # Create an instance of the class for our use

PROJECT_DIR = os.path.dirname(os.path.realpath(__file__))
DB_FILE = os.path.join(PROJECT_DIR, '../manter/manter2.db')

app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_FILE}'

db = SQLAlchemy(app) # Um objeto do SQLAlchemy