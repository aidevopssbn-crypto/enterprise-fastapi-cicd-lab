pipeline {
    agent any

    options {
        timestamps()
        disableConcurrentBuilds()
        skipDefaultCheckout(true)
    }

    environment {
        IMAGE_NAME = "enterprise-fastapi-lab"
        IMAGE_TAG  = "build-${BUILD_NUMBER}"
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Python Unit Test') {
            agent {
                docker {
                    image 'python:3.13-slim'
                }
            }
            steps {
                sh '''
                    python -m pip install --upgrade pip
                    pip install -r requirements-dev.txt
                    mkdir -p test-results
                    pytest --cov=app --cov-report=xml:test-results/coverage.xml
                '''
            }
            post {
                always {
                    junit allowEmptyResults: true, testResults: 'test-results/pytest.xml'
                }
            }
        }

        stage('Static Checks') {
            agent {
                docker {
                    image 'python:3.13-slim'
                }
            }
            steps {
                sh '''
                    pip install -r requirements-dev.txt
                    ruff check app tests
                    bandit -r app -ll
                    pip-audit -r requirements.txt
                '''
            }
        }

        stage('Build Image') {
            steps {
                sh 'docker build -t ${IMAGE_NAME}:${IMAGE_TAG} .'
                sh 'docker save -o image.tar ${IMAGE_NAME}:${IMAGE_TAG}'
                archiveArtifacts artifacts: 'image.tar', fingerprint: true
            }
        }
    }

    post {
        always {
            echo "Build result: ${currentBuild.currentResult}"
        }
    }
}
