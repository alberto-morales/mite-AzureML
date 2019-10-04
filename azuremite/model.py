from azureml.core.model import Model
from azuremite.workspace import get_workspace

def model_register():
    ws = get_workspace()
    model = Model.register(workspace=ws, model_path="../artifacts/worst.pickle", model_name="worst-model")
    return model

def get_model_path():
    ws = get_workspace()
    model_path = Model.get_model_path('worst-model', _workspace=ws)
    return model_path

if __name__ == '__main__':
    model_path = get_model_path()
    print(model_path)
    print("ok")