#!/usr/bin/python3
from get_coin_data import get_coin_data
import json


def write_to_file(filename, data):
    with open(filename, 'a') as file:
        json.dump(data, file)


def main():
    with open('data/api_key.json') as f:
        data = json.load(f)

    if data["api_key"]:
        cryptocurrency = get_coin_data(data["api_key"], "BTC")
        print(cryptocurrency)
        write_to_file('/data/cryptocurrency.json', cryptocurrency)
    else:
        print('Error: Failed to read API key from the JSON file')


if __name__ == '__main__':
    main()
