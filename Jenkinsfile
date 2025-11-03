pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                // Pull the latest code from GitHub
                git branch: 'main', url: 'https://github.com/tshreya51/automation-tests.git'
            }
        }

        stage('Setup Environment') {
            steps {
                sh '''
                    echo "Creating virtual environment..."
                    python3 -m venv venv
                    source venv/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                    echo "Running automation tests..."
                    source venv/bin/activate
                    pytest --html=report.html --self-contained-html
                '''
            }
        }

        stage('Publish Report') {
            steps {
                publishHTML([
                    allowMissing: false,
                    alwaysLinkToLastBuild: true,
                    keepAll: true,
                    reportDir: '.',
                    reportFiles: 'report.html',
                    reportName: 'Automation Report'
                ])
            }
        }
    }

    post {
        always {
            echo 'Cleaning up environment...'
            sh 'deactivate || true'
        }
        success {
            echo '✅ Build succeeded!'
        }
        failure {
            echo '❌ Build failed. Check logs and report.'
        }
    }
}
