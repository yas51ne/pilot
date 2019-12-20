import os
from ast import literal_eval


# config.py
class Config:

    def __init__(self):
        self.DATABASE_HOST = os.environ.get("DATABASE_HOST", "db")
        self.DATABASE_PORT = int(os.environ.get("DATABASE_PORT", 5432))
        self.DATABASE_NAME = os.environ.get("DATABASE_NAME", "postgres")
        self.DATABASE_USER = os.environ.get("DATABASE_USER", "postgres")
        self.DATABASE_PASSWORD = os.environ.get("DATABASE_PASSWORD", "")
        self.SERVER_URL = os.environ.get("SERVER_URL", "pilot-frontend.pilot.svc.cluster.local")
    def __str__(self) -> str:
        return str(self.__dict__)