from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# database config
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///myDB.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # to supress warnings
db = SQLAlchemy(app)

# index route
@app.route('/')
def index():
  return 'Congrats! This Flask application now supports databases!'