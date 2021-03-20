node {
    checkout scm
    def customImage = docker.build("my-image:${env.BUILD_ID}")
    sh 'docker run -it -d -p 5000:5000 $customImage'
    customImage.push()
    customImage.push('latest')
}
