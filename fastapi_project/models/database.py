import databases

DB_USER = "temp_db"
DB_PASSWORD = "temp_db"
DB_HOST = "127.0.0.1"
DB_NAME = "temp_db"
SQLALCHEMY_DATABASE_URL = (
    f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:5432/{DB_NAME}"
)
# создаем объект database, который будет использоваться для выполнения запросов
database = databases.Database(SQLALCHEMY_DATABASE_URL)