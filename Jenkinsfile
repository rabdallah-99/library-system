pipeline {
  agent any
      options {
    buildDiscarder(logRotator(numToKeepStr: '5'))
  }
  environment {
    DOCKERHUB_CREDENTIALS = credentials('rihamm80-dockerhub')
        MYSQL_URI = credentials("MYSQL_URI")
        SECRET_KEY = credentials("SECRET_KEY")
	MYSQL_USER= 'root'
	MYSQL_URL = 'mysql'
	MYSQL_DATABASE = 'library'
	MYSQL_PASSWORD = credentials("MYSQL_PASSWORD")
  }
  stages {
    stage('Build') {
      steps {
        sh 'docker build -t databasemysql:8 database'
	sh 'docker build -t flask-library:latest . '
 
      }
    }
    stage('RUN') {
      steps {
        sh ' docker network create mynetwork '
	sh ' docker run -d --name mysql --network mynetwork databasemysql:8'
	sh 'docker run -d --name flask-app --network mynetwork flask-library:latest '
	sh ' docker run -d --name nginx -p 80:80 --network mynetwork --mount type=bind,source=$(pwd)/nginx.conf,target=/etc/nginx/nginx.conf nginx:latest'
      }
    }
  }
  post {
    always {
      sh 'docker logout'
      
    }
  }

}  
