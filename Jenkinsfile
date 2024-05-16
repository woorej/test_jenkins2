pipeline {
    agent any
    environment {
        SERVER_IP = "218.233.16.216"
        SERVER_PORT = "30722"
        SERVER_USER = "groupai"
        REPO_URL = 'https://github.com/woorej/test_jenkins2.git'
        PROJECT_DIR = '/home/groupai/workspace/test_jenkins2'
    }
    // stages {
    //     stage('Checkout') {
    //         steps {
    //             checkout scm: [ $class: 'GitSCM', branches: [[name: '*/master']],
    //                             userRemoteConfigs: [[credentialsId: 'server_7',
    //                             url: '${REPO_URL}']]]
    //         }
    //     }
        stage('Prepare Environment') {
            steps {
                script {
                    sshagent(['server_7']) {
                        sh """
                        ssh -o StrictHostKeyChecking=no -p ${SERVER_PORT} ${SERVER_USER}@${SERVER_IP} '
                        if [ ! -d "${PROJECT_DIR}" ]; then
                            echo "Directory does not exist. Cloning repository..."
                            git clone ${REPO_URL} ${PROJECT_DIR}
                        else
                            echo "Directory exists. Pulling latest changes..."
                            cd ${PROJECT_DIR}
                            git pull
                        fi
                        '
                        """
                    }
                }
            }
        }
        stage('Setup Virtual Environment') {
            steps {
                script {
                    sshagent(['server_7']) {
                        sh """
                        ssh -o StrictHostKeyChecking=no -p ${SERVER_PORT} ${SERVER_USER}@${SERVER_IP} '
                        if [ ! -d "${PROJECT_DIR}/venv" ]; then
                            echo "Creating virtual environment..."
                            /usr/bin/python3.11 -m venv ${PROJECT_DIR}/venv
                        fi
                        source ${PROJECT_DIR}/venv/bin/activate
                        pip3 install -r ${PROJECT_DIR}/requirements.txt
                        deactivate
                        '
                        """
                    }
                }
            }
        }
        stage('Run Tests') {
            steps {
                script {
                    sshagent(['server_7']) {
                        sh """
                        ssh -o StrictHostKeyChecking=no -p ${SERVER_PORT} ${SERVER_USER}@${SERVER_IP} '
                        source ${PROJECT_DIR}/venv/bin/activate
                        python3 -m pytest ${PROJECT_DIR}/tests
                        deactivate
                        '
                        """
                    }
                }
            }
        }
        stage('Build and Deploy') {
            steps {
                script {
                    sshagent(['server_7']) {
                        sh """
                        ssh -o StrictHostKeyChecking=no -p ${SERVER_PORT} ${SERVER_USER}@${SERVER_IP} '
                        source ${PROJECT_DIR}/venv/bin/activate
                        pip3 freeze | grep calculator && pip3 uninstall -y calculator
                        pip3 install ${PROJECT_DIR}
                        '
                        """
                    }
                }
            }
        }
    }
}