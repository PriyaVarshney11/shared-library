def executeShellCommand(command) {
    def process = command.execute()
    process.waitForProcessOutput(System.out, System.err)
    return process.exitValue()
}

// Call the Python script with the desired action ("init", "fmt", or "plan")
def action = "init"
def command = "python3 terraform_ci.py ${action}"

def exitCode = executeShellCommand(command)

// Check the exit code and handle errors if necessary
if (exitCode != 0) {
    println "Error: Terraform CI failed with exit code ${exitCode}"
    System.exit(exitCode)
} else {
    println "Terraform CI executed successfully."
}
