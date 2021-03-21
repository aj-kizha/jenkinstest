node {
    environment
    {
      registryCredential = 'dockerlogin'
        
    }
    checkout scm
    registryCredential = 'dockerlogin'
    docker.withRegistry( '', registryCredential )
    {
    dockerImage.push("$BUILD_NUMBER")
    dockerImage.push('latest')    
   
    }    
}
