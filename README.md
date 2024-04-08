# Fabrik_DevOps : Containerization and Deployment Automation for three.js Editor Application

[![Tools](https://skillicons.dev/icons?i=docker,nginx,github,git,html,py,vscode,ubuntu,linux,bash)](https://skillicons.dev)

## 📝 Overview

This repository contains the Dockerfile for containerizing the three.js editor application, along with deployment automation scripts and documentation for building the Docker image and deploying the application  to a simulated client environment.

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
The `deployment.py` script will performs the following tasks:

-Checks if Docker is installed on the target machine and installs it.

Pulls the Docker image of the three.js editor application from the docker hub/local registry.

## How to Use Your Own Docker Registry

Docker Hub is the premier Image Repository with thousands of Official Images ready for use. It’s also just as easy to push your own images to the Docker Hub registry so that everyone can benefit from your Dockerized applications.

https://www.docker.com/blog/how-to-use-your-own-registry-2/


## 📂 Step 1: Set Up a Local Docker Registry (if not already done):Running the Distribution service

-If you haven’t already, set up a local Docker registry on your system. You can use the official Docker registry image.
-Run the following command to start a local registry container:

```bash
docker run -d -p 5000:5000 --name registry registry:2.7

```

The -d flag will run the container in detached mode. The -p flag publishes port 5000 on your local machine’s network. We also give our container a name using the --name flag.

## Step 2: Tag Your Existing Image for the Local Registry:

-we have our registry running locally, Assuming you’ve already built an image named “editor” (or any other name), tag it with the local registry hostname and port:

```bash
docker tag editor localhost:5000/editor

```
Replace “editor” with your actual image name.

## Step 3: Push the Tagged Image to the Local Registry:
-List Images in Registry: List the images stored in your local registry, Push the tagged image to your local registry:

```bash
docker push localhost:5000/editor

```
Replace “editor” with your actual image name. If you see an error like "Error response from daemon: Get https://localhost:5000/v2/: http: server gave HTTP response to HTTPS client", you may need to add the registry to the insecure registries list in the Docker daemon configuration file.

You should see output indicating that the image was successfully pushed to the local registry:

This command pushes the tagged Docker image to your local registry. You can now use this image as a base for other images or pull it from the registry to other machines.

## Step 4: Verify the Image in the Local Registry:
-Visit http://localhost:5000/v2/_catalog in your web browser or use the following command to verify that your image is listed:

```bash
curl http://localhost:5000/v2/_catalog

```

## Step 5: Verify Pulled Image
List Pulled Images: List the Docker images on your local machine to verify the pulled image:

```bash
docker images
REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
your-image          latest              7698f282e524        2 minutes ago       1.2GB

```
## Step 6 : Running the Deployment Automation Script
The deployment automation script will take care of installing the necessary dependencies, building the Docker image, and running the container. To run the script, execute the following command:

```bash
python deployment.py

```

-This is will complete the docker registry setup on the target environment. Now you can use this docker registry for sharing the docker images.

-Starts the Docker container with the appropriate configuration. The port mapping ensures that the web interface of the three.js editor application is accessible on the host machine.

-Creates a container using the pulled image with the appropriate configuration.

-Starts the created container.

-Exposes port 80 of the container to port 8080 of the host machine.

-Prints out the URL that can be used to access the three.js editor application.

-Verifies that the application is running and accessible.

-Builds a static version of the Three.js editor application.

-Copies the built files into the Docker container.

-Restarts the Docker container to reflect the changes.

-Note: The above steps are performed sequentially by the deployment automation script. The script will output the URL that can be used to access the three.js editor application once the deployment process is complete.

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












