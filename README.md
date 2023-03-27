# didd
Docker Integration & Docker Deployment

### Summary
CICD with Docker &amp; AWS

### Basic Actions' Secrets Requirements
* SSH Key to access remote EC2 instance
* EC2 DNS info
* EC2 Username info

### Recommended Actions' Secrets Requirements
* Root Directory/Working Directory
* Repo name

### Actions Runner Workflow
1. Configure SSH to remote login to EC2 instance
2. Enter project root directory and pull in latest repo changes
3. Stop and remote existing docker container
4. Remove existing docker image
5. Build & run the new docker image
