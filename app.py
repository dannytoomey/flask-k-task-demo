from flask import Flask 
from flask import render_template, request, jsonify

app = Flask(__name__, template_folder='./templates', static_folder='./static')

@app.route("/")
def home():
    return render_template("home.html")

if __name__ == "__main__":
    from os import environ
    app.run(debug=False, port=environ.get("PORT", 33507), processes=2)