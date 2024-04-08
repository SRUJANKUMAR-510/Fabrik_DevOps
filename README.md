# Fabrik_DevOps->Containerization and Deployment Automation for three.js Editor Application

[![My Skills](https://skillicons.dev/icons?i=js,html,css,wasm)](https://skillicons.dev)

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

### 🛫 Running the Deployment Automation Script
The deployment automation script will take care of installing the necessary dependencies, building the Docker image, and running the container. To run the script, execute the following command:

1.Open the terminal or command prompt.

2.Navigate to the project directory where the deployment automation script is located.

3.Run the following command to execute the deployment automation script:

```bash
python deployment.py
```
The `deployment.py` script will This script performs the following tasks:

Checks if Docker is installed on the target machine and installs it if necessary.

Pulls the Docker image for the three.js editor application.

Starts the Docker container with the appropriate configuration.

Verifies that the application is running and accessible.

Builds a static version of the Three.js editor application.

Copies the built files into the Docker container.

Restarts the Docker container to reflect the changes.

Once the deployment process is complete, you can access the three.js editor application by opening a web browser and navigating to the specified URL http://localhost:8080.











