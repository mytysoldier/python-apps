from orator import DatabaseManager, Schema, Model

DATABASES = {
    "postgres": {
        "driver": "postgres",
        "host": "localhost",
        "database": "graphql_sample_db",
        "user": "user",
        "password": "password",
        "prefix": "",
        "port": 5432,
    }
}

db = DatabaseManager(DATABASES)
schma = Schema(db)
Model.set_connection_resolver(db)
