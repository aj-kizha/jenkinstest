node {
   stage('Get Source') {
      // copy source code from local file system and test
      // for a Dockerfile to build the Docker image
      git ('https://github.com/upasana-mittal/flask-dockerized-jenkins.git')
      if (!fileExists("dockerfile")) {
         error('Dockerfile missing.')
      }
   }
   stage('Build Docker') {
       // build the docker image from the source code using the BUILD_ID parameter in image name
         "sudo docker build -t flask-app ."
   }
   stage("run docker container"){
        docker run -it -d -p 8000:5000 --name flask-app:latest"
    }
}
