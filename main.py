import data_processor

if __name__ == "__main__":
    json_file = config.JSON_FILE
    csv_file = config.CSV_FILE
    db_file = 'my_database.db'
    data_processor.procesar_datos(json_file, csv_file, db_file)
