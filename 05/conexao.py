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

    # # Connect to the database
    # try:
    #     connection = pg.connect(DATABASE_URL
    #         # user=url.username,
    #         # password=url.password,
    #         # host=url.hostname,
    #         # port=url.port,
    #         # dbname=url.path[1:]
    #     )
    #     print(DATABASE_URL)
    #     return connection
    # except Exception as e:
    #     print(f"Failed to connect: {e}")
    #     return None

# # Load environment variables from .env
# load_dotenv()

# # Fetch variables
# USER = os.getenv("postgres")
# PASSWORD = os.getenv("54983726;xP")
# HOST = os.getenv("db.qevttwfxqlbzioujvtvn.supabase.co")
# PORT = os.getenv("5432")
# DBNAME = os.getenv("postgres.qevttwfxqlbzioujvtvn")

# # Connect to the database
# try:
#     connection = pg.connect(
#         user=USER,
#         password=PASSWORD,
#         host=HOST,
#         port=PORT,
#         dbname=DBNAME
#     )
#     print("Connection successful!")
    
#     # Create a cursor to execute SQL queries
#     cursor = connection.cursor()
    
#     # Example query
#     cursor.execute("SELECT NOW();")
#     result = cursor.fetchone()
#     print("Current Time:", result)

#     # Close the cursor and connection
#     cursor.close()
#     connection.close()
#     print("Connection closed.")

# except Exception as e:
#     print(f"Failed to connect: {e}")