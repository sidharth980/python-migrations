from database import database
from db_sql import db_sql
from migrations import migrations


db = database()
test = db_sql(db)

mig = migrations()
connection = test.connect()
test.test_connection(connection)
for version in mig.get_migration_files():
    mig.store_migration_version_and_run_commands(connection,version)
test.close(connection)
