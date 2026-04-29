pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git url: 'https://github.com/Pranithamarri/TASK.git',
                    branch: 'main'
            }
        }

        stage('Build') {
            steps {
                echo 'Building project...'
            }
        }
    }
}
