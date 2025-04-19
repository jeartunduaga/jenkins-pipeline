pipeline {
    agent any  // Ejecutar en cualquier nodo disponible de Jenkins

    stages {
        stage('Preparación') {
            steps {
                script {
                    echo 'Instalando dependencias...'
                    // Instalamos las dependencias necesarias antes de ejecutar las pruebas
                    sh 'pip install -r requirements.txt'  // Asegúrate de que xmlrunner esté en requirements.txt
                }
            }
        }

        stage('Ejecutar Pruebas') {
            steps {
                script {
                    echo 'Ejecutando pruebas...'
                    // Ejecutamos las pruebas con unittest y generamos el reporte en formato XML
                    sh 'python3 -m unittest test_nomina.py'
                }
            }
        }

        stage('Resultados') {
            steps {
                script {
                    echo 'Generando resultados...'
                    // Archivamos el archivo result.xml como un artefacto para poder visualizarlo
                    archiveArtifacts artifacts: 'result.xml', allowEmptyArchive: true
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
