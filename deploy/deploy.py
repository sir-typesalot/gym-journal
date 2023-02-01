import os
import json
import re
import subprocess

def run_bash_script():
    try:
        subprocess.run(["./deploy/deploy.sh"])
        print("Built docker image and pushed to AWS")
    except:
        print("There was an error running the deploy bash file")

def update_container_version():
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
    subprocess.run([
        "aws", "lightsail", "create-container-service-deployment",
        "--service-name", "exercise-api", "--containers", "file://containers.json",
        "--public-endpoint", "file://public-endpoint.json"
    ])
    print("Deployment successful")

if __name__ == '__main__':
    run_bash_script()
    update_container_version()
    deploy_container()
