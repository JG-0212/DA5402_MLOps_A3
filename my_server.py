import os
from fastapi import FastAPI, Body
import uvicorn
from pydantic import BaseModel
import numpy as np
import pickle
from dense_neural_class import *
import base64
from PIL import Image
import io
import configparser

def get_port():
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config['server']['port_exposed']

def load_model(filename):
    # Gets the current directory where the script is being executed
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # Constructs the full path of the .pkl file
    filepath = os.path.join(current_dir, filename + '.pkl')
    with open(filepath, 'rb') as file:
        model_loaded = pickle.load(file)
    
    return model_loaded


# create the webapp.
app = FastAPI(title="REST API Server for predicting hand drawn digit")

model = load_model('model')

class Data(BaseModel):
    b64_img:str

@app.post("/predict")
async def predict(data:Data):
    decoded_img = base64.b64decode(data.b64_img)
    pil_img = Image.open(io.BytesIO(decoded_img))
    arr_img = np.asarray(pil_img)
    img = arr_img.reshape(1,-1) / 255.0
    result = model.predict(img)[0]
    return int(result)

# Run from command line: uvicorn apiWithBody:app --port 7000 --host 0.0.0.0
# or invoke the code below.
uvicorn.run(app,port = 7000)#,host = '0.0.0.0',port =int(get_port()))