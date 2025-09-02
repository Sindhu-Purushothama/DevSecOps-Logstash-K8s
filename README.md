DevSecOps Logstash & Kubernetes Simulation
Overview

This project demonstrates a SOC-focused simulation using Logstash, Docker, and Kubernetes. It is designed to showcase threat detection, log collection, and automation skills relevant for a Security Operations Center (SOC) Analyst role.

Features

Logstash Deployment Automation:

Deploys Logstash on AWS (or local Docker) using Terraform and Ansible.

Automates log ingestion from multiple sources for analysis.

Docker Containers:

Simulates multiple isolated environments (containers) for testing logs and events.

Each container acts as an independent instance, similar to real servers in production.

Kubernetes Simulation (Optional):

Demonstrates orchestration and scaling of multiple containerized environments.

SOC Skills Highlighted:

Log collection and monitoring

Incident detection and triage

Infrastructure-as-Code (Terraform & Ansible)

Automation of repetitive tasks

Understanding of cloud environments and container orchestration

How to Run

Clone the repository:

git clone https://github.com/Sindhu-Purushothama/Devsecops-logstack-k8s.git
cd Devsecops-logstack-k8s


Start Docker:
Ensure Docker is running on your system.

Run the simulation:

docker-compose up -d


Verify running containers:

docker-compose ps


Check logs inside the logs/ folder for sample events.

Skills Demonstrated

Security monitoring & analysis (SOC)

CI/CD pipeline understanding

Infrastructure automation (Terraform & Ansible)

Containerization (Docker) and orchestration concepts (Kubernetes)

Cloud security basics

Notes

This project is safe to run locally; no sensitive data is included.

Can be extended to include more complex SOC workflows for deeper demonstrations.
