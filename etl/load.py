from sqlalchemy import create_engine
from sqlalchemy.engine import URL


def load_data(fact_sales, dim_store, dim_date, dim_feature):

    db_name = 'RETAILS_ETL'
    db_host = 'localhost'
    db_port = 3306
    db_pass = 'Change@123456'
    db_user = 'root'

    connection_url = URL.create(
        drivername='mysql+pymysql',
        username=db_user,
        password=db_pass,
        host=db_host,
        port=db_port,
        database=db_name
    )

    engine = create_engine(connection_url)

    dim_store.to_sql('dim_store',
                     engine,
                     if_exists='replace',
                     index=False)

    dim_date.to_sql('dim_date',
                     engine,
                     if_exists='replace',
                     index=False)

    dim_feature.to_sql('dim_feature',
                       engine,
                       if_exists='replace',
                       index=False)

    fact_sales.to_sql('fact_sales',
                      engine,
                      if_exists='replace',
                      index=False)

    print('Data loaded to MySQL successfully')

