pipeline {
  agent any
  stages {
    stage('Checkout Code') {
      steps {
        git(url: 'https://github.com/DuyNHKTR/PoCTablet', branch: 'main')
      }
    }

    stage('Add logs') {
      steps {
        sh 'ls -al'
      }
    }

  }
}