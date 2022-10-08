from flask import Flask, render_template, request, flash
from flask_sqlalchemy import SQLAlchemy
from send_mail import send_mail

app = Flask(__name__)

ENV = 'dev'

if ENV == 'dev':
  app.debug = True
  app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password@localhost/dominos'
else:
  app.debug = False
  app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://<heroku_url>'



app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Feedback(db.Model):
  __tablename__ = 'feedback'
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(200), unique=True)
  branch = db.Column(db.String(200))
  rating = db.Column(db.Integer)
  comments = db.Column(db.Text())

  def __init__(self, name, branch, rating, comments):
    self.name = name
    self.branch = branch
    self.rating = rating
    self.comments = comments
    

@app.route("/")
def index():
  return render_template('index.html')

@app.route("/submit", methods = ['POST'])
def submit():
  if request.method == 'POST':
    name = request.form.get('name')
    branch = request.form.get('branch')
    rating = request.form.get('rating')
    comments = request.form.get('comments')
    # print(name, branch, rating, comments)
    if name == '' or branch == '':
      return render_template('index.html', message='Please enter required fields!')

    # if name == '' or branch == '':
    #   flash('Please enter required fields', category='error')

    if db.session.query(Feedback).filter(Feedback.name == name).count() == 0:
      data = Feedback(name, branch, rating, comments)
      db.session.add(data)
      db.session.commit()
      send_mail(name, branch, rating, comments)
      return render_template('success.html')

    return render_template('index.html', message='You have already submitted feedback')


if __name__ == '__main__':
  app.run()
