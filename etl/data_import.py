import os
import json
import mysql.connector
from sqlalchemy import create_engine
import pandas as pd
import glob
from datetime import datetime

# Load the configuration
with open('config.json', 'r') as config_file:
    config = json.load(config_file)

sources = config['sources']
database_config = config['database']

# Open the database connection
with mysql.connector.connect(
    host=database_config['host'],
    user=database_config['username'],
    password=database_config['password'],
    database=database_config['database']
) as conn:

    # Iterate over the sources and ingest data into raw tables
    for source in sources:
        source_name = source['name']
        folder_path = source['folder']
        file_pattern = source['file_pattern']

        # Construct the full file path with the wildcard
        file_path = os.path.join(folder_path, file_pattern)

        # Use glob to find all files matching the pattern
        matching_files = glob.glob(file_path)

        # Iterate over each matching file
        for file in matching_files:
            # Read the file into a DataFrame
            df = pd.read_csv(file)

            # Add metadata columns
            df['Source'] = source_name
            df['FileName'] = file
            df['StageDate'] = datetime.now()

            # Remove spaces from column names
            df.columns = [col.replace(' ', '_') for col in df.columns]

            # Create the raw table name
            raw_table_name = f"raw_{source_name}"

            # Write the DataFrame to a raw table
            engine_str = f"mysql+mysqlconnector://{database_config['username']}:{database_config['password']}@{database_config['host']}:{database_config['port']}/{database_config['database']}"
            engine = create_engine(engine_str)
            df.to_sql(raw_table_name, con=engine, index=False, if_exists='replace')


            print(f"Data loaded into raw table {raw_table_name} from file: {file}")
