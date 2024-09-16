
import psycopg2
import datetime

from psycopg2 import Error, InterfaceError
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

from config.config import config

class DataBase():
    
    connection = psycopg2.connect(
        host=config.POSTGRESQL_HOST.get_secret_value(),
        database=config.POSTGRESQL_DATABASE.get_secret_value(),
        user=config.POSTGRESQL_USER.get_secret_value(),
        password=config.POSTGRESQL_PASSWORD.get_secret_value(),
        port = config.POSTGRESQL_PORT.get_secret_value()
    )
    
    cursor = connection.cursor()

    async def sql_users_add(self, id_users, fname, lname, tname):
        
        try:
            with self.connection as connect:
                with connect.cursor() as cursor:
                    date_users = datetime.datetime.today()
                    
                    add_users = f"INSERT INTO public.meeting_place_users (id_users, first_name, last_name, tg_name, date_action_last) VALUES ({id_users}, '{fname}', '{lname}', '{tname}', '{date_users}');"
                    cursor.execute(add_users)
                    connect.commit()
            
            return True
            
        except (InterfaceError, Error) as error:
            print(error, "Ошибка!", id_users)
            
            
    async def sql_users_check(self, id_users, fname, lname, uname):

        try:
            with self.connection as connect:
                with connect.cursor() as cursor:
                    check_users = f"SELECT id_users FROM public.meeting_place_users WHERE id_users = {id_users}"
                    cursor.execute(check_users)
                    users_check = cursor.fetchall()
                    self.connection.commit()

                    try:
                        if users_check[0][0]:
                            return True
                    except:
                        print("Добавление нового пользователя", id_users)
        except (InterfaceError, Error) as error:
            print(error, "Ошибка!", connect.status, id_users)
            
        await DataBase.sql_users_add(DataBase, id_users, fname, lname, uname)