pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Source code is available in the workspace'
            }
        }

        stage('Build') {
            steps {
                echo 'Building the Flask application with Docker'
                sh 'docker build -t devsecops-flask-app .'
            }
        }

        stage('Test') {
            steps {
                echo 'Checking application files'
                sh 'python3 -m py_compile app.py'
            }
        }
    }
}
