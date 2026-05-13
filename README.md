# Python File & User API

[![Python](https://img.shields.io/badge/Python-3.13+-blue.svg)](https://www.python.org)
[![Flask](https://img.shields.io/badge/Flask-3.x-black.svg)](https://flask.palletsprojects.com)
[![Helm](https://img.shields.io/badge/Helm-3.x-0F1689.svg)](https://helm.sh)
[![Kubernetes](https://img.shields.io/badge/Kubernetes-Ready-326CE5.svg)](https://kubernetes.io)

A lightweight **Flask REST API** for file system browsing and user management, designed for Kubernetes deployment via Helm.

##  Features

- Browse and view files from configured server directories
- User CRUD operations with secure password hashing (bcrypt + pepper)
- Fully containerized and Kubernetes-native
- Helm chart for easy deployment and configuration
- Clean separation of configuration and secrets

## Quick Start

### Prerequisites

- Kubernetes cluster (Minikube, kind, EKS, etc.)
- Helm 3.x

### Installation

```bash
# Clone the repository
git clone https://github.com/mAGNETAFONAS/Python_API.git
cd Python_API

# Re-use Docker registry inside Minikube or any other kubernetes cluster
eval $(minikube docker-env)

# Build web app image using premade scripts
./scripts/build.sh python-api-web

# Install the Helm chart using premade scripts
./scripts/helm-upgrade.sh web-helm ./webchart ./webchart/values.yaml
```
### Usage

Application can be used by port forwarding:
```bash
kubectl port-forward deployment/web-helm 8000:8000
```
Application can be reached with localhost:8000

## Project structure
```bash
Python_API/
├── flask.main.py                 # Main Flask application
├── requirements.txt
├── config.yml
├── webchart/                     # Helm Chart (main deployment method)
│   ├── Chart.yaml
│   ├── values.yaml
│   ├── templates/
│   └── .helmignore
├── docker/
│   └── web/
│       └── Dockerfile
├── VERSION.md
├── files/                        # Example files directory
├── scripts/                      # Premade Bash scripts
└── templates/                    # HTML templates
```

## Configuration
All important settings are managed through webchart/values.yaml:

- Image repository and tag
- Resource requests & limits
- Database connection settings
- Persistence for files
- Probes (startup, liveness, readiness)

See webchart/values.yaml for all available options.

## API Endpoints
- GET / → Homepage
- GET /web/<directory> → Browse files
- GET /web/<directory>/<filename> → View file content
- User management endpoints

## Screenshots
![Main page](../../Pictures/Screenshot%20from%202026-05-13%2009-42-55.png)
![Database service](../../Pictures/Screenshot%20from%202026-05-13%2010-18-04.png)
![files service](../../Pictures/Screenshot%20from%202026-05-13%2010-27-44.png)
## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)