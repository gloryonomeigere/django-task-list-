pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Test') {
            steps {
                sh '''
                    docker run --rm \
                    -v "$PWD:/app" \
                    -w /app \
                    python:3.13-slim \
                    sh -c "pip install --no-cache-dir -r requirements.txt && python manage.py test"
                '''
            }
        }

        stage('Docker Build') {
            steps {
                sh 'docker build -t task-list .'
            }
        }
    }
}