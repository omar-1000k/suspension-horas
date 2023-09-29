FROM python:3.11.5

# Permitir que las declaraciones y los mensajes de registro aparezcan inmediatamente en los registros de Knative
ENV PYTHONUNBUFFERED True

EXPOSE 8080

# Copie el código local a la imagen del contenedor.
ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . ./

# Instalar dependencias de producción.
RUN pip install -r requirements.txt

# Ejecute el servicio web al iniciar el contenedor. Aquí usamos el servidor web gunicorn 
# con un proceso de trabajo y 8 subprocesos. 
# Para entornos con múltiples núcleos de CPU, aumente la cantidad de workers 
# para que sea igual a los núcleos disponibles. 
# El tiempo de espera se establece en 0 para deshabilitar los tiempos de espera de los workes y permitir que Cloud Run maneje el escalado de instancias.
CMD streamlit run --server.port 8080 --server.host=0.0.0.0 streamlit_app.py