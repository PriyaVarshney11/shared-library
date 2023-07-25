# terraform_ci.py

import subprocess
import sys

class TerraformError(Exception):
    pass

def terraform_init():
    try:
        subprocess.run(["terraform", "init"], check=True)
    except subprocess.CalledProcessError:
        raise TerraformError("Failed to run 'terraform init'")

def terraform_fmt():
    try:
        subprocess.run(["terraform", "fmt", "-recursive"], check=True)
    except subprocess.CalledProcessError:
        raise TerraformError("Failed to run 'terraform fmt'")

def terraform_plan():
    try:
        subprocess.run(["terraform", "plan"], check=True)
    except subprocess.CalledProcessError:
        raise TerraformError("Failed to run 'terraform plan'")

# Provide a way to execute the actions from the command line

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python terraform_ci.py <action>")
        sys.exit(1)

    action = sys.argv[1]
    try:
        if action == "init":
            terraform_init()
        elif action == "fmt":
            terraform_fmt()
        elif action == "plan":
            terraform_plan()
        else:
            raise TerraformError(f"Unknown action: {action}")
    except TerraformError as e:
        print(str(e))
        sys.exit(1)
