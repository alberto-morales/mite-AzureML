"""
from azureml.core.runconfig import RunConfiguration
from azureml.core.compute import AmlCompute
list_vms = AmlCompute.supported_vmsizes(workspace=ws)

compute_config = RunConfiguration()
compute_config.target = "amlcompute"
compute_config.amlcompute.vm_size = "STANDARD_D1_V2"


---------------

from azureml.core.conda_dependencies import CondaDependencies

dependencies = CondaDependencies()
dependencies.add_pip_package("scikit-learn")
dependencies.add_pip_package("numpy==1.15.4")
compute_config.environment.python.conda_dependencies = dependencies

---------------

from azureml.core.experiment import Experiment
from azureml.core import ScriptRunConfig

script_run_config = ScriptRunConfig(source_directory=os.getcwd(), script="train.py", run_config=compute_config)
experiment = Experiment(workspace=ws, name="compute_target_test")
run = experiment.submit(config=script_run_config)
run.wait_for_completion(show_output=True)

"""

