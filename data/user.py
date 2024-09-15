
import psycopg2
import datetime

from psycopg2 import Error
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

from config.config import config

async def sql_users_add(id_users, fname, lname, tname):
    
    try:
        # Подключение к существующей базе данных
        connection = psycopg2.connect(
        host=config.POSTGRESQL_HOST.get_secret_value(),
        database=config.POSTGRESQL_DATABASE.get_secret_value(),
        user=config.POSTGRESQL_USER.get_secret_value(),
        password=config.POSTGRESQL_PASSWORD.get_secret_value(),
        port = config.POSTGRESQL_PORT.get_secret_value()
        )
        connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        # Курсор для выполнения операций с базой данных
        cursor = connection.cursor()
        
        date_users = datetime.datetime.today()
        
        add_users = f"INSERT INTO public.users (id_users, first_name, last_name, tg_name, date_action_last, balance, status_pay, status_tg, id_record) VALUES ({id_users}, '{fname}', '{lname}', '{tname}', '{date_users}', {0}, 'NO', 'NO', {1});"
        cursor.execute(add_users)
        
        connection.commit()
        
    finally:
        if connection:
            cursor.close()
            connection.close()
