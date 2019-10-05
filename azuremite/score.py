
from sklearn.externals import joblib

from azuremite.model import get_model_path

import pandas as pd

from azureml.core.model import Model

def get_model():
    model_path = get_model_path()
    _model = joblib.load(model_path)
    return _model

def init():
    global model
    # retrieve the path to the model file using the model name
    # model_path = os.path.join(os.getenv('AZUREML_MODEL_DIR'), 'sklearn_mnist_model.pkl')
    model = get_model()

def run(raw_data):
    df = pd.DataFrame(data)
    jsonContent = pd.DataFrame.to_json(df, orient='split')
    print(f"invocaremos con {jsonContent}")
    # make prediction
    y_hat = model.predict(df)
    # you can return any data type as long as it is JSON-serializable
    return y_hat.tolist()

if __name__ == '__main__':
    init()
    data = [[2000]]
    prediction = run(data)
    print(prediction)

