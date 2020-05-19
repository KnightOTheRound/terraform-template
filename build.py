#! /usr/bin/python3-64
import argparse
import datetime
import os
import subprocess
import sys
import configparser

import terraform
# import ansible ?? maybe ??


DEBUG_ENABLED = False
DEFAULT_CONFIG = {
                    'DEFAULT': {},
                    'Providers': {'AWS': False, "Azure": False, "Google": False, "Local": True},
                    'Applications': {
                        'Serverless': "ContentServer,StateBasedWorkflow",
                        'Server': "BasicLamp",
                        'Container': "Python38DockerContainer"
                    },
                    'Application:ContentServer': {},
                    'Application:StateBasedWorkflow': {},
                    'Application:BasicLamp': {},
                    'Application:Python38DockerContainer': {},
                    'Security': {}
                 }


def build_stack(stack):
    # TODO Build Stack Wrapper Mechanism
    # TODO Generate Overrides from passed config
    # TODO Build Stack with Terraform
    # TODO Test Stack with Terraform
    return stack


def build_documentation(name):
    if name == "documentation":
        mdfile_list = ["documentation/architecture.md"]
    elif name == "readme":
        mdfile_list = ["README.md", "modules\\README.md", "documentation\\README.md", "config\\README.md"]
    elif name == "secrets":
        mdfile_list = ["README.md"]
    else:
        mdfile_list = ["README.md"]
    if DEBUG_ENABLED: print(mdfile_list)
    for mdfile in mdfile_list:
        print("\t\t" + os.getcwd() + os.sep + mdfile)
        # TODO Generate HTML from Markdown
        # TODO Generate PDF from HTML
    return True


if __name__ == '__main__':
    process_start_time = datetime.datetime.now()
    print("Runtime Options")
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--debug",   help="debug options and output",  action="store_true")
    parser.add_argument("-t", "--timeout", help="process timeout",           type=int)
    parser.add_argument("-c", "--config",  help="config file path",          type=str)
    parser.add_argument("name",            help="stack instance name",       type=str)
    args = parser.parse_args()
    if args.debug:
        DEBUG_ENABLED = True
    if args.config is not None:
        config = configparser.ConfigParser()
        config.read(args.config)
    else:
        config = configparser.ConfigParser()
        config.read_dict(DEFAULT_CONFIG)
    # Output Runtime Settings
    print("OS:                    " + os.name)
    print("CWD:                   " + os.getcwd())
    print("Python:                " + sys.version)
    if DEBUG_ENABLED:
        print("  Installed Modules:")
        modules = subprocess.run([sys.executable, "-m", "pip", "freeze"], capture_output=True).stdout.\
            decode('utf-8').split("\n")
        for module in modules:
            print("                       " + module)
    print("Terraform:             " + terraform.TERRAFORM_EXECUTABLE)
    print("Terraform platform:    " + terraform.PLATFORM)
    if DEBUG_ENABLED:
        print("Environment Variables: ")
        for env in os.environ:
            print("                       " + env + " : " + str(os.environ[env]))
        print("Arguments:             ")
        for argument in args.__dict__:
            print("                       " + argument + " : " + str(args.__dict__[argument]))
    # Start stack build
    print("\n\nBuilding stack: " + args.name)
    build_stack(args.name)
    print("Building stack " + args.name + " completed\n")
    # Build Documentation
    print("Assembling Documentation for : " + args.name)
    documentation_status = build_documentation("readme")
    print("Documentation Complete\n\n")
    # Runtime Report
    process_end_time = datetime.datetime.now()
    process_total_time = process_end_time - process_start_time
    print("build start:    " + process_start_time.strftime("%m/%d/%Y, %H:%M:%S"))
    print("build end:      " + process_end_time.strftime("%m/%d/%Y, %H:%M:%S"))
    print("build duration: " + str(process_total_time.total_seconds()) + " seconds")
    print("DONE.")
