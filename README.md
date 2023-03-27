# didd
Docker Integration & Docker Deployment

## Summary
CICD with Docker &amp; AWS

## Basic Actions' Secrets Requirements
[+] SSH Key to access remote EC2 instance
[+] EC2 DNS info
[+] EC2 Username info

## Recommended Actions' Secrets Requirements
[+] Root Directory/Working Directory

## Actions Runner Workflow
[+] Configure SSH to remote login to EC2 instance
[+] Enter project root directory and pull in latest repo changes
[+] Stop and remote existing docker container
[+] Remove existing docker image
[+] Build & run the new docker image
