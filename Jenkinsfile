pipeline{
    agent any
    stages{
        stage('Build'){
            steps{
                echo 'Building..'
                bat 'docker build -t demoapp:v1 .'
            }
        }
        stage('Login to DockerHub'){
            steps{
                echo 'Logging in to DockerHub'
                bat 'docker login -u "ashwitharapelli" -p "Ashu@2410"'
            }
        }
        stage('Push Image'){
            steps{
                echo 'Pushing Image to DockerHub'
                bat 'docker tag demoapp:v1 ashwitharapelli/exam:v1'
                bat 'docker push ashwitharapelli/exam:v1'
            }
        }
        stage('Deployment'){
            steps{
                echo 'Deploying Application'
                bat 'kubectl apply -f deployment.yaml --validate=false'
                bat 'kubectl apply -f service.yaml'
            }
        }
    }  
    post{
        success{
            echo 'pipeline build Successfully'
        }
        failure{
            echo 'pipeline build Failed'
        }
    } 
}
