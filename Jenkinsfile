pipeline {
    agent any
    stages {
        stage('checkout') {
            steps {
                script {
                    properties([pipelineTriggers([pollSCM('* * * * *')])])
                }
                git 'https://github.com/ehabdev/DEVOPSCourse1.git'
            }
        }
        stage('run python') {
            steps {
                script {
                    if (checkOs() == 'Windows') {
                        bat  'start /min python rest_app.py'
                    } else {
                        sh 'python 1.py'
                    }
                }
            }
        }
    }
}

def checkOs(){
    if (isUnix()) {
        def uname = sh script: 'uname', returnStdout: true
        if (uname.startsWith("Darwin")) {
            return "Macos"
        }
        else {
            return "Linux"
        }
    }
    else {
        return "Windows"
    }
}
