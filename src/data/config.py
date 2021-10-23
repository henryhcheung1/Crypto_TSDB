import os

class Config:
        
    DB_USER = 'postgres'
    DB_PASS = 'postgres'
    DB_HOST = 'localhost'
    DB_PORT = '5432'
    DB_NAME = 'crypto'
    API_KEY = os.environ['API_KEY']

# class Production:
#     pass