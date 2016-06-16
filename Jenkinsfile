#!groovy

node('docker') {

    stage 'Checkout'
    checkout scm

    stage 'Lint - Wheezy'
    wrap([$class: 'AnsiColorBuildWrapper']) {
      sh 'make lint@wheezy'
    }

    stage 'Lint - Jessie'
    wrap([$class: 'AnsiColorBuildWrapper']) {
      sh 'make lint@jessie'
    }

    stage 'Test - Wheezy'
    wrap([$class: 'AnsiColorBuildWrapper']) {
      sh 'make test@wheezy'
    }

    stage 'Test - Jessie'
    wrap([$class: 'AnsiColorBuildWrapper']) {
      sh 'make test@jessie'
    }

}
