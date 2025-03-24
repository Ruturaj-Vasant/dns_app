
# Distributed System with Flask: Auth, Fibonacci, and User Servers

## Overview
This project demonstrates a simple distributed system built using Flask with three interconnected services:
- **Auth Server**: Handles domain name registration and lookup.
- **Fibonacci Server**: Calculates and stores Fibonacci numbers.
- **User Server**: Coordinates requests between the other services.

The project uses Docker for containerization and includes Kubernetes deployment configuration for orchestration.

## Services:
1. **Auth Server (AS)**:
   - Registers and looks up domain names with associated IP addresses.

2. **Fibonacci Server (FS)**:
   - Calculates Fibonacci numbers for provided inputs and stores them for future retrieval.

3. **User Server (US)**:
   - Queries the **Auth Server** for domain information and fetches Fibonacci numbers from the **Fibonacci Server**.

## Setup Instructions:
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/project-name.git
   cd project-name
   ```

2. Run the application locally:
   ```bash
   docker-compose up
   ```

3. Access the services:
   - **Auth Server**: `http://localhost:53533`
   - **Fibonacci Server**: `http://localhost:9090`
   - **User Server**: `http://localhost:8080`

## Kubernetes Deployment:
This project includes a Kubernetes deployment file (`deploy_dns.yml`) to deploy the services. 

1. Apply the deployment configuration:
   ```bash
   kubectl apply -f deploy_dns.yml
   ```

## Dependencies:
- Flask==2.3.2
- Werkzeug==2.3.4
- Docker
- Kubernetes (for deployment)

## Conclusion:
This project showcases a basic distributed system with domain registration, Fibonacci calculation, and service interaction. It demonstrates the use of Docker and Kubernetes for service deployment and orchestration.
