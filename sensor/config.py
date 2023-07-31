import pymongo
import pandas as pd
import json
from dataclasses import dataclass
import os

# provide mongodb url to connect pytgon to mongodb

@dataclass

class EnvironmentVariable:
    mongo_db_url: str = os.getenv("MONGO_DB_URL")
    aws_access_key_id:str = os.getenv("AWS_ACCESS_KEY_ID")
    aws_access_secret_key:str = os.getenv("AWS_SECRET_ACCESS_KEY")

# Creating object of class EnvironmentVariable
env_var = EnvironmentVariable()
mongo_client = pymongo.MongoClient(env_var.mongo_db_url)
TARGET_COLUMN = "class"

