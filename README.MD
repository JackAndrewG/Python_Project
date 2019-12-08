LEVANTAR SERVIDOR
=================
- Instalar python
- Añadir pip a variables de entorno
- Instalar Django con : 
```
pip install Django
```
- Instalar entorno virtual python: 
```        
pip install virtualenv
```
- Crear entorno virtual en directorio deseado con: 
```
virtualenv env
```
- Activar entorno virtual env/Scripts/ -> activate ó source env/Scripts/activate
- Instalar conector a base de datos y libreria para cargar archivos:
```
pip install django-cymysql
python -m pip install Pillow
```
- Verificar archivo settings: /futbolito/settings.py
```
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
```
- Crear usuario unico en Base de Datos:
```
    ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'root';	<SOLO SI HAY RESCTRICCIONES
    CREATE USER 'AdminFutbolito'@'localhost' IDENTIFIED BY 'futbolito';
    GRANT ALL PRIVILEGES ON * . * TO 'AdminFutbolito'@'localhost';
```

- Dirigirse a ruta de proyecto Python y ejecutar las migraciones de los modelos a la base de datos:
```
    python manage.py migrate (Realiza la creación del sitio admin, tablas, auth_users, etc.)
    python manage.py makemigrations app1
    python manage.py migrate app1
```

- Crear superusuario por consola:
```
python manage.py createsuperuser
```
- Instlación de librerias Django:
```
    pip install django-rest-swagger
    pip install djangorestframework
```

- Correr servidor usando: python runserver 
    _Correr a traves de Ip(configurar en settings):_
```
    python manage.py runserver 0.0.0.0:8000
```

CONFIGURAR SERVIDOR
=================

- Ingresar al sitio de administración de Django: crear usuarios y complejos.
- Dar privilegio is_staff a administradores de complejos
- Crear usuario_final


## Autores ✒️

* **Jimmy Vicente** - *Desarrollo móvil* - [jlvicente](https://github.com/villanuevand)
* **Albert Mora** - *Desarrollo Web* - [albertmora](#fulanito-de-tal)
* **Jackson Guzmán** - *Desarrollo Web*  *Documentación* - [JackAndrewG](https://github.com/JackAndrewG)





