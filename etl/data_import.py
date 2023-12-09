import os
import json

# Load configuration from the config.json file
with open('config/config.json', 'r') as config_file:
    config = json.load(config_file)

# Access configuration values
file_config = config['files']
database_config = config['database']

# Check if the necessary keys are present in the configuration
if 'bank' in file_config and 'credit_card' in file_config and all(key in database_config for key in ['host', 'port', 'database', 'username', 'password']):
    # Use os.path.join to construct file paths
    bank_path = os.path.join(file_config['bank']['path'], file_config['bank']['file_pattern'])
    credit_card_path = os.path.join(file_config['credit_card']['path'], file_config['credit_card']['file_pattern'])

    print(file_config)
    print(database_config)
    print(bank_path)
    print(credit_card_path)
else:
    print("Invalid or incomplete configuration.")
