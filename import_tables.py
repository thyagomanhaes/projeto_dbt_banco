#%% Libraries
import os
import pandas as pd
from sqlalchemy import create_engine
from getpass import getpass

# %% Variables
base = os.getcwd() # current working directory 
path_tables = os.path.join(base, 'sources') # base\\sources
tables = os.listdir(path_tables) # List the files in path_tables
# password = getpass('Database password:')

#%% Create database connection
HOST="34.218.235.113"
USER="greenvest"
PASSWORD="greenvesttecnologia"
con = create_engine(f'postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}:5432/soccerbets')

#%% Upload tables
for table in tables:
    path_table = os.path.join(path_tables, table)
    table = table.replace('.csv', '')
    df = pd.read_csv(path_table)
    df.to_sql(
        table, con, schema='transacional',
        if_exists='replace', index=False
    )
    print(f'Table {table} uploaded!')