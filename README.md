

## Guía de Uso de la Aplicación de Gestión de PDF

### 1. Instalación y Configuración del Entorno de Desarrollo

1. Asegúrate de tener Python y pip instalados en tu sistema.
2. Clona el repositorio desde GitHub:


git clone <URL_del_repositorio>


3. Navega al directorio del proyecto:


cd gestion_PDF


4. Crea y activa un entorno virtual:


python -m venv venv
# En Windows: venv\Scripts\activate
# En Unix/MacOS: source venv/bin/activate


5. Instala las dependencias:


pip install -r requirements.txt


6. Realiza las migraciones:


python manage.py migrate
```

### 2. Crear un Superusuario y Acceder a la Aplicación

1. Crea un superusuario:


python manage.py createsuperuser
```

Sigue las instrucciones para ingresar un nombre de usuario, correo electrónico y contraseña.

2. Inicia el servidor de desarrollo:


python manage.py runserver


3. Accede al panel de administración: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/). Ingresa con las credenciales del superusuario.

### 3. Agregar Documentos y Visualizar Bandeja de Aprobación

1. Desde el panel de administración, agrega algunos documentos PDF desde la sección "Documentos PDF".
2. Accede a la bandeja de documentos pendientes de aprobación: [http://127.0.0.1:8000/documentos/documentos_pendientes/](http://127.0.0.1:8000/documentos/documentos_pendientes/).
3. Como superusuario, podrás aprobar o rechazar documentos.

### 4. Acceder a la Página Principal y al Perfil de Usuario

1. Visita la página principal: [http://127.0.0.1:8000/](http://127.0.0.1:8000/).
2. Accede a tu perfil de usuario: [http://127.0.0.1:8000/perfil/](http://127.0.0.1:8000/perfil/).

### 5. Agregar Documentos desde la Aplicación

1. Accede a la página de agregar documentos: [http://127.0.0.1:8000/documentos/agregar/](http://127.0.0.1:8000/documentos/agregar/).
2. Completa el formulario y haz clic en "Agregar".

### 6. Eliminar Documentos desde la Aplicación

1. Accede a la lista de documentos: [http://127.0.0.1:8000/documentos/lista/](http://127.0.0.1:8000/documentos/lista/).
2. Haz clic en "Eliminar" junto al documento que deseas eliminar.

### 7. Cerrar Sesión

1. Accede a la página de cierre de sesión: [http://127.0.0.1:8000/accounts/logout/](http://127.0.0.1:8000/accounts/logout/).
2. Haz clic en "Sign Out".

### 8. Cierre del Entorno de Desarrollo

1. Detén el servidor de desarrollo presionando `Ctrl+C`.
2. Desactiva el entorno virtual:

- En Windows:


deactivate


- En Unix o MacOS:

```bash
source deactivate
```

