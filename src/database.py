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
    