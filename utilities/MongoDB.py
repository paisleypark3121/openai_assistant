import os
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv() 

CONNECTION_STRING=os.environ.get('CONNECTION_STRING')
DATABASE_NAME=os.environ.get('DATABASE_NAME')

class MongoDB:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(MongoDB, cls).__new__(cls, *args, **kwargs)
            cls._instance.connection = MongoClient(
                CONNECTION_STRING,
                maxPoolSize=50,
            )
            cls._instance.db = cls._instance.connection[DATABASE_NAME]
        return cls._instance

    @classmethod
    def get_db(cls):
        return cls._instance.db

MongoDB = MongoDB()