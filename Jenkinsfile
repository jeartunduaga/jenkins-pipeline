pipeline {
    agent any  // Ejecutar en cualquier nodo disponible de Jenkins

    stages {
        stage('Ejecutar Pruebas') {
            steps {
                script {
                    echo 'Ejecutando pruebas...'
                    // Ejecutamos las pruebas con unittest (o pytest si lo prefieres)
                    sh 'python3 -m unittest test_nomina.py'
                }
            }
        }

        stage('Resultados') {
            steps {
                script {
                    echo 'Generando resultados...'
                    // Aquí puedes agregar cualquier acción adicional (como guardar los resultados)
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
