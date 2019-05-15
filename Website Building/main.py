##################################################################################
# Creator     : Gaurav Roy
# Date        : 15 May 2019
# Description : The code helps with a building a website using Flask. 
#               It is deployed on a python virtual environment first.
#               It also helps in deploying it in a live server (Heroku).
##################################################################################

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/about/')
def about():
    return render_template("about.html")

if __name__=="__main__":
    app.run(debug=True)