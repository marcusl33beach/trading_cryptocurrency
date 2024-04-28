#!/usr/bin/python3
from get_coin_data import get_coin_data
from helpers import *
import pandas as pd


def main():
    cryptocurrency = get_coin_data(api_key(), 'BTC')
    # Read the data dict into a DataFrame
    cryptocurrencyd_dataframe = pd.DataFrame(cryptocurrency, index=[1])
    print(cryptocurrencyd_dataframe)
    write_to_file('/data/cryptocurrency.csv', cryptocurrencyd_dataframe)


if __name__ == '__main__':
    main()
