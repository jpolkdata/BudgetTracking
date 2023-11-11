import pandas as pd
import json
import os

# Load configuration from the config.json file
with open('config.json', 'r') as config_file:
    config = json.load(config_file)

# Access configuration values
input_directory = config['input_directory']

# Look for any file starting with 'COMBINED' and having a '.csv' extension
combined_files = [f for f in os.listdir(input_directory) if f.lower().startswith('combined') and f.lower().endswith('.csv')]

# Check if there is at least one combined file
if not combined_files:
    print("No combined file found.")
else:
    # Take the first combined file (you may modify this logic if needed)
    combined_file_name = combined_files[0]

    # Construct the full path to the combined file
    combined_file_path = os.path.join(input_directory, combined_file_name)

    # Read the combined CSV file into a DataFrame
    df = pd.read_csv(combined_file_path)

    # Display the DataFrame
    print(df)
