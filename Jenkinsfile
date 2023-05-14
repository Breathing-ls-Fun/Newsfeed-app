pipeline{
    agent any
    stages {
    
        stage('Setup Python Virtual ENV'){
        steps  {
            sh '''
            chmod +x envsetup.sh
            ./envsetup.sh
            '''}
        }
        stage('Setup Gunicorn Setup'){
            steps {
                sh '''
                chmod +x gunicorn.sh
                ./gunicorn.sh
                '''
            }
        }
        stage('setup NGINX'){
            steps {
                sh '''
                chmod +x nginx.sh
                ./nginx.sh
                '''
            }
        }
        stage('Run Tests'){
            steps {
                sh '''
                chmod +x auto_tests.sh
                ./auto_tests.sh
                '''
            }
        }
        stage('Run API Tests'){
            steps {
                sh '''
                chmod +x auto_api_tests.sh
                ./auto_api_tests.sh
                '''
            }
        }
    }
}