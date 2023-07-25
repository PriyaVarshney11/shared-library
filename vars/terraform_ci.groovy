def call(Closure body){
     def config = [:]
     body.resolveStrategy = Closure.DELEGATE_FIRST
     body.delegate = config
     body()
     
pipeline {
    agent any

    stages {
        stage('AWS Example') {
            steps {
                // Retrieve AWS credentials from Jenkins credentials store
                withCredentials([[
                    $class: 'AmazonWebServicesCredentialsBinding',
                    accessKeyVariable: 'AWS_ACCESS_KEY_ID',
                    secretKeyVariable: 'AWS_SECRET_ACCESS_KEY',
                    credentialsId: 'jenkins-user'
                ]]) {
                    // Now you can use the AWS credentials in your steps
                    // For example, using AWS CLI with Python
                    sh 'pip install awscli' // Install AWS CLI for Python
                    sh 'aws ec2 describe-instances --region us-east-1' // Example AWS CLI command
                }
            }
        }

        stage('Terraform CI') {
            steps {
                script {
                    //def action = "init"
                    //def command = "python3 terraform_ci.py ${action}"
                    //sh "python3 $WORKSPACE/resources/terraform_ci.py ${action}"
                      def content = readFileFromResources('terraform_ci.py')
                      println 'content'
                      writeFile file: 'output.py' , text: content
                      sh "python3 output.py init"

                }
            }
        }
    }
}
}

