pipeline {
    agent {
        dockerfile true
        docker {
        args '-it --entrypoint=/bin/bash'
        }
    }
    stages {
        stage('Test') {
            steps {
                sh 'node --version'
            }
        }
    }
}
