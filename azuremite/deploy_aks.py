from azuremite.workspace import get_workspace
from azuremite.image import get_image
from azuremite.cluster import get_cluster

from azureml.core.webservice import Webservice, AksWebservice
from azureml.core.image import ContainerImage
def get_service():
  ws = get_workspace() 
  services = Webservice.list(workspace = ws, compute_type='AKS')
  return services[0]

def deploy_image():
  ws = get_workspace() 
  azure_image = get_image()
 
  # Use the default configuration (can also provide parameters to customize)
  #prov_config = AksCompute.provisioning_configuration()

  # Set the web service configuration (using default here with app insights)
  aks_config = AksWebservice.deploy_configuration(enable_app_insights=True)

  # Unique service name
  service_name ='myaks'

  aks_target = get_cluster()

  # Webservice creation using single command
  aks_service = Webservice.deploy_from_image( workspace=ws, 
                                              name=service_name,
                                              deployment_config = aks_config,
                                              image = azure_image,
                                              deployment_target = aks_target)

  aks_service.wait_for_deployment(show_output=True)

if __name__ == '__main__':
    #deploy_image()
    print(get_service().scoring_uri)
    print("ok")
