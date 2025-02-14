import psycopg2 as pg
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

def get_db_connection():
    # Load environment variables from .env
    load_dotenv()

    # Fetch variables
    DATABASE_URL = os.getenv("DATABASE_URL")
    engine = create_engine(DATABASE_URL)  
    
    with engine.connect() as connection:
        print('Conexão estabelecida')
    return engine