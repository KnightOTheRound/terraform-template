# terraform-template
A standardized starting point for projects that follow previous configurations I've set up.

##Todo
- AWS Serverless WebServer (AutismShapes Generator)
- AWS App Server (Foundry VTT)
- AWS Serverless Stack Application (Conference Registration System)
- "On-prem" Server app configuration

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
requests 2.23.0
terraform-bin 1.0.1
