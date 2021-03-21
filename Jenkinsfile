node {
    environment
    {
      registryCredential = 'dockerlogin'
        
    }
    checkout scm 
    registryCredential = 'dockerlogin'
    docker.withRegistry( '', registryCredential )
    {
   
    def customImage = docker.build("ajaykizha/imagerepo:${env.BUILD_ID}")
    sh 'echo hello'  
    sh 'python test.py'    
    sh 'flake8'
    customImage.run('-p 5000:5000')   
    customImage.push()
 }
}
