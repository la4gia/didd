# didd
Docker Integration & Docker Deployment

### Summary
CICD with Docker

### Basic Actions' Secrets Requirements
* SSH Key to access remote instance
* Remote Host IP (or EC2 DNS info)
* Remote Username 

### Recommended Actions' Secrets Requirements
* Project Directory/Working Directory
* Repo name

### Actions Runner Workflow
1. Configure SSH to remote login to remote instance
2. Pull in the latest repo changes
3. Stop and remove existing docker container
4. Remove existing docker image
5. Build & run the new docker image

### Prerequisites
* Remote Instance with ability to pull repository
  * Repo will need to be cloned first
* Docker running on instance
* Git installed on instance

### Start-up Note
* Comment lines 32-37 in didd.yml for first run
  * Error will be thrown if previous image & container does not exist
