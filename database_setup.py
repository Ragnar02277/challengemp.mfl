from sqlalchemy import create_engine, Table, Column, Integer, String, Enum, ForeignKey, MetaData

import config

def crear_base_datos():
    db_url = f"mysql+mysqlconnector://{config.DB_USERNAME}:{config.DB_PASSWORD}@{config.DB_HOST}/{config.DB_NAME}"
    engine = create_engine(db_url, echo=True)
    metadata = MetaData()

    # Definir las tablas
    manager_table = Table('Manager', metadata,
        Column('id_manager', Integer, primary_key=True, autoincrement=True),
        Column('name', String(255), nullable=False),
        Column('email', String(255), nullable=False, unique=True)
    )

    owner_table = Table('Owner', metadata,
        Column('id_owner', Integer, primary_key=True, autoincrement=True),
        Column('name', String(255), nullable=False),
        Column('manager_id', Integer, ForeignKey('Manager.id_manager'))
    )

    database_info_table = Table('DatabaseInfo', metadata,
        Column('id_database', Integer, primary_key=True, autoincrement=True),
        Column('name', String(255), nullable=False),
        Column('classification', Enum('High', 'Medium', 'Low'), nullable=False),
        Column('owner_id', Integer, ForeignKey('Owner.id_owner'))
    )

    # Crear las tablas en la base de datos
    metadata.create_all(engine)

if __name__ == "__main__":
    crear_base_datos()
