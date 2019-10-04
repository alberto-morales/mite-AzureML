from azureml.core.conda_dependencies import CondaDependencies

def env_file_generate():
    myenv = CondaDependencies()
    myenv.add_conda_package("scikit-learn")
    with open("../temp/myenv.yml", "w") as f:
        f.write(myenv.serialize_to_string())

if __name__ == '__main__':
    env_file_generate()
    print("ok")
    with open("../temp/myenv.yml", "r") as f:
        print(f.read())