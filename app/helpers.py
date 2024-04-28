from os.path import exists
import json
import pandas as pd


def write_to_file(filename, data):
    if exists(filename):
        # Write the DataFrame to a CSV file
        data.to_csv(filename, mode='a', header=False, index=False)
    else:
        # Write the DataFrame to a CSV file
        data.to_csv(filename, index=False)


def api_key():
    file_api_key = 'data/api_key.json'
    with open(file_api_key, 'r') as file:
        data = json.load(file)
    if data['api_key']:
        return data['api_key']
    else:
        print('Error: Failed to read API key from the JSON file')
