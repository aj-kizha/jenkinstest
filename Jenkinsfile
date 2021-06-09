node {
    environment
    {
      registryCredential = 'dockerlogin'
      AWS_ACCESS_KEY_ID     = credentials('jenkins-aws-secret-key-id')
      AWS_SECRET_ACCESS_KEY = credentials('jenkins-aws-secret-access-key')  
        
    }
    def flake8_status = true
    checkout scm 
    registryCredential = 'dockerlogin'
    echo "cheking permissions"
    sh "whoami"
    //sh 'sudo usermod -a -G docker jenkins'
    //sh 'sudo service jenkins restart'
    //sh 'sudo chmod 777 /var/run/docker.sock'
    //sh 'ls -lrt /var/run/ '
    try 
    {
        stage('QualityAnalysis')
        {
           echo "running flake8"
           sh "ls -lrt"
           sh "flake8" 
           //sh "bandit -r . -f json"
            sh "bandit -r . -f json -o report.json"
        }
    }catch(e)
    {
        flake8_status=false
    }
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
     withCredentials([usernamePassword(credentialsId: 'awsdynamodbaccess', usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD')])
    {
  // available as an env variable, but will be masked if you try to print it out any which way
  // note: single quotes prevent Groovy interpolation; expansion is by Bourne Shell, which is what you want
  sh 'echo $PASSWORD'
  // also available as a Groovy variable
  echo USERNAME
  // or inside double quotes for string interpolation
  echo "username is $USERNAME"
  echo "password is $PASSWORD"
        
  sh 'pip install boto3'
  sh 'python fetchinsertdynamodb.py $USERNAME $PASSWORD'
   }
    stage('fetch metrics and insert to dynamodb')
    {
        //AWS_ACCESS_KEY_ID  = credentials('jenkins-aws-secret-key-id')
        //AWS_SECRET_ACCESS_KEY = credentials('jenkins-aws-secret-access-key')
        //echo $AWS_ACCESS_KEY_ID
        //echo $AWS_SECRET_ACCESS_KEY
       // echo USERNAME
        //echo "username is $USERNAME"
        echo "fetch metrics and inset to db"
        //sh 'pip install boto3'
        //sh 'python fetchinsertdynamodb.py $USERNAME $PASSWORD'
    }
    
    if (flake8_status)
    {
        echo "success"
    }
    else
    {
        echo "flake8 failed"
    }    
    
}
