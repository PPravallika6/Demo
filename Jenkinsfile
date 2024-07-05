pipeline {
    agent any

    environment {
        // Docker Hub credentials ID in Jenkins
        DOCKER_CREDENTIALS_ID = 'dockerHub'
        // Docker Hub username and repository name
        DOCKER_HUB_REPO = 'palurupravallika/pythonapp'
        // Image tag (e.g., the Git commit hash or build number)
        IMAGE_TAG = "${env.BUILD_ID}"
    }

    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/your-username/your-repo.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    docker.build("${DOCKER_HUB_REPO}:${IMAGE_TAG}")
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                script {
                    docker.withRegistry('https://index.docker.io/v1/', DOCKER_CREDENTIALS_ID) {
                        docker.image("${DOCKER_HUB_REPO}:${IMAGE_TAG}").push()
                    }
                }
            }
        }

        stage('Run Docker Container') {
            steps {
                script {
                    // Stop and remove any existing container with the same name
                    sh """
                        docker rm -f my-container || true
                        docker run -d --name my-container -p 80:80 ${DOCKER_HUB_REPO}:${IMAGE_TAG}
                    """
                }
            }
        }
    }

    post {
        always {
            cleanWs()
        }
    }
}
