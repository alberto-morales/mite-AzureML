from azureml.core.webservice import AciWebservice, Webservice
from azuremite.workspace import get_workspace
from azuremite.image import get_image
from azuremite.configuration import LOCATION, MODEL_NAME

def deploy_image():
  ws = get_workspace() 
  azure_image = get_image()
  aci_config = AciWebservice.deploy_configuration(cpu_cores=1, 
                                                  memory_gb=1, 
                                                  tags={'method' : 'sklearn'}, 
                                                  description='Worst model',
                                                  location=LOCATION)
  webservice = Webservice.deploy_from_image(image=azure_image,
                                           workspace=ws,
                                           name=MODEL_NAME,
                                           deployment_config=aci_config)
  webservice.wait_for_deployment(show_output=True)
 
if __name__ == '__main__':
    deploy_image()
    print("ok")
