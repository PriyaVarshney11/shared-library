import subprocess
import sys

def terraform_init():
    try:
        subprocess.run(["terraform", "init"], check=True)
    except subprocess.CalledProcessError:
        print("Failed to run 'terraform init'")
        sys.exit(1)

def terraform_fmt():
    try:
        subprocess.run(["terraform", "fmt", "-recursive"], check=True)
    except subprocess.CalledProcessError:
        print("Failed to run 'terraform fmt'")
        sys.exit(1)





def terraform_validate():
    try:
        subprocess.run(["terraform", "validate"], check=True)
    except subprocess.CalledProcessError:
        print("Failed to run 'terraform validate'")
        sys.exit(1)

def terraform_plan():
    try:
        subprocess.run(["terraform", "plan"], check=True)
    except subprocess.CalledProcessError:
        print("Failed to run 'terraform plan'")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 terraform_ci.py <action>")
        sys.exit(1)

    action = sys.argv[1]
    if action == "init":
        terraform_init()
    elif action == "fmt":
        terraform_fmt()
    elif action == "validate":
        terraform_validate()
    elif action == "plan":
        terraform_plan()
    else:
        print(f"Unknown action: {action}")
        sys.exit(1)
