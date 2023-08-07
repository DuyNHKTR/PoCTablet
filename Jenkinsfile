pipeline {
  agent {
    node {
      label 'Pi'
    }

  }
  stages {
    stage('Checkout Code') {
      steps {
        git(url: 'https://github.com/DuyNHKTR/PoCTablet', branch: 'main')
      }
    }

    stage('Add logs') {
      parallel {
        stage('Add logs') {
          steps {
            sh 'ls -al'
          }
        }

        stage('Install requirements') {
          steps {
            sh 'pip3 install -r requirements.txt'
          }
        }

      }
    }

    stage('') {
      steps {
        sh 'python3 main.py'
      }
    }

  }
}