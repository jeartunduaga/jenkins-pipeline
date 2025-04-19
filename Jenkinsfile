pipeline {
    agent any  // Ejecutar en cualquier nodo disponible de Jenkins

    stages {
        stage('Preparación') {
            steps {
                script {
                    echo 'Instalando dependencias...'
                    
                    // Crear el entorno virtual
                    sh 'python3 -m venv venv'

                    // Activar el entorno virtual y luego instalar las dependencias usando bash
                    sh 'bash -c "source venv/bin/activate && pip install -r requirements.txt"'
                }
            }
        }

        stage('Ejecutar Pruebas') {
            steps {
                script {
                    echo 'Ejecutando pruebas...'
                    
                    // Ejecutar las pruebas con unittest dentro del entorno virtual
                    sh 'bash -c "source venv/bin/activate && python3 -m unittest test_nomina.py"'
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
