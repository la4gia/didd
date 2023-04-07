# didd
Docker Integration & Docker Deployment

### Summary
CICD with Docker via SSH

### Basic Actions' Secrets Requirements
* SSH Key to access remote instance
* Remote Host IP (or EC2 DNS info)
* Remote Username

### Actions Runner Workflow
1. Configure SSH login to remote instance
2. Pull in the latest repo changes
3. Stop existing docker containers
4. Remove altered/deleted images
5. Build/rebuild new/updated images
6. Build new containers
7. Clean up

### Prerequisites
* Remote Instance with ability to pull repository
  * Repo will need to be cloned first
* Docker running on instance
* Git installed on instance
* Dockerfile must be in project's root folder

### Note
* This is designed to use the GitHub provided runner
  * If you prefer a self-hosted runner, move the ssh config info to the runner's host 
* Images are tagged with the project folder's name
* If the Dockerfile is removed, the associated image will be removed
* Included a workflow to manually re-deploy all running containers