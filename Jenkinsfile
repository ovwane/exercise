pipeline {
  agent any
  stages {
    stage('build') {
      parallel {
        stage('build') {
          steps {
            echo 'build....'
          }
        }
        stage('') {
          steps {
            echo 'build2'
          }
        }
      }
    }
    stage('test') {
      steps {
        echo 'test....'
      }
    }
    stage('dev') {
      steps {
        echo 'dev....'
      }
    }
  }
}