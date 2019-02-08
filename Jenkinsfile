pipeline {
    agent none
    stages {
        stage('Sync databases') {
            agent {
                docker {
                    image 'python:2-alpine'
                }
            }
            steps {
                sh 'python manage.py migrate'
            }
        }
    }
}
