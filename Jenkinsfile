pipeline {
    agent any  // Ejecutar en cualquier nodo disponible de Jenkins

    stages {
        stage('Preparación') {
            steps {
                script {
                    echo 'Preparando el entorno...'
                    // Crear un entorno virtual
                    sh 'python3 -m venv venv'  // Crea un entorno virtual en la carpeta 'venv'
                    // Activar el entorno virtual y luego instalar las dependencias
                    sh '. venv/bin/activate && pip install -r requirements.txt'  // Activamos el entorno y ejecutamos pip
                }
            }
        }

        stage('Ejecutar Pruebas') {
            steps {
                script {
                    echo 'Ejecutando pruebas...'
                    // Ejecutamos las pruebas con pytest o unittest (según como hayas configurado las pruebas)
                    sh '. venv/bin/activate && python -m unittest test_nomina.py'  // Usamos el entorno virtual para ejecutar las pruebas
                }
            }
        }

        stage('Resultados') {
            steps {
                script {
                    echo 'Generando resultados...'
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
