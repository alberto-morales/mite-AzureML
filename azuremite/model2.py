from azureml.core.model import Model
from azuremite.workspace import get_workspace
from azuremite.configuration import EXPERIMENT_NAME, MODEL_PATH
import mlflow.sklearn

def get_experiment():
    ws = get_workspace()
    experiment_name = EXPERIMENT_NAME
    exp = ws.experiments[experiment_name]
    return exp

def get_last_run_id():
    exp = get_experiment()
    runs = list(exp.get_runs())
    runId = runs[0].id
    print(f"last run ID={runId}")
    return runId

def get_model_uri(runId=get_last_run_id(), model_save_path=MODEL_PATH):
    ws = get_workspace()
    mlflow.set_tracking_uri(ws.get_mlflow_tracking_uri())
    model_uri = 'runs:/{}/{}'.format(runId, model_save_path)
    return model_uri

def get_model(runId=get_last_run_id(), model_save_path=MODEL_PATH):
    ws = get_workspace()
    mlflow.set_tracking_uri(ws.get_mlflow_tracking_uri())
    model_uri = get_model_uri(runId, model_save_path)
    model = mlflow.sklearn.load_model(model_uri)
    return model

if __name__ == '__main__':
    model = get_model()
    print(model)
    print("ok")