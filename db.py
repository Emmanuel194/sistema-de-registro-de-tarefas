import pyodbc
from dotenv import load_dotenv
import os

load_dotenv()

def get_connection():
    conn = pyodbc.connect(
        f"DRIVER={os.getenv('DRIVER')};"
        f"SERVER={os.getenv('SERVER')};"
        f"DATABASE={os.getenv('DATABASE')};"
        f"Trusted_Connection={os.getenv('Trusted_Connection')};"
    )
    return conn
