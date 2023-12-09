import os
import json

# Load configuration from the config.json file
with open('config.json', 'r') as config_file:
    config = json.load(config_file)

# Access configuration values
sources = config['sources']
database = config['database']

for source in sources:
    file_path = os.path.join(source['folder'], source['file_pattern'])
    print(source['name'])
    print(source['folder'])
    print(source['file_pattern'])
    print(file_path)
