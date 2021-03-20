node {
    checkout scm
    def customImage = docker.build("my-image:${env.BUILD_ID}")
    customImage.run()
    customImage.push()
    customImage.push('latest')
}
