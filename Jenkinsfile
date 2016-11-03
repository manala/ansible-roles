#!groovy

node('docker') {

    stage 'Checkout'
    checkout scm

    stage 'Lint - Jessie'
    wrap([$class: 'AnsiColorBuildWrapper']) {
      sh 'make lint@jessie'
    }

    stage 'Test - Jessie'
    wrap([$class: 'AnsiColorBuildWrapper']) {
      sh 'make test@jessie'
    }

}
