import subprocess
import sys
import time

import requests  # Install using pip install requests


def check_docker_installed():
    try:
        subprocess.run(["docker", "--version"], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return True
    except subprocess.CalledProcessError:
        return False

def install_docker():
    print("Docker is not installed. Installing Docker...")
    try:
        subprocess.run(["sudo", "apt-get", "update"], check=True)
        subprocess.run(["sudo", "apt-get", "install", "-y", "docker.io"], check=True)
        print("Docker installed successfully.")
    except subprocess.CalledProcessError:
        print("Failed to install Docker. Exiting.")
        sys.exit(1)

def pull_docker_image(image_name):
    print("Pulling Docker image:", image_name)
    try:
        subprocess.run(["docker", "pull", image_name], check=True)
        print("Docker image pulled successfully.")
    except subprocess.CalledProcessError:
        print("Failed to pull Docker image. Exiting.")
        sys.exit(1)

def start_container(image_name, port_mapping):
    print("Starting Docker container...")
    try:
        subprocess.run(["docker", "run", "-d", "-p", port_mapping, "--name", "threejs_editor", image_name], check=True)
        print("Docker container started successfully.")
    except subprocess.CalledProcessError:
        print("Failed to start Docker container. Exiting.")
        sys.exit(1)

    # Wait for the container to start
    print("Waiting for Docker container to start...")
    container_started = False
    start_time = time.time()
    while time.time() - start_time < 60: # Wait for 60 seconds max
        try:
            subprocess.run(["docker", "inspect", "threejs_editor"], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            container_started = True
            break
        except subprocess.CalledProcessError:
            time.sleep(1)  # Wait for 1 second before checking again to avoid flooding Docker with requests

    if not container_started:
        print("Warning: Failed to start Docker container within the timeout. Proceeding anyway.")

def verify_application_running():
    print("Verifying application is running...")
    try:
        subprocess.run(["curl", "http://localhost:8080/build/three.module.js"], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print("Application is running and accessible.")
    except subprocess.CalledProcessError:
        print("Application is not running or accessible. Exiting.")
        sys.exit(1)

def check_docker_image_exists(image_name, tag):
    
    url = f"https://hub.docker.com/v2/repositories/{image_name}/tags/{tag}"
    
    response = requests.get(url)

    if response.status_code == 200:
        return True
    else:
        return False

if __name__ == "__main__":
    
    docker_image = "sktn123/editor_devops" # Image name on Docker Hub or local registry
    tag = "latest" # Image tag

    # Check if the Docker image exists on Docker Hub
    if not check_docker_image_exists(docker_image, tag):
        print("Docker image does not exist on Docker Hub. Pulling from local registry...")
        docker_image = "editor_devops:latest"  # Change to the local image name
    else:
        print("Docker image exists on Docker Hub.")

    # Specify port mappings and volume mounts if needed
    port_mappings = "8080:80"
    #volume_mounts = "D:\\SEM 7\\three.js-master\\three.js-master:/app"

    if not check_docker_installed():
        install_docker()

    pull_docker_image(docker_image)

    start_container(docker_image, port_mappings)

    # Wait for a few seconds to ensure the container is fully started before verifying accessibility
    time.sleep(10)

    verify_application_running()