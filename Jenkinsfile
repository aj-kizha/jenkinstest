pipeline {
  agent { docker { image 'python:3.7.6' } }
  stages {  
    stage('test') {
      steps {
        sh 'python test.py'
      }
      post {
        always {
          junit 'test-reports/*.xml'
        }
      }    
    }
  }
}
