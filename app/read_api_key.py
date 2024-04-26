import json


def read_api_key(file_path):
    try:
        # Open the JSON file and load the contents
        with open(file_path, 'r') as file:
            data = json.load(file)

        # Get the API key from the JSON data
        api_key = data.get('api_key')

        if api_key:
            return api_key
        else:
            print('Error: API key not found in the JSON file')
    except FileNotFoundError:
        print(f"Error: File not found: {file_path}")
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON format in file: {file_path}")

    return None
