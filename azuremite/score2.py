
from sklearn.externals import joblib

from azuremite.model2 import get_model

import pandas as pd

from azureml.core.model import Model

def init():
    global model
    # retrieve the model
    model = get_model()

def run(raw_data):
    df = pd.DataFrame(data)
    # make prediction
    y_hat = model.predict(df)
    # you can return any data type as long as it is JSON-serializable
    return y_hat.tolist()

if __name__ == '__main__':
    init()
    data = [[2000]]
    prediction = run(data)
    print(prediction)

