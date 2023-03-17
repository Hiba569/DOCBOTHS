from flask import Flask, render_template, request, jsonify
from chat import get_response  #this method we put in a message and we get a response(string)

import speech_recognition as sr



app = Flask(__name__)

@app.get("/")
def index_get():
    return render_template("base.html")

@app.post("/predict")
def predict ():
    text = request.get_json().get("message")
    # TODO = check if text is valid
    response=get_response(text)
    message={"answer":response}
    return jsonify(message)

if __name__ =="__main__":
 app.run(debug=True) #for testing
 



    

    