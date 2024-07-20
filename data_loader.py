import json
import pandas as pd
import config


def cargar_datos_json(json_file):
    """
    Carga los datos desde un archivo JSON.

    Args:
        json_file (str): Ruta al archivo JSON.

    Returns:
        dict: Datos cargados desde el archivo JSON.
    """
    with open(json_file, 'r') as file:
        datos_json = json.load(file)
    return datos_json


def cargar_datos_csv(csv_file):
    """
    Carga los datos desde un archivo CSV.

    Args:
        csv_file (str): Ruta al archivo CSV.

    Returns:
        DataFrame: Datos cargados desde el archivo CSV.
    """
    datos_csv = pd.read_csv(csv_file)
    return datos_csv


def cargar_datos():
    """
    Carga los datos desde los archivos JSON y CSV especificados en config.py.

    Returns:
        tuple: (datos_json, datos_csv)
    """
    datos_json = cargar_datos_json(config.JSON_FILE)
    datos_csv = cargar_datos_csv(config.CSV_FILE)
    return datos_json, datos_csv
