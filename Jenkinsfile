pipeline {
    agent any  // Ejecutar en cualquier nodo disponible de Jenkins

    stages {
        stage('Preparación') {
            steps {
                script {
                    echo 'Preparando el entorno...'
                    // Aseguramos que Python y pip estén instalados en el contenedor
                    sh '''
                        apt-get update
                        apt-get install -y python3 python3-pip
                    ''' // Instalamos Python3 y pip3
                    sh 'pip3 install -r requirements.txt'  // Instalamos las dependencias desde el archivo requirements.txt
                }
            }
        }

        stage('Ejecutar Pruebas') {
            steps {
                script {
                    echo 'Ejecutando pruebas...'
                    // Ejecutamos las pruebas con pytest o unittest (según como hayas configurado las pruebas)
                    sh 'python3 -m unittest test_nomina.py'
                }
            }
        }

        stage('Resultados') {
            steps {
                script {
                    echo 'Generando resultados...'
                    // Aquí puedes agregar acciones para guardar los resultados de las pruebas o cualquier otra acción
                }
            }
        }
    }

    post {
        always {
            echo 'Pipeline ejecutado con éxito.'
        }
        success {
            echo 'Las pruebas fueron exitosas.'
        }
        failure {
            echo 'Hubo un error en el pipeline.'
        }
    }
}
