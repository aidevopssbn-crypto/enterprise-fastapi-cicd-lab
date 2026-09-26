pipeline {
    agent none

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
            agent any
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

                    python -m pytest \
                      --cov=app \
                      --cov-report=xml:test-results/coverage.xml \
                      --junitxml=test-results/pytest.xml
                '''
            }
            post {
                always {
                    junit allowEmptyResults: true,
                          testResults: 'test-results/pytest.xml'

                    archiveArtifacts(
                        allowEmptyArchive: true,
                        artifacts: 'test-results/coverage.xml'
                    )
                }
            }
        }

        stage('Static & Dependency Checks') {
            agent {
                docker {
                    image 'python:3.13-slim'
                }
            }
            steps {
                sh '''
                    python -m pip install --upgrade pip
                    pip install -r requirements-dev.txt

                    ruff check app tests
                    bandit -r app -ll
                    pip-audit -r requirements.txt
                '''
            }
        }

        stage('SonarQube Analysis') {
            agent {
                docker {
                    image 'sonarsource/sonar-scanner-cli:12.2.0.4256_8.1.0'
                }
            }
            steps {
                withSonarQubeEnv('SonarQube-Local') {
                    sh '''
                        export SONAR_TOKEN="$SONAR_AUTH_TOKEN"
                        sonar-scanner
                    '''
                }
            }
        }

        stage('Quality Gate') {
            agent none
            steps {
                timeout(time: 10, unit: 'MINUTES') {
                    waitForQualityGate abortPipeline: true
                }
            }
        }

        stage('Build Image') {
            agent any
            steps {
                sh '''
                    docker build -t ${IMAGE_NAME}:${IMAGE_TAG} .
                    docker save -o image.tar ${IMAGE_NAME}:${IMAGE_TAG}
                '''

                archiveArtifacts(
                    artifacts: 'image.tar',
                    fingerprint: true
                )
            }
        }
    }

    post {
        always {
            echo "Build result: ${currentBuild.currentResult}"
        }
    }
}