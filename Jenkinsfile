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

        stage('Deploy') {
            steps {
                sh '''
                    docker stop task-list-app || true
                    docker rm task-list-app || true

                    docker run -d \
                    --name task-list-app \
                    -p 8000:8000 \
                    task-list
                '''
            }
        }
    }
}