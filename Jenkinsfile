node {
    environment
    {
      registryCredential = 'dockerlogin'
        
    }
    checkout scm 
    registryCredential = 'dockerlogin'
    echo "cheking permissions"
    sh 'ls -lrt /usr/run/ '
    docker.withRegistry( '', registryCredential )
    {
       
    def customImage = docker.build("ajaykizha/imagerepo:${env.BUILD_ID}")
    sh 'echo hello' 
    customImage.run('-p 5000:5000')   
    customImage.push()
    }
    stage('Sonarqube Analysis')
    {
     echo "inside sonarqube analysis"   
     sh 'ls -lrt'   
    }
    
}
