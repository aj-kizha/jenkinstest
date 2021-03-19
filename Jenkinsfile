
pipeline {
   stage('Get Source') {
      // copy source code from local file system and test
      // for a Dockerfile to build the Docker image
      git ('https://github.com/aj-kizha/jenkinstest.git')
      if (!fileExists("dockerfile")) {
         error('Dockerfile missing.')
      }
   }
   stage('test') {
      steps {
        'python test.py'
      }
   }
}
