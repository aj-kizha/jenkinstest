node {
    environment
    {
      registryCredential = 'dockerlogin'
      AWS_ACCESS_KEY_ID     = credentials('jenkins-aws-secret-key-id')
      AWS_SECRET_ACCESS_KEY = credentials('jenkins-aws-secret-access-key')  
        
    }
    checkout scm 
    registryCredential = 'dockerlogin'
    echo "cheking permissions"
    sh "whoami"
    //sh 'sudo usermod -a -G docker jenkins'
    //sh 'sudo service jenkins restart'
    //sh 'sudo chmod 777 /var/run/docker.sock'
    //sh 'ls -lrt /var/run/ '
    docker.withRegistry( '', registryCredential )
    {
       
    def customImage = docker.build("ajaykizha/imagerepo:${env.BUILD_ID}")
    sh 'echo hello' 
    //customImage.run('-p 5000:5000')   
    customImage.push()
    }
    stage('Sonarqube Analysis')
    {
     echo "inside sonarqube analysis"   
     sh 'ls -lrt'   
     withSonarQubeEnv('sonarqubeserver')
        {
           echo "sonarqubeserver"
           scannerHome = tool 'sonarscanner' 
           sh "${scannerHome}/bin/sonar-scanner"
        }
    }
   
    stage('fetch metrics and insert to dynamodb')
    {
        //AWS_ACCESS_KEY_ID  = credentials('jenkins-aws-secret-key-id')
        //AWS_SECRET_ACCESS_KEY = credentials('jenkins-aws-secret-access-key')
        echo $AWS_ACCESS_KEY_ID
        echo $AWS_SECRET_ACCESS_KEY
        echo "fetch metrics and inset to db"
        sh 'pip install boto3'
        sh 'python fetchinsertdynamodb.py $AWS_ACCESS_KEY_ID $AWS_SECRET_ACCESS_KEY'
    }
    
}
