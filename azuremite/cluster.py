from azureml.core.compute import AksCompute, ComputeTarget
from azuremite.workspace import get_workspace

def create_cluster():
    ws = get_workspace()
    # Use the default configuration (can also provide parameters to customize)
    prov_config = AksCompute.provisioning_configuration()
    aks_name = 'MLLabK8s'

    # Create the cluster
    aks_target = ComputeTarget.create(workspace=ws,
                                      name=aks_name,
                                      provisioning_configuration=prov_config)

    aks_target.wait_for_completion(show_output=True)

    print(aks_target.provisioning_state)
    print(aks_target.provisioning_errors)

    return aks_target

def attach_cluster():
    # Set the resource group that contains the AKS cluster and the cluster name
    resource_group = 'MLLab-resource-group'
    cluster_name = 'MLLabK8s'

    # Attach the cluster to your workgroup. If the cluster has less than 12 virtual CPUs, use the following instead:
    attach_config = AksCompute.attach_configuration(resource_group = resource_group,
                                                    cluster_name = cluster_name,
                                                    cluster_purpose = AksCompute.ClusterPurpose.DEV_TEST)
    ws = get_workspace()
    aks_target = ComputeTarget.attach(ws, 'myaks', attach_config) ## myaks ==> The name to associate with the Compute object
    return aks_target

if __name__ == '__main__':
    aks_target  = attach_cluster()
    # aks_target = create_cluster()
    print("ok")