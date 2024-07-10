from database import database
import os


class migrations:
    def __init__(self) -> None:
        self.db = database()
        self.migrations_dir = 'version'

    def get_migration_files(self):
        migration_files = [f.split(".sql")[0] for f in os.listdir(self.migrations_dir) if os.path.isfile(os.path.join(self.migrations_dir, f))]
        migration_files.sort()  
        return migration_files

    def store_migration_version_and_run_commands(self,connection, version):

        with connection.cursor() as cur:

            cur.execute("""
            CREATE TABLE IF NOT EXISTS migrations (
                version VARCHAR PRIMARY KEY
            )
            """)
            
            cur.execute("SELECT version FROM migrations WHERE version = %s", (version,))
            if cur.fetchone():
                print(f"Migration {version} has already been applied.")
                return False


            with open(os.path.join(self.migrations_dir,version+".sql"), 'r') as file:
                sql_commands = file.read()
                cur.execute(sql_commands)


            cur.execute("INSERT INTO migrations (version) VALUES (%s)", (version,))
            connection.commit()
            print(f"Migration {version} applied")
        return True
    