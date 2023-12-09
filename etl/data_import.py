import os
import json
import glob

# Load our configuration from the config.json file
with open('config.json', 'r') as config_file:
    config = json.load(config_file)

sources = config['sources']
database_config = config['database']

# Iterate over sources and ingest data into staging tables
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
        
        print(file)

