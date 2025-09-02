# Devsecops-logstack-k8s
“Simulating a SOC environment with Logstash, Elasticsearch, Kibana, Docker, and Kubernetes for log monitoring and alerting.”

# SOC Log Monitoring with Docker & Kubernetes

This project simulates a Security Operations Center (SOC) environment using Docker and Kubernetes. It demonstrates how logs can be generated, collected, analyzed, and visualized in a scalable and automated setup, relevant for security monitoring and threat detection.

## Features

- **Log Generation:** Simulated server and application logs using Python scripts.
- **Log Collection:** Collected and processed logs using Logstash.
- **Storage:** Centralized logs in Elasticsearch for search and analysis.
- **Visualization:** Real-time dashboards with Kibana.
- **Containerization:** Each component runs in Docker containers for isolation.
- **Orchestration:** Managed multiple containers using Kubernetes (Deployments & Services).
- **Automation:** Scripts provided for Docker and Kubernetes deployment.
- **Scalability:** Logstash containers can scale horizontally to handle increased log volumes.

## Architecture

Log Generators --> Logstash (Docker/K8s) --> Elasticsearch --> Kibana Dashboard

markdown
Copy code

- Kubernetes handles container orchestration, scaling, and auto-healing.
- Terraform/Ansible can be optionally integrated for Infrastructure as Code (IaC).

## Prerequisites

- Docker & Docker Compose
- Kubernetes (Minikube or Kind)
- Python 3.x
- Git

## How to Run

### Using Docker (local test)
```bash
./scripts/deploy_docker.sh
Using Kubernetes (Minikube/Kind)
bash
Copy code
./scripts/deploy_k8s.sh
Access Kibana dashboard at http://localhost:5601 to view logs.

Skills Demonstrated
SOC Analyst: Log monitoring, parsing, IOC detection, incident simulation

DevOps/DevSecOps: Docker, Kubernetes, CI/CD basics

Cloud & Automation: Infrastructure-as-Code concepts, automation with scripts

Project Structure
perl
Copy code
multi-container-soc-logs/
├── docker/          # Dockerfiles for Logstash, Elasticsearch, Kibana
├── k8s/             # Kubernetes manifests (Deployments & Services)
├── log-generators/  # Python scripts to simulate logs
├── scripts/         # Deployment scripts
├── diagrams/        # Architecture diagrams
└── README.md
Author
Sindhu Purushothama
SOC Analyst | CompTIA Security+ | SIEM (Wazuh, Splunk) | Azure & Cloud Security
Location: Offenbach, Germany
Email: sindhu.seu16@gmail.com
LinkedIn: https://www.linkedin.com/in/sindhu-purushothama/
