# Usamos la imagen oficial de Jenkins LTS
FROM jenkins/jenkins:lts

# Cambiamos el usuario a root para instalar dependencias
USER root

# Actualizamos los repositorios y instalamos Python y pip
RUN apt-get update && apt-get install -y python3 python3-pip python3-venv

# Creamos un entorno virtual en el directorio /var/jenkins_home/venv
RUN python3 -m venv /var/jenkins_home/venv

# Activamos el entorno virtual y luego instalamos las dependencias
RUN /var/jenkins_home/venv/bin/pip install --upgrade pip
COPY requirements.txt /var/jenkins_home/requirements.txt
RUN /var/jenkins_home/venv/bin/pip install -r /var/jenkins_home/requirements.txt

# Cambiamos de vuelta a usuario 'jenkins' después de la instalación
USER jenkins

# Exponemos los puertos necesarios
EXPOSE 8080
EXPOSE 50000
