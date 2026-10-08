from sqlalchemy import create_engine
from sqlalchemy.engine import URL


db_user = 'root'
db_pass = 'Change@123456'
db_host = 'localhost'
db_port = 3306
db_name = 'RETAILS_ETL'


connection_url = URL.create(
    drivername='mysql+pymysql',
    username=db_user,
    password=db_pass,
    host=db_host,
    port=db_port,
    database=db_name
)

engine = create_engine(connection_url)

try:
    with engine.connect() as connection:
        print("MySQL connection successful!")

except Exception as e:
    print("MySQL connection failed:")
    print(e)