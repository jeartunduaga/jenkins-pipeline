pipeline {
    agent any  // Ejecutar en cualquier nodo disponible de Jenkins

    stages {
        stage('Ejecutar Pruebas') {
            steps {
                script {
                    echo 'Ejecutando pruebas...'
                    // Ejecutar las pruebas con unittest usando xmlrunner y generar los resultados en formato XML
                    sh 'python3 -m unittest test_nomina.py'  // Esto debería generar result.xml
                }
            }
        }

        stage('Resultados') {
            steps {
                script {
                    echo 'Generando resultados...'
                    // Archivar el archivo result.xml como un artefacto para poder visualizarlo
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
