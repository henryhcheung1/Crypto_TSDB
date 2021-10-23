from alpha_vantage.cryptocurrencies import CryptoCurrencies
# import matplotlib.pyplot as plt

import pprint
import os

class Crypto:

    def __init__(self, api_key: str):
        self.api_key = api_key

        self.output_format = 'pandas' # or json

    def fetch_daily(self, symbol: str, market='CNY'):
        
        # check if symbol is valid

        cc = CryptoCurrencies(key=self.api_key, output_format=self.output_format)
        data, meta_data = cc.get_digital_currency_daily(symbol=symbol, market=market)

        return data, meta_data


if __name__ == '__main__':

    pp = pprint.PrettyPrinter(indent=2)

    cc = Crypto(os.environ['API_KEY'])

    symbol = 'btc'

    data, meta_data = cc.fetch_daily(symbol)

    pp.pprint(data)
    pp.pprint(meta_data)
    pp.pprint(data.columns)
    pp.pprint(data.head())





# cc = CryptoCurrencies(key=config.API_KEY, output_format='pandas')

# data, meta_data = cc.get_digital_currency_daily(symbol='BTC', market='CNY')

# data, meta_data = cc.get_digital_currency_exchange_rate(from_currency='BTC', to_currency='USD')
# pp.pprint(data)
# pp.pprint(meta_data)
# pp.pprint(data.columns)
# pp.pprint(data.head())
