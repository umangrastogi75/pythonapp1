pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                sh 'docker-compose build'
            }
        }
        stage('Test') {
            steps {
                sh 'docker-compose up -d'
                // Add test commands here, e.g.:
                // sh 'docker-compose exec app pytest tests/'
                
            }
        }
        stage('Deliver') {
            steps {
                // Example: Push to a registry or deploy
                // sh 'docker push myrepo/myapp:latest'
            }
        }
    }
}

