import os
from flask import Flask , request 
import pickle


app = Flask(__name__)


#------------------------FUNCTIONS---------------------------------------------
def get_the_prediction():
    status = "None"
    #Loading the Model
    with open('RNmodel_pickle', 'rb') as f:
        model = pickle.load(f)
        status = "Model Loaded"

    return status

# ------------------ API Endpoints ----------------------------------------------
@app.route("/")
def testApp():
    return "App is Working"



@app.route("/test" , methods=['POST' 'GET'])
def test_app():
    if request.method=="POST":
        
        age = request.form['age']
        education = request.form['Education']
        gender = request.form['gender']
        return "Success - "+age+" "+gender+" "+education

    return "ERR"

@app.route("/predict")
def predict_class():

    return get_the_prediction()


if __name__ == "__main__":
    app.run()