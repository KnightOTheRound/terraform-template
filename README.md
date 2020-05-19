# Infrastructure Bootstrap Template
A standardized starting point for projects that follow previous configurations I've set up.

##Todo

- AWS Serverless WebServer (AutismShapes Generator, API with Web Interface)
- AWS App Server (e.g. RTMP Server, Foundry VTT, Rocket.Chat)
- AWS Serverless Stack Application (Conference Registration System)
- "On-prem"/Local Server app configuration
- Azure and gCloud Wrappers

##Terraform

"Property overriding" done through co-located override file. Procedural generation of these files with executions of 
terraform for sequences of stacks.

Gitignore will ignore override files as they are usually used to override resources locally and so are not checked in
    override.tf
    override.tf.json
    *_override.tf
    *_override.tf.json

##Python

Wrapper script using Python 3.8.2

###Venv setup and Pip Packages

requests 2.23.0      /RESTful calls/
terraform-bin 1.0.1  /Provisioning Stack/ 
