# Construir la imagen
docker build -t sustension-horas .

# crear contenedor con la imagen de sustension-horas y colocar un nombre de contenedor
docker run -p 8501:8501 sustension-horas --name sustension-horas

#detener el contenedor
docker stop sustension-horas


