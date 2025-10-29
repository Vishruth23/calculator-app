# Scientific Calculator - DevOps Pipeline Project

This project demonstrates a complete CI/CD DevOps pipeline using a simple Scientific Calculator application built with Python.  
The pipeline automates testing, Dockerization, and deployment using Jenkins and Ansible.

---

## Features
- Basic scientific operations: square root, factorial, logarithm, power  
- Unit testing with pytest  
- Containerized using Docker  
- Automated CI/CD pipeline with Jenkins  
- Deployment managed by Ansible

---

## Tools Used
- Python – Application development  
- Git & GitHub – Source code management  
- Pytest – Unit testing framework  
- Docker – Containerization  
- Jenkins – Continuous Integration & Delivery  
- Ansible – Automated deployment

---

## Pipeline Overview
1. Code pushed to GitHub triggers Jenkins.  
2. Jenkins runs unit tests using Pytest.  
3. Docker image is built and pushed to Docker Hub.  
4. Ansible pulls the latest image and deploys the container.

Push to verify if pipeline is working as expected-3.
