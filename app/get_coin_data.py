import requests


def get_coin_data(api_key, coin):
    try:
        url = f"http://rest.coinapi.io/v1/exchangerate/{coin}/USD"
        headers = {
            "X-CoinAPI-Key": api_key
        }
        response = requests.get(url, headers=headers)
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
    else:
        print('Error: Failed to retrieve coin data')
