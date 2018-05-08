pipeline {
  agent any
  stages {
    stage('build') {
      steps {
        retry(count: 3) {
          sh 'python ----'
        }

      }
    }
  }
}