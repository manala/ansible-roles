#!groovy

node('docker') {

    stage 'Checkout'
    checkout scm

    stage 'Test - Wheezy'
    wrap([$class: 'AnsiColorBuildWrapper']) {
      sh 'make test@wheezy'
    }

    stage 'Test - Jessie'
    wrap([$class: 'AnsiColorBuildWrapper']) {
      sh 'make test@jessie'
    }

}
