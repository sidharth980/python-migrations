import psycopg2
from psycopg2 import sql

class db_sql:
    def __init__(self,db) -> None:
        self.db = db

    def test_connection(self,connection):
        try:
            print(f"Connecting to {self.db.database} on port {self.db.port} from user {self.db.user} pass {self.db.password}")
            # connection = self.connect()
            cursor = connection.cursor()
            cursor.execute("SELECT version();")
            record = cursor.fetchone()
            print("You are connected to - ", record, "\n")
        except (Exception, psycopg2.Error) as error:
            print("Error while connecting to PostgreSQL", error)
        return cursor,connection

    def close(self,cursor,connection):
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
    def close(self,connection):
        connection.close()
        return True

    def querry(self, table_query):
        new_connection = self.connect()
        new_connection.autocommit = True  
        new_cursor = new_connection.cursor()

        new_cursor.execute(table_query)
        print(f"{table_query} created successfully'")
        new_connection.close()
        new_cursor.close()

    def create_db(self, querry):
        connection = self.connect()
        connection.autocommit = True
        cursor = connection.cursor()
        cursor.execute(sql.SQL(querry))
        print(f"Database created successfully")
        cursor.close()
        connection.close()


