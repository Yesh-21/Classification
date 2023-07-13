import json
import jsonpickle
import pickle

from flask import Flask,request,app,jsonify,url_for,render_template
import numpy as np
import pandas as pd

app=Flask(__name__)

## Load the model
model=pickle.load(open('trained_pipeline_BRF(2).pkl','rb'))
data = ['0', 'No', 'No', '41', 'Yes', 'No', 'No', 'No', 'No', 'No', 'No',
        'No', 'Month-to-month', 'Yes', 'Bank transfer (automatic)',
        '25.25', '996.45']
data = np.array(data).reshape(1,-1)
output = model.predict(data)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict_api',methods=['POST'])
def predict_api():
    data=request.json['data']
    data = np.array(list(data.values())).reshape(1,-1)
    output = model.predict(data)
    print(output[0])
    return jsonify(int(output[0]))

@app.route('/predict',methods=['POST'])
def predict():
    data=[request.form.values()]
    data = np.array(list(data.values())).reshape(1,-1)
    output = model.predict(data)
    print(output[0])
    return render_template("home.html",prediction_text="The House price prediction is {}".format(jsonify(int(output[0]))))

if __name__=="__main__":
    app.run(debug=True)