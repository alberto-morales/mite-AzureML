from azureml.core.webservice import AksWebservice, Webservice
from azureml.core.model import Model
from azureml.core.compute import AksCompute, ComputeTarget
from azuremite.workspace import get_workspace

def model_deploy():
    ws = get_workspace()
    aks_target = AksCompute(ws,"myaks")
    # If deploying to a cluster configured for dev/test, ensure that it was created with enough
    # cores and memory to handle this deployment configuration. Note that memory is also used by
    # things such as dependencies and AML components.
    deployment_config = AksWebservice.deploy_configuration(cpu_cores = 1, memory_gb = 1)
    service = Model.deploy(ws, "myservice", [model], inference_config, deployment_config, aks_target)
    service.wait_for_deployment(show_output = True)
    print(service.state)
    print(service.get_logs())

    # Set configuration and service name
    prod_webservice_name = "worst-model-prod"
    prod_webservice_deployment_config = AksWebservice.deploy_configuration()

    # Deploy from image
    prod_webservice = Webservice.deploy_from_image(workspace=ws,
                                                   name=prod_webservice_name,
                                                   image=model_image,
                                                   deployment_config=prod_webservice_deployment_config,
                                                   deployment_target=aks_target)

if __name__ == '__main__':
    model_deploy()
    print("ok")