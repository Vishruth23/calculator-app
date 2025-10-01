pipeline {
    agent any
    environment {
        DOCKERHUB_USER = 'vvj23'
        DOCKER_IMAGE = "${DOCKERHUB_USER}/calculator-app"
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/Vishruth23/calculator-app.git'
            }
        }

        stage('Install dependencies & Test') {
            steps {
                sh 'pip install -r requirements.txt'
                sh 'pytest -q'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $DOCKER_IMAGE:latest .'
            }
        }

        stage('Push to Docker Hub') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub-creds', usernameVariable: 'USER', passwordVariable: 'PASS')]) {
                    sh 'echo $PASS | docker login -u $USER --password-stdin'
                    sh 'docker push $DOCKER_IMAGE:latest'
                }
            }
        }
    }

    post {
        success {
            echo 'Pipeline finished successfully ✅'
        }
        failure {
            echo 'Pipeline failed ❌'
        }
    }
}
