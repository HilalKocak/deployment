import os
import uvicorn
from fastapi import FastAPI
import numpy as np
import joblib
from pydantic.main import BaseModel

app=FastAPI(title= "MY ML App ")


@app.get('/')
def home():
    return "API is working as expected"

class MyData(BaseModel):
    X: int
@app.post('/predict')
def predict(data: MyData):
    my_model=joylib.load('app/my_model')
    X=np.array(data.X).reshape(-1,1)
    return str(my_model.predict(X))


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
    