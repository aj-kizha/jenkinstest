node {
    checkout scm
    def customImage = docker.build("my-image:${env.BUILD_ID}")
    customImage.run('-p 5000:5000')
    customImage.push("my-image:${env.BUILD_ID}")
    customImage.push('latest')
}
