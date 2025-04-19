pipeline {
    agent any  // Ejecutar en cualquier nodo disponible de Jenkins

    stages {
        stage('Ejecutar Pruebas') {
            steps {
                script {
                    echo 'Ejecutando pruebas...'

                    // Ejecutamos las pruebas con xmlrunner para generar resultados en formato XML
                    sh 'python3 -m xmlrunner discover -s . -p "test_nomina.py" > result.xml'
                }
            }
        }

        stage('Archivar Resultados') {
            steps {
                script {
                    echo 'Archivando resultados...'
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
