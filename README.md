DevSecOps-Logstash-K8s 🚀

A simple simulation project to demonstrate a SOC analyst workflow using Docker, Logstash, and optionally Kubernetes. This project generates logs, processes them, and sends them to a central system for monitoring.

What it does

Reads log files from the logs/ folder. 📄

Organizes and processes the log data using Logstash. 🔧

Sends the processed logs to Elasticsearch or displays them in the console for analysis. 📊

Project Structure

soc-simulation/
│
├── README.md                  # Project overview with setup instructions
├── docker-compose.yml         # To run your services
├── generate_logs.py           # Script to generate log data
│
├── logs/                      # Sample log files
│   ├── sample1.log
│   └── sample2.log
│
├── logstash/                  # Logstash configuration
│   └── logstash.conf
│
└── k8s/ (optional)            # Kubernetes manifests if you add them later
    ├── deployment.yaml
    └── service.yaml
How to run

Make sure Docker is running 🐳

Run the services: docker-compose up -d

Check that Logstash is processing logs and Elasticsearch (if used) is receiving them. ✅

Notes: * This is a simulation project for SOC analyst practice.
       * Kubernetes folder is optional and can be added later for orchestration.
