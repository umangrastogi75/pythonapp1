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
                
                
            }
        }
        stage('Deliver') {
            steps {
                // Example: Push to a registry or deploy
                // sh 'echo "Deliebred"'
            }
        }
    }
}

