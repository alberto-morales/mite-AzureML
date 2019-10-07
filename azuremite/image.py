import mlflow.azureml
from azureml.core import Image
from azuremite.model2 import get_model_uri
from azuremite.model2 import get_experiment
from azuremite.workspace import get_workspace
from azuremite.configuration import IMAGE_NAME

def get_image():
    ws = get_workspace()
    container_image_from_name = Image(ws, name=IMAGE_NAME)
    return container_image_from_name

def build_image():
    ws = get_workspace() 
    m_uri = get_model_uri()
    azure_image, azure_model = mlflow.azureml.build_image(model_uri=m_uri,
                                                          workspace=ws,
                                                          model_name='worst-model',
                                                          image_name=IMAGE_NAME,
                                                          synchronous=True)

if __name__ == '__main__':
    build_image()
    print("ok")
    #azure_image = get_image()
    #print(azure_image.name)
