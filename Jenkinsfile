pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
                echo 'Source code checked out into the workspace'
            }
        }

        stage('Validate and Test') {
            steps {
                echo 'Checking Python syntax, installing dependencies, and running tests'
                sh '''
                    set -eu
                    python3 -m py_compile app.py test_app.py
                    python3 -m venv .venv
                    . .venv/bin/activate
                    python -m pip install -r requirements.txt
                    python -m unittest discover -v
                '''
            }
        }

        stage('Build') {
            steps {
                echo 'Building the Flask application Docker image'
                sh 'docker build -t devsecops-flask-app .'
            }
        }
    }
}
