pipeline {
    agent {
        dockerfile true
        args '-it --entrypoint=/bin/bash'
    }
    stages {
        stage('Test') {
            steps {
                sh 'node --version'
            }
        }
    }
}
