node {
    environment
    {
      registryCredential = 'dockerlogin'
        
    }
    checkout scm
    stage('test') {
      steps {
        sh 'python test.py'
      }   
    }
    registryCredential = 'dockerlogin'
    docker.withRegistry( '', registryCredential )
    {
   
    def customImage = docker.build("ajaykizha/imagerepo:${env.BUILD_ID}")
    sh 'echo hello'  
    sh 'flake8'
    customImage.run('-p 5000:5000')   
    customImage.push()
 }
}
