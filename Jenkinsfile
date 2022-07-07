pipeline {
    agent any
    stages {
        stage('checkout') {
            steps {
                script {
                    properties([pipelineTriggers([pollSCM('30 * * * *')])])
                }
                git 'https://github.com/ehabdev/DEVOPSCourse1.git'
            }
        }
        stage('run rest_app') {
            steps {
                script {
                    
                        bat  'start /min python rest_app.py'
                }
            }
        }
     stage('run web_app') {
            steps {
                script {
                    
                        bat  'start /min python web_app.py'
                }
            }
        
        }
    stage('run backend testing') {
            steps {
                script {
                   
                        bat  'python backend_testing.py'
                }
            }
        
        }
    stage('run frontend testing') {
            steps {
                script {
                   
                        bat  'python frontend_testing.py'
                }
            }
        }
     stage('run combined testing') {
            steps {
                script {
                   
                        bat  'python combined_testing.py'
                }
            }
        }
    stage('run clean environment') {
            steps {
                script {
                   
                        bat  'python clean_envirnment.py'
                }
            }
        }
    
    }
}
