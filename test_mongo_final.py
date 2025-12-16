from pymongo import MongoClient
import certifi
import os
from dotenv import load_dotenv

load_dotenv()

client = MongoClient(
    os.getenv("mongodb+srv://swabhimanraj453_db_user:Kite123456789.@cluster0.qzcfyo3.mongodb.net/?appName=Cluster0"),
    tls=True,
    tlsCAFile=certifi.where()
)

print(client.list_database_names())
