node {
    environment
    {
      registryCredential = 'dockerlogin'
        
    }
    checkout scm
    registryCredential = 'dockerlogin'
    docker.withRegistry( '', registryCredential )
    {
    def customImage = docker.build("my-image:${env.BUILD_ID}")
    customImage.run('-p 5000:5000')
    customImage.push("my-image:${env.BUILD_ID}")
    customImage.push('latest')
 }
}
