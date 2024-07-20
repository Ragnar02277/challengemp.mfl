from sqlalchemy import create_engine, Table, Column, Integer, String, Enum, ForeignKey, MetaData, select
import yagmail
import pandas as pd
import json
import config


def manejar_campos_incompletos(json_data):
    for registro in json_data:
        if 'clasificacion' not in registro:
            registro['clasificacion'] = 'Medium'
    return json_data


def obtener_url_mysql():
    return f"mysql+mysqlconnector://{config.DB_USERNAME}:{config.DB_PASSWORD}@{config.DB_HOST}/{config.DB_NAME}"


def guardar_en_base_datos(json_data, csv_data, db_url):
    engine = create_engine(db_url, echo=True)
    metadata = MetaData()

    # Definir las tablas
    manager_table = Table('Manager', metadata, autoload_with=engine)
    owner_table = Table('Owner', metadata, autoload_with=engine)
    database_info_table = Table('DatabaseInfo', metadata, autoload_with=engine)

    with engine.connect() as conn:
        # Insertar managers desde el CSV
        for _, row in csv_data.iterrows():
            manager_email = row['user_manager']
            manager_exists = conn.execute(
                select([manager_table.c.id_manager]).where(manager_table.c.email == manager_email)).fetchone()
            if not manager_exists:
                conn.execute(manager_table.insert().values(name=f"Manager {manager_email}", email=manager_email))

        # Insertar owners desde el CSV
        for _, row in csv_data.iterrows():
            owner_email = row['user_id']
            manager_email = row['user_manager']
            manager_id = \
            conn.execute(select([manager_table.c.id_manager]).where(manager_table.c.email == manager_email)).fetchone()[
                0]
            owner_exists = conn.execute(
                select([owner_table.c.id_owner]).where(owner_table.c.name == f"Owner {owner_email}")).fetchone()
            if not owner_exists:
                conn.execute(owner_table.insert().values(name=f"Owner {owner_email}", manager_id=manager_id))

        # Insertar información de base de datos
        for registro in json_data:
            nombre_base = registro['nombre']
            clasificacion = registro['clasificacion']
            email_owner = registro['email_owner']
            owner_id = conn.execute(
                select([owner_table.c.id_owner]).where(owner_table.c.name == f"Owner {email_owner}")).fetchone()[0]

            conn.execute(database_info_table.insert().values(
                name=nombre_base,
                classification=clasificacion,
                owner_id=owner_id
            ))

            if clasificacion == 'High':
                enviar_email_aprobacion(nombre_base, manager_email)


def procesar_datos(json_file, csv_file, db_file):
    json_data = json.load(open(json_file))
    csv_data = pd.read_csv(csv_file)
    json_data = manejar_campos_incompletos(json_data)
    db_url = obtener_url_mysql()
    guardar_en_base_datos(json_data, csv_data, db_url)


def enviar_email_aprobacion(nombre_base, manager_email):
    asunto = f'Reválida de Clasificación: {nombre_base}'
    cuerpo = f'Se requiere su aprobación para la clasificación de la base de datos {nombre_base}.'

    yag = yagmail.SMTP(config.EMAIL_USERNAME, config.EMAIL_PASSWORD)
    yag.send(manager_email, asunto, cuerpo)
