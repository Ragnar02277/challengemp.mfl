Instrucciones para Instalar y Ejecutar el Proyecto
1. Requisitos Previos
Antes de comenzar, asegúrate de tener instalados los siguientes programas en tu máquina:

Python: Asegúrate de tener Python 3.8 o superior instalado. Puedes descargarlo desde python.org.
MySQL: Asegúrate de tener MySQL 8.0 o superior instalado. Puedes descargarlo desde mysql.com.
Git: Si aún no lo tienes, puedes instalar Git desde git-scm.com.
2. Clonar el Repositorio
Abrir la Terminal o Línea de Comandos.

Clonar el Repositorio:

bash
Copy code
git clone https://github.com/tu_usuario/tu_repositorio.git
Reemplaza tu_usuario y tu_repositorio con el nombre de usuario de GitHub y el nombre del repositorio.

Navegar al Directorio del Proyecto:

bash
Copy code
cd tu_repositorio
3. Configurar el Entorno Virtual
Crear un Entorno Virtual:

bash
Copy code
python -m venv venv
Activar el Entorno Virtual:

Windows:
bash
Copy code
venv\Scripts\activate
macOS/Linux:
bash
Copy code
source venv/bin/activate
4. Instalar Dependencias
Instalar Paquetes Necesarios:

bash
Copy code
pip install -r requirements.txt
Asegúrate de que requirements.txt contenga las siguientes librerías, o ajusta el archivo según sea necesario:

Copy code
mysql-connector-python
yagmail
python-dotenv
5. Configurar el Archivo .env
Crear un Archivo .env en la raíz del proyecto con el siguiente contenido:

env
Copy code
DB_HOST=localhost
DB_USER=tu_usuario_db
DB_PASSWORD=tu_contraseña_db
DB_NAME=MyDatabase

EMAIL_USER=tu_email@gmail.com
EMAIL_PASSWORD=tu_contraseña_email
Reemplaza tu_usuario_db, tu_contraseña_db, tu_email@gmail.com, y tu_contraseña_email con tus credenciales de base de datos y correo electrónico.

6. Crear la Base de Datos y Tablas
Abrir MySQL Workbench o tu cliente de base de datos preferido.

Ejecutar el Script SQL para crear la base de datos y tablas. Guarda el siguiente contenido en un archivo schema.sql y ejecútalo:

sql
Copy code
-- Create the database (adjust the name as per your preference)
CREATE DATABASE IF NOT EXISTS MyDatabase;
USE MyDatabase;

-- Create the Manager table
CREATE TABLE Manager (
    id_manager INT PRIMARY KEY auto_increment,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE
);

-- Create the Owner table
CREATE TABLE Owner (
    id_owner INT PRIMARY KEY auto_increment,
    name VARCHAR(255) NOT NULL,
    manager_id INT,
    FOREIGN KEY (manager_id) REFERENCES Manager(id_manager)
);

-- Create the DatabaseInfo table
CREATE TABLE DatabaseInfo (
    id_database INT PRIMARY KEY auto_increment,
    name VARCHAR(255) NOT NULL,
    classification ENUM('High', 'Medium', 'Low') NOT NULL,
    owner_id INT,
    FOREIGN KEY (owner_id) REFERENCES Owner(id_owner)
);
7. Preparar los Archivos CSV
Crear los Archivos CSV en la raíz del proyecto con las siguientes estructuras:

managers.csv:

csv
Copy code
id_manager,name,email
1,Manager1,manager1@example.com
2,Manager2,manager2@example.com
3,Manager3,manager3@example.com
owners.csv:

csv
Copy code
id_owner,name,manager_id
1,Owner1,1
2,Owner2,2
3,Owner3,3
database_info.csv:

csv
Copy code
id_database,name,classification,owner_id
1,Database1,High,1
2,Database2,Medium,2
3,Database3,Low,3
8. Ejecutar el Proyecto
Ejecutar el Script de Carga de Datos:

bash
Copy code
python data_loader.py
Este script cargará los datos desde los archivos CSV a la base de datos y enviará correos electrónicos a los gerentes para la validación de las clasificaciones.

9. Verificar el Funcionamiento
Verificar los Datos en la Base de Datos:

Asegúrate de que los datos se hayan cargado correctamente en las tablas de la base de datos utilizando tu cliente MySQL.
Revisar los Correos Electrónicos Enviados:

Verifica que los correos electrónicos de solicitud de validación hayan sido enviados a los gerentes.
