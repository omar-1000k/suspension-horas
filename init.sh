# Construir la imagen
docker build -t sustension-horas .

# crear contenedor con la imagen de sustension-horas y colocar un nombre de contenedor
docker run -p 8501:8501 sustension-horas --name sustension-horas

#detener el contenedor
docker stop sustension-horas

# ejecutar el aerchivo docker-compose.yml
docker-compose up -d

# desactivar el docker-compose y eliminar la imagen de sustension-horas
docker compose down --rmi all

export $(grep -v '^#' .env | xargs)

 # Eliinar el entorno virtual
rm -rf venv

# crear el entorno virtual con uv 
uv venv venv --python=3.13

# activar el entorno virtual
source venv/bin/activate
# instalar las dependencias
uv pip install -r requirements.txt

# desu¿instalar todas los modulos de uv
uv pip freeze | xargs uv pip uninstall

#mostrar puertos abiertos en macos
lsof -i -P | grep LISTEN
# mostrar puertos abiertos en linux
netstat -tuln

# La siguiente linea de comado es para construir una imagen de docker con una aquitectura amd64
# A. Crear un builder multi-arquitectura
docker buildx create --name multiarch-builder --use
docker buildx inspect --bootstrap

# B. Construir la imagen multi-arquitectura y exportarla a un archivo tar, este metodo no crea la imagen en el docker local
docker buildx build \
--platform linux/amd64 \
-t suspension-horas:1.0-amd64 \
-o type=docker,dest=suspension-horas-amd64.tar .

#B.1 Construye la imagen multi-arquitectura pero no la exporta a un archivo tar
docker buildx build \
--platform linux/amd64 \
-t suspension-horas:1.0-amd64 \
--load .

# C. Cargar la imagen en el docker local
docker inspect suspension-horas:1.0-amd64 | grep Architecture