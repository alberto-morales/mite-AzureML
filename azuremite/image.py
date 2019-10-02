from azureml.core.compute import AksCompute, ComputeTarget
from azuremite.workspace import get_workspace

def attach_cluster():
    # Set the resource group that contains the AKS cluster and the cluster name
    resource_group = 'MLLab-resource-group'
    cluster_name = 'MLLab-K8s'

    # Attach the cluster to your workgroup. If the cluster has less than 12 virtual CPUs, use the following instead:
    attach_config = AksCompute.attach_configuration(resource_group = resource_group,
                                                    cluster_name = cluster_name,
                                                    cluster_purpose = AksCompute.ClusterPurpose.DEV_TEST)
    ws = get_workspace()
    aks_target = ComputeTarget.attach(ws, 'myaks', attach_config)
    return aks_target

if __name__ == '__main__':
    aks_target  = attach_cluster()
    print("ok")