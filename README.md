# DevSecOps Logstash & Kubernetes Simulation 🛡️🚀

## Overview 📚
This repository showcases a **SOC Analyst simulation project** using **Logstash**, **Docker**, and **Kubernetes**.  
It demonstrates how logs can be collected, processed, and monitored in a containerized environment, highlighting automation and security practices. Perfect for building a **Cybersecurity portfolio**! 🔐💻

## Features ✨
- Automated deployment of **Logstash** on **AWS** using **Terraform** and **Ansible** ⚙️  
- Containerized environment using **Docker** 🐳  
- Orchestrated container management with **Kubernetes** ☸️  
- Collects logs from multiple sources and simulates real-world scenarios 📝  
- Demonstrates **SOC monitoring & alerting workflows** 🚨  

## Project Structure 📂
soc-simulation/
├─ docker-compose.yml # Docker Compose configuration
├─ generate_logs.py # Script to generate sample logs 📝
├─ logs/ # Sample log files 📄
├─ logstash/ # Logstash configuration 🔧
└─ soc-soc-sim/ # Submodule simulation (optional) 🔹

markdown
Copy code

## Learning Objectives 🎯
- Understand **DevSecOps pipelines** and automation  
- Learn **Infrastructure as Code (IaC)** using Terraform & Ansible  
- Hands-on experience with **Docker containers** and **Kubernetes orchestration**  
- Gain skills relevant to **SOC Analyst** roles: log monitoring, parsing, and alert simulation 🛡️  

## How to Run 🏃‍♀️
1. Ensure **Docker** and **Kubernetes** are installed and running 🐳☸️  
2. Clone the repository:  
```bash
git clone https://github.com/Sindhu-Purushothama/Devsecops-logstack-k8s.git
cd Devsecops-logstack-k8s
Start the environment:

bash
Copy code
docker-compose up -d
Generate sample logs:

bash
Copy code
python3 generate_logs.py
Observe log ingestion and monitoring in Logstash and container outputs 📊

Skills Highlighted 🏆
SIEM & Monitoring: Logstash, Docker, Kubernetes

Automation: Terraform, Ansible

Cloud & Infrastructure: AWS EC2, Kubernetes orchestration

SOC Analyst: Threat detection simulation, log collection, alerting 🚨

Portfolio Link 🔗 https://github.com/Sindhu-Purushothama
