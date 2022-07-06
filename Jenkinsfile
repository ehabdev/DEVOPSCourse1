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
        stage('run web_app') {
            steps {
                script {
                    if (checkOs() == 'Windows') {
                        bat  'python web_app.py'
                    } else {
                        sh 'python 1.py'
                    }
                }
            }
        }
     stage('run rest_app') {
            steps {
                script {
                    if (checkOs() == 'Windows') {
                        bat  'start/min python rest_app.py'
                    } else {
                        sh 'python 1.py'
                    }
                }
            }
        
        }
    stage('run backend testing') {
            steps {
                script {
                    if (checkOs() == 'Windows') {
                        bat  'python backend_testing_upd.py'
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
