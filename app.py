#app.py is the entry & exit point of the app (Application Layer)
#This 3-file split is called MVC (Model View Controller) Pattern
from flask import Flask #import flask
from models import *
app = Flask(__name__) #create an app instance

@app.route("/") #at the end point /
def hello(): #call method hello
        return "Hello World!" #which returns "hello world"

if __name__ == "__main__": #when app.py (main method called)
    #Call Schema to create table before app run starts
    Schema()
    app.run(debug = True) #run the flask app
    #debug=True turns on debug mode for the server
    #server will restart as new code added to Flask app