pipeline {
    agent any

    stages {

        stage('Test') {
            steps {
                sh '''
                    docker run --rm \
                    -v "$WORKSPACE:/app" \
                    -w /app \
                    python:3.13-slim \
                    sh -c "ls -la && pip install --no-cache-dir -r requirements.txt && python manage.py test"
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