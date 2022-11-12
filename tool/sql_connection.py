import sqlalchemy as alch
import os
from dotenv import load_dotenv
from getpass import getpass

password = os.getenv("password_mysql")
dbName = "project_4"
connectionData=f"mysql+pymysql://root:{password}@localhost/{dbName}"
engine = alch.create_engine(connectionData)
