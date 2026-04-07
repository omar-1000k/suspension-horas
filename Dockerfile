FROM python:3.13-alpine

# Permitir que las declaraciones y los mensajes de registro aparezcan inmediatamente en los registros de Knative
# ENV PYTHONUNBUFFERED True

EXPOSE 8501

# Copie el código local a la imagen del contenedor.
WORKDIR /
COPY requirements.txt /
COPY Puebla.jpg /
COPY login.py /
COPY app/ /app/
# COPY .streamlit/ /.streamlit/

# crear un archivo requirements.txt vacío para que la imagen de Docker pueda ser descargada correctamente
# Crear un archivo __init__.py vacío para que app sea reconocido como un paquete Python
# Instalar bash en alpine
RUN touch /app/__init__.py \
    && pip install -r requirements.txt \
    && apk add --no-cache bash 


# El tiempo de espera se establece en 0 para deshabilitar los tiempos de espera de los workes y permitir que Cloud Run maneje el escalado de instancias.
# CMD streamlit run --server.port 8501  --server.address=0.0.0.0 login.py
ENTRYPOINT ["streamlit", "run", "login.py", "--server.port=8501", "--server.address=0.0.0.0"]