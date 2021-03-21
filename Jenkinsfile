node {
    environment
    {
      registryCredential = 'dockerlogin'
        
    }
    checkout scm
    registryCredential = 'dockerlogin'
    docker.withRegistry( '', registryCredential )
    {
   
    def customImage = docker.build("ajaykizha/imagerepo")
    customImage.run('-p 5000:5000')
    customImage.push()
    customImage.push('${env.BUILD_ID}')
 }
}
