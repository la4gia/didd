# didd
Docker Integration & Docker Deployment

### Summary
CICD with Docker

### Basic Actions' Secrets Requirements
* SSH Key to access remote instance
* Remote Host IP (or EC2 DNS info)
* Remote Username

### Actions Runner Workflow
1. Configure SSH to login to remote instance
2. Pull in the latest repo changes
3. Stop existing docker container
4. Remove existing docker image
5. Build & run the new docker image
6. Clean up

### Prerequisites
* Remote Instance with ability to pull repository
  * Repo will need to be cloned first
* Docker running on instance
* Git installed on instance
* Dockerfile must be in project folder's root

### Note
* This is designed to use the GitHub provided runner
  * If you prefer a self-hosted runner, move the ssh config info to the runner's host 
* Images are tagged with the project folder's name