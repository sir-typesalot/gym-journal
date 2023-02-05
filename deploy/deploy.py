"""
    Deploy the docker container to AWS lightsail.
"""
import os
import json
import re
import subprocess

def run_bash_script():
    """
    Run the bash script that handles the AWS commands.
    """
    try:
        subprocess.run(["./deploy/deploy.sh"], check=True)
        print("Built docker image and pushed to AWS")
    except subprocess.CalledProcessError:
        print("There was an error running the deploy bash file")

def update_container_version():
    """
    Method to handle updating the container version in the JSON file.
    """
    # TODO: May need to change this based on deployment process
    os.chdir("./deploy")
    with open('containers.json', 'r') as openfile:
        # Reading from json file
        json_object = json.load(openfile)

    version = json_object['flask']['image']
    temp = re.findall(r'\d+', version)
    version_num = int(temp[0])
    new_version = f"{version[0:-2]}{version_num+1}"
    json_object['flask']['image'] = new_version

    with open("containers.json", "w") as outfile:
        json.dump(json_object, outfile)
    
    print("Wrote new version to containers file")

def deploy_container():
    """
    Deploy the container to AWS
    """
    subprocess.run([
        "aws", "lightsail", "create-container-service-deployment",
        "--service-name", "exercise-api", "--containers", "file://containers.json",
        "--public-endpoint", "file://public-endpoint.json"
    ], check=True)
    print("Deployment successful")

if __name__ == '__main__':
    run_bash_script()
    update_container_version()
    deploy_container()
