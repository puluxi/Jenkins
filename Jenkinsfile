#!/usr/bin/env groovy
pipeline {
  agent any

  stages {
    stage('Build') {
        steps {
            echo 'Building..'
        }
    }
    stage('Test') {
        steps {
            echo 'Testing..'
        }
    }
    stage('Deploy') {
        steps {
            echo 'Deploying....'
        }
    }
  }
  post {
        always {
            echo 'One way or another, I have finished'
            deleteDir() /* clean up our workspace */
        }
        success {
            echo 'I succeeeded!'
			mail to: '470971464@qq.com',
            subject: "Sucessful Pipeline: ${currentBuild.fullDisplayName}",
            body: "Something is good with ${env.BUILD_URL}"

        }
        unstable {
            echo 'I am unstable :/'
        }
        failure {
            echo 'I failed :('
        }
        changed {
            echo 'Things were different before...'
        }
    }
}