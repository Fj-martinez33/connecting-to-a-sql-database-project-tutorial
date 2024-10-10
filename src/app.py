import os
from sqlalchemy import create_engine
import pandas as pd
from dotenv import load_dotenv

# load the .env file variables
load_dotenv()

# 1) Connect to the database here using the SQLAlchemy's create_engine function

def connect ():
    global engine #variable de sqlalchemy.
    connection_string = f"postgresql://{os.getenv('usrfmm20241010_1107')}:{os.getenv('*r2YtH7xI4yJo')}@{os.getenv('localhost')}/{os.getenv('sample-db')}?autocommit=true"
    print("Starting connection...")
    engine = create_engine(connection_string)
    engine.connect()
    return engine
# 2) Execute the SQL sentences to create your tables using the SQLAlchemy's execute function

# 3) Execute the SQL sentences to insert your data using the SQLAlchemy's execute function

# 4) Use pandas to print one of the tables as dataframes using read_sql function

print(connect())