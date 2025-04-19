pipeline {
    agent any  // Ejecutar en cualquier nodo disponible de Jenkins

    stages {
        stage('Ejecutar Pruebas') {
            steps {
                script {
                    echo 'Ejecutando pruebas...'
                    // Ejecutamos las pruebas con unittest y generamos el archivo result.xml
                    sh 'python3 -m unittest test_nomina.py --xml result.xml'
                }
            }
        }

        stage('Archivar Resultados') {
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
            junit '**/result.xml'  // Publica el informe de pruebas JUnit para procesar el archivo result.xml
        }
        failure {
            echo 'Hubo un error en el pipeline.'
        }
    }
}
