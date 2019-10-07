from azureml.core.compute import AksCompute, ComputeTarget
from azuremite.workspace import get_workspace
from azuremite.configuration import AKS_NAME, AKS_CLUSTER_NAME, RESOURCE_GROUP

def get_cluster():
    ws = get_workspace()
    aks_name = AKS_NAME
    cts = ws.compute_targets
    if aks_name in cts and cts[aks_name].type == 'AKS':
       print('Found existing AKS cluster, will use it!')
       aks_target = cts[aks_name]
       return aks_target
    else:
       print('AKS cluster not found, sorry')
       return None

def create_cluster():
    ws = get_workspace()
    # Use the default configuration (can also provide parameters to customize)
    prov_config = AksCompute.provisioning_configuration()
    aks_name = AKS_CLUSTER_NAME

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
    resource_group = RESOURCE_GROUP
    cluster_name = AKS_CLUSTER_NAME

    # Attach the cluster to your workgroup. If the cluster has less than 12 virtual CPUs, use the following instead:
    attach_config = AksCompute.attach_configuration(resource_group = resource_group,
                                                    cluster_name = cluster_name,
                                                    cluster_purpose = AksCompute.ClusterPurpose.DEV_TEST)
    ws = get_workspace()
    aks_target = ComputeTarget.attach(ws, AKS_NAME, attach_config)
    return aks_target

if __name__ == '__main__':
    aks_target = get_cluster()
    print(aks_target)
    #aks_target  = attach_cluster()
    # aks_target = create_cluster()
    print("ok")
