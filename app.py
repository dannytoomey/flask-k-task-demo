from flask import Flask
from flask import render_template, request, jsonify, Response
from flask_cache_buster import CacheBuster
#from flask_sqlalchemy import SQLAlchemy
import os

config = {
     'extensions': ['.js', '.css', '.csv'],
     'hash_size': 10
}
#configure an extension used to bust caches
cache_buster = CacheBuster(config=config)

#create a flask application and tell it where the 'templates' and 'static' folders are
#flask uses a particular project structure that expects the following:
# app.py 
#   |--static 
#       |-- resources to be used by templates
#   |--templates 
#       |-- html templates to rendered by the flask app
app = Flask(__name__, template_folder='./templates', static_folder='./static')

'''
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///ktask_demo'

db = SQLAlchemy(app)

class Exp_Data(db.Model):
   id = db.Column('participant_id', db.Integer, primary_key = True)
   name = db.Column(db.String(100))
   trial = db.Column(db.Integer)  
   trial_rt = db.Column(db.Integer)
   trial_acc = db.Column(db.Integer)

def __init__(self, name, trial, trial_rt,trial_acc):
    self.name = name
    self.trial = trial
    self.trial_rt = trial_rt
    self.trial_acc = trial_acc

'''

#if resources have been updated, use the most recent resources instead of old cached resources
cache_buster.register_cache_buster(app)

#set a route for the load screen
@app.route("/")
def home():
    #load the file 'home.html' from the templates folder
    #to render a template outside of the templates folder, specifcy a different folder in 
    #app = Flask(... , template_folder=<your new folder>, ...)
    return render_template("home.html")

'''
@app.route("/data", methods=['GET','POST'])
def store_data(request):
    if request.method == 'POST':
      if not request.form['name']:
         flash('Please enter your name', 'error')
      else:
         data = Exp_Data(request.form['name'], request.form['trial'],
            request.form['trial_rt'], request.form['trial_acc'])
         
         db.session.add(data)
         db.session.commit()
         
         flash('Record was successfully added')
         return redirect(url_for('home'))

'''

if __name__ == "__main__":
    from os import environ
    app.run(debug=False, port=environ.get("PORT", 33507), processes=2)

