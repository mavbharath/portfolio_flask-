# Portfolio Website (Flask + Docker)

A personal portfolio site for **Bharath H**, built with Flask and Docker.

## 🚀 Run with Docker

docker build -t portfolio-flask .
docker run -d -p 5000:5000 --name portfolio portfolio-flask

AI Prompts Used:
1. You are a release manager AI. Given the Git commit message, Docker image tag, and Helm values update, write professional release notes in under 150 words. Include the version, key changes, and an emoji-based summary.

2. You are a Kubernetes cost-optimizer AI. Given current CPU/memory usage metrics, propose updated values.yaml settings for replicas, requests, and limits to balance cost and performance.

3. You are a DevOps SRE AI. Given kubectl describe pod and kubectl logs output, generate a status report with 3 sections:
1. Current health summary
2. Possible issues
3. Recommended actions
