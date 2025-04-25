from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# database config
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///myDB.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # to supress warnings
db = SQLAlchemy(app)

# declare the Book model
class Book(db.Model):
  id = db.Column(db.Integer, primary_key = True) # primary key column, automatically generated IDs
  title = db.Column(db.String(80), index = True, unique = True) # book title
  author_name = db.Column(db.String(50), index = True, unique = False) # author first name
  author_surname = db.Column(db.String(80), index = True, unique = False) # author surname
  month = db.Column(db.String(20), index = True, unique = False) # the month of book suggestion
  year = db.Column(db.Integer, index = True, unique = False) # the year of book suggestion
  
  # printout for Book objects
  def __repr__(self):
    return "{} in: {},{}".format(self.title, self.month,self.year)

# declare the Reader model
class Reader(db.Model):
  id = db.Column(db.Integer, primary_key = True)
  name = db.Column(db.String(50), index = True, unique = False)
  surname = db.Column(db.String(80), index = True, unique = False)
  email = db.Column(db.String(120), index = True, unique = True)

  # printout for Reader objects
  def __repr__(self):
    return "Reader: {}".format(self.email)

# index route
@app.route('/')
def index():
  return 'Congrats! This Flask application now supports databases!'