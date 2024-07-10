import psycopg2
from psycopg2 import sql
import os

db_info = {
    "user" : os.getenv("DB_USER"),
    "password" : os.getenv("DB_PASSWORD"),
    "database" : os.getenv("DB_NAME"),
    "port" : 5432
}


def test_connection():
    try:
        # print(f"Connecting to {db_info.database} on port {db_info.port}")
        connection = psycopg2.connect(
            user="sampleuser",
            password="samplepass",
            host="localhost",
            port="5432",
            database="sampledb"
        )
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

def create_database():
    new_db_name = "mydatabase"
    table_creation_query = """
    CREATE TABLE items (
        id SERIAL PRIMARY KEY,
        name TEXT NOT NULL,
        price NUMERIC(10, 2) NOT NULL
    );
    """

    # Connect to the PostgreSQL server
    try:
        # Step 1: Connect to the default database to create a new database
        connection = psycopg2.connect(
            user="sampleuser",
            password="samplepass",
            host="localhost",
            port="5432",
            database="sampledb"
        )
        connection.autocommit = True  # Enable autocommit

        # Create a cursor object
        cursor = connection.cursor()

        # Create the new database
        cursor.execute(sql.SQL("CREATE DATABASE {}").format(
            sql.Identifier(new_db_name))
        )
        print(f"Database '{new_db_name}' created successfully")

        # Close the initial connection
        cursor.close()
        connection.close()

        # Step 2: Connect to the newly created database to create the table
        new_connection = psycopg2.connect(
            user="sampleuser",
            password="samplepass",
            host="localhost",
            port="5432",
            database="sampledb"
        )
        new_connection.autocommit = True  # Enable autocommit
        new_cursor = new_connection.cursor()

        # Create the table
        new_cursor.execute(table_creation_query)
        print(f"Table 'items' created successfully in database '{new_db_name}'")

    except Exception as error:
        print(f"Error: {error}")

    finally:
        # Close the new cursor and connection
        if 'new_cursor' in locals() and new_cursor:
            new_cursor.close()
        if 'new_connection' in locals() and new_connection:
            new_connection.close()
        if 'cursor' in locals() and cursor:
            cursor.close()
        if 'connection' in locals() and connection:
            connection.close()


test_connection()