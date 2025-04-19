pipeline {
    agent any  // Ejecutar en cualquier nodo disponible de Jenkins

    stages {
        stage('Preparación') {
            steps {
                script {
                    echo 'Instalando dependencias...'

                    // Crear un entorno virtual
                    sh 'python3 -m venv venv'  // Crear un entorno virtual llamado 'venv'

                    // Activar el entorno virtual y luego instalar las dependencias
                    sh 'source venv/bin/activate && pip install -r requirements.txt'  // Para Linux/Mac
                }
            }
        }

        stage('Ejecutar Pruebas') {
            steps {
                script {
                    echo 'Ejecutando pruebas...'

                    // Activar el entorno virtual y ejecutar las pruebas con unittest
                    sh 'source venv/bin/activate && python3 -m unittest test_nomina.py'
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
