from azuremite.configuration import WORKSPACE_NAME, SUBSCRIPTION_ID, RESOURCE_GROUP

from azureml.core import Workspace

def get_workspace():
    """
    MLLab Área de trabajo del servicio Machine Learning
    a21d8af7-720a-451d-9010-9defcff47587 Suscription id
    mllab7849892444 Microsoft.Insights/components
    mllab8506144354 Microsoft.KeyVault/vaults
    mllab6951918960 Microsoft.Storage/storageAccounts
    MLLab Microsoft.MachineLearningServices/workspace
    MLLab-resource-group Resource group
    MLLabK8s Nombre cluster kubernetes
    myaks kubernetes service
    mllabed19e1e6 Container Registry
              (MLLab-K8s es id de recurso, nombre del proceso myaks)
    """
    ws = Workspace.get(name=WORKSPACE_NAME, subscription_id=SUBSCRIPTION_ID, resource_group=RESOURCE_GROUP)
    return ws

if __name__ == '__main__':
    workspace = get_workspace()
    print("ok")