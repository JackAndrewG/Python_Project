-----LEVANTAR SERVIDOR ----
- Instalar python
- Añadir pip a variables de entorno
- Instalar Django con : pip install Django
- Instalar entorno virtual python: pip install virtualenv
- Crear entorno virtual en directorio deseado con: virtualenv env
- Activar entorno virtual env/Scripts/ -> activate ó source env/Scripts/activate
- Instalar conector a base de datos: - pip install cymysql
- Verificar archivo settings: /futbolito/settings.py
    DATABASES = {
            'default': {
                'ENGINE': 'mysql_cymysql',
                'NAME': 'futbolitoDB',
                'USER': 'AdminFutbolito',
                'PASSWORD': 'futbolito',
                'HOST': 'localhost',
                'PORT': '3306',
            }
        }

- Crear usuario unico en Base de Datos:
    CREATE USER 'AdminFutbolito'@'localhost' IDENTIFIED BY 'futbolito';
    GRANT ALL PRIVILEGES ON * . * TO 'AdminFutbolito'@'localhost';

-Dirigirse a ruta de proyecto Python y ejecutar las migraciones de los modelos a la base de datos:
    python manage.py makemigrations app1
    python manage.py migrate app1

- Correr servidor usando: python runserver 

