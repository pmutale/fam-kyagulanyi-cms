pipeline {
    agent none
    stages {
        stage('Install Requirements') {
            agent {
                docker {
                    image 'python:3-alpine'
                }
            }
            steps {
                sh '''
                    pip install -r requirements.txt
                    python manage.py migrate
                    python manage.py collectstatic --noinput
                    npm install && npm run build-production
                '''
            }
        }
    }
}
