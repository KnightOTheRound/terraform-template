#! /usr/bin/python3-64
import os
import terraform

print("OS:                " + os.name)
print("Terraform Version: " + terraform['TERRAFORM_VERSION'])

if __name__ == '__main__':
    print("")
