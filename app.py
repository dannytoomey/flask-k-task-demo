from flask import Flask 
from flask import render_template, request, jsonify, Response
from flask_cache_buster import CacheBuster
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

#if resources have been updated, use the most recent resources instead of old cached resources
cache_buster.register_cache_buster(app)

#set a route for the load screen
@app.route("/")
def home():
    #load the file 'home.html' from the templates folder
    #to render a template outside of the templates folder, specifcy a different folder in 
    #app = Flask(... , template_folder=<your new folder>, ...)
    return render_template("home.html")

if __name__ == "__main__":
    from os import environ
    app.run(debug=False, port=environ.get("PORT", 33507), processes=2)

