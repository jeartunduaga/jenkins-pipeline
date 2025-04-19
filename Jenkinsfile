pipeline {
    agent any  // Ejecutar en cualquier nodo disponible de Jenkins

    stages {
        stage('Preparación') {
            steps {
                script {
                    echo 'Preparando el entorno...'
                    // Aquí puedes agregar cualquier preparación que necesite el entorno (como instalación de dependencias)
                    sh 'pip install -r requirements.txt'  // Si tienes un archivo de dependencias
                }
            }
        }

        stage('Ejecutar Pruebas') {
            steps {
                script {
                    echo 'Ejecutando pruebas...'
                    // Ejecutamos las pruebas con pytest o unittest (según como hayas configurado las pruebas)
                    sh 'python -m unittest test_nomina.py'
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
