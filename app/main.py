#!/usr/bin/python3
from get_coin_data import get_coin_data
import json


def main():
    with open('data/api_key.json') as f:
        data = json.load(f)

    if data["api_key"]:
        print('AN API KEY: ', data["api_key"])
        print(get_coin_data(data["api_key"], "BTC"))
    else:
        print('Error: Failed to read API key from the JSON file')


if __name__ == '__main__':
    main()
