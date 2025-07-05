# Usa una imagen base de Python 3.11 (estable)
FROM python:3.11-slim

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia los archivos del proyecto al contenedor
COPY . /app

# Actualiza pip y setuptools
RUN pip install --upgrade pip setuptools

# Instala dependencias
RUN pip install -r requirements.txt

# Expone el puerto (Render usará esto)
EXPOSE 8000

# Comando para ejecutar el servidor (ajústalo si usas algo diferente a Django)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
