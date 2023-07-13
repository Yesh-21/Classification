# -*- coding: utf-8 -*-
"""
"""

# 1. Library imports
import uvicorn
from fastapi import FastAPI
from Churn import Churn
import numpy as np
import pickle
import pandas as pd
# 2. Create the app object
app = FastAPI()
model=pickle.load(open('trained_pipeline_BRF(2).pkl','rb'))


# 3. Index route, opens automatically on http://127.0.0.1:8000
@app.get('/')
def index():
    return {'message': 'Hello, World'}

# 4. Route with a single parameter, returns the parameter within a message
#    Located at: http://127.0.0.1:8000/AnyNameHere
@app.get('/{name}')
def get_name(name: str):
    return {'Welcome': f'{name}'}

# 3. Expose the prediction functionality, make a prediction from the passed
#    JSON data and return the predicted Bank Note with the confidence
@app.post('/predict')
def predict_banknote(data:Churn):
    data = data.dict()
    data = np.array(list(data.values())).reshape(1,-1)
    output = model.predict(data)
    print(output[0])
    #return jsonify(int(output[0]))

    if ( output[0] == 0 ):
        prediction="Not gonna churn"
    else:
        prediction="Gonna churn"
    return {
        'prediction': prediction
    }


# 5. Run the API with uvicorn
#    Will run on http://127.0.0.1:8000
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
    
#uvicorn app:app --reload