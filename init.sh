# Construir la imagen
docker build -t sustension-horas .

# crear contenedor con la imagen de sustension-horas y colocar un nombre de contenedor
docker run -p 8501:8501 sustension-horas --name sustension-horas

#detener el contenedor
docker stop sustension-horas

# ejecutar el aerchivo docker-compose.yml
docker-compose up -d

# desactivar el docker-compose
docker-compose down


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