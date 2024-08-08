#Si tienes versiones anteriores de Docker instaladas, desinstálalas primero:
sudo dnf remove docker docker-client docker-client-latest docker-common docker-latest docker-latest-logrotate docker-logrotate docker-selinux docker-engine-selinux docker-engine

#Instala los paquetes necesarios para habilitar el repositorio Docker:
sudo dnf install -y yum-utils device-mapper-persistent-data lvm2

#Añade el repositorio oficial de Docker:
sudo yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo

#Instala Docker utilizando el comando dnf:
sudo dnf install -y docker-ce docker-ce-cli containerd.io docker-compose

#Inicia el servicio Docker y habilítalo para que se inicie automáticamente al arrancar el sistema:
sudo systemctl start docker
sudo systemctl enable docker

#Verifica que Docker se haya instalado correctamente ejecutando el comando:
sudo docker run hello-world

#Para ejecutar comandos Docker sin sudo, añade tu usuario al grupo Docker:
sudo usermod -aG docker $USER

#Instalar Docker Compose
sudo curl -L "https://github.com/docker/compose/releases/download/v2.20.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose

#Aplica permisos ejecutables al binario de Docker Compose:
sudo chmod +x /usr/local/bin/docker-compose

#Verifica la instalación de Docker Compose:
docker-compose --version

#Puedes verificar la versión de Docker instalada con el siguiente comando:
docker --version

#Cambiar permisos del socket (si es necesario):
sudo chmod 666 /var/run/docker.sock