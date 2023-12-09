import os
import pandas as pd
import json
from datetime import datetime

# Load configuration from the config.json file
with open('config.json', 'r') as config_file:
    config = json.load(config_file)

# Access configuration values
input_directory = config['input_directory']

# Get a list of all files in the directory
all_files = os.listdir(input_directory)

# Filter only the files with a .csv extension (case-insensitive)
csv_files = [f for f in all_files if f.lower().endswith('.csv')]

# Initialize variables to keep track of record counts
total_records = 0
records_per_file = {}

# Initialize an empty DataFrame to store the combined data
combined_df = pd.DataFrame()

# Loop through each CSV file and append its data to the combined DataFrame
for csv_file in csv_files:
    file_path = os.path.join(input_directory, csv_file)
    try:
        df = pd.read_csv(file_path)
        record_count = len(df)
        total_records += record_count
        records_per_file[csv_file] = record_count
        combined_df = combined_df.append(df, ignore_index=True)
    except Exception as e:
        print(f"Error reading {file_path}: {e}")

# Generate the output file name with 'COMBINED' and current datetime
current_datetime = datetime.now().strftime('%Y%m%d%H%M%S')
output_file = f'{input_directory}\\COMBINED_{current_datetime}.csv'

# Save the combined DataFrame to the new CSV file
combined_df.to_csv(output_file, index=False)

# Output record counts
print("Record counts:")
for file, count in records_per_file.items():
    print(f"{file}: {count} records")

print(f"Total records across all files: {total_records}")
print(f"Records in the output file ({output_file}): {len(combined_df)}")
