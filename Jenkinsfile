pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                sh 'docker compose build'
            }
        }
    
        stage('trivy') {
            steps {
                sh 'trivy image --format template --template /usr/local/share/trivy/templates/html.tpl -o trivy-report.html pythonapp'
                //sh 'trivy image --format html -o trivy-report.html pythonapp'

            }
        }
        
        stage('Test') {
            steps {
                sh 'docker compose up -d'
                // Add test commands here, e.g.:
                
                
            }
        }
        stage('Deliver') {
            steps {
                // Example: Push to a registry or deploy
                 sh 'echo "Deliebred"'
            }
        }
    }
}
