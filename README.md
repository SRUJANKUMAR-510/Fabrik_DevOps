# Fabrik_DevOps : Containerization and Deployment Automation for three.js Editor Application

[![Tools](https://skillicons.dev/icons?i=docker,nginx,github,html,py,vscode,ubuntu,linux,apple)](https://skillicons.dev)

## 📝 Overview
This project is a containerized version of the [three.js editor application](https://threejs.org/editor/), which is a web-based tool for creating and editing 3D scenes using the three.js library. The application is served using an Nginx web server running inside a Docker container. The project also includes deployment automation scripts for building the Docker image and deploying the application to a simulated client environment.

This repository contains the Dockerfile for containerizing the three.js editor application, along with deployment automation scripts and documentation for building the Docker image and deploying the application to a simulated client environment.

## Application Containerization
## 🌱 Getting Started

### Clone the Repository
```bash
git clone https://github.com/SRUJANKUMAR-510/Fabrik_DevOps

```
### Once the cloning process is complete, navigate to the project directory
```bash
cd Fabrik_DevOps

```
## 🚀 Configuring the Target Environment

The Dockerfile in the repository is configured to run the three.js editor application on a Nginx server. The application is served on port 8080 by default. If you wish to change the port, you can do so by modifying the Dockerfile.

### 👁️ Check the Docker verion installed on your machine
```bash
docker --version
```
If the docker is not installed on your system, the automation script will install the docker on your system.

## 🛫 Running the Deployment Automation Script
The deployment automation script will take care of installing the necessary dependencies, building the Docker image, and running the container. To run the script, execute the following command:

1.Open the terminal or command prompt.

2.Navigate to the project directory where the deployment automation script is located.

3.Run the following command to execute the deployment automation script:

```bash
python deployment.py

```
The `deployment.py` script will This script performs the following tasks:

Checks if Docker is installed on the target machine and installs it.

Pulls the Docker image from the docker hub/local registry for the three.js editor application.

## Step 1: Install Docker Registry
Install Docker Registry: If you haven't already, install Docker Registry using the following command:
```bash
docker run -d -p 5000:5000 --restart=always --name registry registry:2
```

This command pulls the Docker Registry image from Docker Hub and runs it as a container named "registry" on port 5000.

## Step 2: Tag and Push Docker Image

Tag Docker Image: Tag your Docker image with the address of your local registry. Replace your-image with the name of your Docker image
```bash
docker tag your-image localhost:5000/your-image
```

Push Docker Image: Push the tagged Docker image to your local registry:
```bash
docker push localhost:5000/your-image

```
This command pushes the Docker image to your local registry running on port 5000.

## Step 3: Validate Pushed Image
List Images in Registry: List the images stored in your local registry:
```bash
curl -X GET http://localhost:5000/v2/_catalog
```

This command retrieves a list of repositories stored in the local registry.

Inspect Image Tags: Inspect the tags of a specific image in the registry. Replace your-image with the name of your Docker image.
```bash
curl -X GET http://localhost:5000/v2/your-image/tags/list
```

This command retrieves a list of tags associated with the specified Docker image.

## Step 4: Pull Docker Image
Pull Docker Image: Pull the Docker image from your local registry. Replace your-image with the name of your Docker image.
```bash
docker pull localhost:5000/your-image
```

This command pulls the Docker image from your local registry to your local machine.

## Step 5: Verify Pulled Image
List Pulled Images: List the Docker images on your local machine to verify the pulled image:

```bash
docker images
REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
your-image          latest              7698f282e524        2 minutes ago       1.2GB

```
If everything is set up correctly, you should see the following output:

This command displays a list of Docker images stored locally on your machine.

Replace your-image with the name of your pulled Docker image.

This is will complete the docker registry setup on the target environment. Now you can use this docker registry for sharing the docker images.

Starts the Docker container with the appropriate configuration. The port mapping ensures that the web interface of the three.js editor application is accessible on the host machine.

Creates a container using the pulled image with the appropriate configuration.

Starts the created container.

Exposes port 80 of the container to port 8080 of the host machine.

Prints out the URL that can be used to access the three.js editor application.

Verifies that the application is running and accessible.

Builds a static version of the Three.js editor application.

Copies the built files into the Docker container.

Restarts the Docker container to reflect the changes.

Note: The above steps are performed sequentially by the deployment automation script. The script will output the URL that can be used to access the three.js editor application once the deployment process is complete.

You should see output similar to this:

```bash

+-------------------+-------------+------+---------+----------+-----------------------+
|      Name         |   Images   | CPU  | Memory  |  Ports   |      URL               |
+-------------------+-------------+------+---------+----------+-----------------------+
| threejs-container | threejs:1  | 0.1  |  128MB  | 8080:80  | http://localhost:8080  |
+-------------------+-------------+------+---------+----------+-----------------------+
```

4. Open a web browser and navigate to the URL http://localhost:8080 to access the three.js editor application.
Copy the provided URL into your web browser to access the three.js editor application. You may need to wait a few moments for the application to load, depending on your system's performance.
This means your local installation of the Three.js editor application is up and running successfully.

Now you can open your web browser and navigate to the specified URL to access the three.js editor application.
Copy the provided URL into your web browser to access the three.js editor application.












