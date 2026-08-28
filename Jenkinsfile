pipeline {
    agent any

    stages {

        stage('Test') {
            steps {
                sh '''
                    python3 --version
                    python3 -m pip install --break-system-packages -r requirements.txt
                    python3 manage.py test
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