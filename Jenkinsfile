pipeline {
    agent any

    stages {


        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Test') {
            steps {
                script {
                    sh 'python3 -m unittest test_main.py'
                }
            }
        }
    }
    post{
        success{
            echo "Your code is perfect !!"
        }
        failure{
            echo "There is problems with your code !!"
        }
    }
}