import psycopg2
from psycopg2 import sql
import os
from dotenv import load_dotenv

class database:
    def __init__(self,host="localhost",port = 5432) -> None:
        load_dotenv()
        self.user = os.getenv("DB_USER")
        self.password = os.getenv("DB_PASSWORD")
        self.database = os.getenv("DB_NAME")
        self.port = port
        self.host = host
    
    

class test_db:
    def __init__(self) -> None:
        self.db = database()

    def test_connection(self):
        try:
            print(f"Connecting to {self.db.database} on port {self.db.port} from user {self.db.user} pass {self.db.password}")
            connection = self.connect()
            cursor = connection.cursor()
            cursor.execute("SELECT version();")
            record = cursor.fetchone()
            print("You are connected to - ", record, "\n")
        except (Exception, psycopg2.Error) as error:
            print("Error while connecting to PostgreSQL", error)
        finally:
            if connection:
                cursor.close()
                connection.close()
                print("PostgreSQL connection is closed")

    def connect(self):
        connection = psycopg2.connect(
                user=self.db.user,
                password=self.db.password,
                host=self.db.host,
                port=self.db.port,
                database=self.db.database
            )
        
        return connection

    def create_database_and_table(self,schema,querry):
        new_db_name = schema
        table_creation_query = querry

        try:
            connection, cursor = self.create_db(new_db_name)
            cursor.close()
            connection.close()

            new_connection, new_cursor = self.create_table(table_creation_query)
            new_connection.close()
            new_cursor.close()

        except Exception as error:
            print(f"Error: {error}")


    def create_table(self, table_creation_query):
        new_connection = self.connect()
        new_connection.autocommit = True  
        new_cursor = new_connection.cursor()

        new_cursor.execute(table_creation_query)
        print("Table 'items' created successfully'")
        return new_connection,new_cursor

    def create_db(self, new_db_name):
        connection = self.connect()
        connection.autocommit = True

        cursor = connection.cursor()

        cursor.execute(sql.SQL("CREATE DATABASE {}").format(
                sql.Identifier(new_db_name))
            )
        print(f"Database '{new_db_name}' created successfully")
        return connection,cursor

tester = test_db()
tester.test_connection()

new_db_name = "CREATE DATABASE mydatabase"
table_creation_query = """
CREATE TABLE items (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    price NUMERIC(10, 2) NOT NULL
);
"""
tester.create_database_and_table(new_db_name,table_creation_query)