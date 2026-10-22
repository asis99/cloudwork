
pipeline {
    agent any

    environment {
        AWS_REGION = 'us-east-1'
        ECR_REPOSITORY = 'python-backend'
        K8S_DEPLOYMENT = 'python-backend'
        CONTAINER_NAME = 'python-backend'
    } 

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/asis99/cloudwork.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh '''
                    docker build -t ${ECR_REPOSITORY}:${BUILD_NUMBER} .
                '''
            }
        }

        stage('Push to ECR') {
            steps {
                sh '''
                    ACCOUNT_ID=$(aws sts get-caller-identity \
                        --query Account --output text)

                    ECR_URI="${ACCOUNT_ID}.dkr.ecr.${AWS_REGION}.amazonaws.com/${ECR_REPOSITORY}"

                    aws ecr get-login-password \
                        --region "${AWS_REGION}" |
                        docker login \
                        --username AWS \
                        --password-stdin \
                        "${ACCOUNT_ID}.dkr.ecr.${AWS_REGION}.amazonaws.com"

                    docker tag "${ECR_REPOSITORY}:${BUILD_NUMBER}" \
                        "${ECR_URI}:${BUILD_NUMBER}"

                    docker push "${ECR_URI}:${BUILD_NUMBER}"
                '''
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                sh '''
                    ACCOUNT_ID=$(aws sts get-caller-identity \
                        --query Account --output text)

                    ECR_URI="${ACCOUNT_ID}.dkr.ecr.${AWS_REGION}.amazonaws.com/${ECR_REPOSITORY}"

                    kubectl apply -f k8s/deployment.yaml
                    kubectl apply -f k8s/service.yaml

                    kubectl set image \
                        deployment/${K8S_DEPLOYMENT} \
                        ${CONTAINER_NAME}="${ECR_URI}:${BUILD_NUMBER}"

                    kubectl rollout status \
                        deployment/${K8S_DEPLOYMENT} \
                        --timeout=180s
                '''
            }
        }
    }
}
