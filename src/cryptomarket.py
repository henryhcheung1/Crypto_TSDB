from alpha_vantage.cryptocurrencies import CryptoCurrencies
from helper import validate_date
# import matplotlib.pyplot as plt

import pprint
import os

# Notes: Alpha Vantage API Python bindings currently doesnt provide intra day measurements. 
# To obtain intra day measurements (e.g. measurement intervals of 15 minutes), need to hit API directly
# https://www.alphavantage.co/documentation/#crypto-intraday

class Cryptomarket:

    def __init__(self, api_key: str):
        self.api_key = api_key

        self.output_format = 'pandas' # or json

    def fetch_daily_between(self, symbol: str, start_date: str, end_date: str, market: str='USD'):
        
        # check if symbol is valid

        # check dates are valid
        validate_date(start_date)
        validate_date(end_date)

        cc = CryptoCurrencies(key=self.api_key, output_format=self.output_format)
        data, meta_data = cc.get_digital_currency_daily(symbol=symbol, market=market)

        # select range of dates
        result = data[start_date:end_date]

        print(result[self.__get_desired_columns(market)])

        return result[self.__get_desired_columns(market)], meta_data

    def __get_desired_columns(self, market: str) -> list:
        # Alpha Vantage API specific column headers

        return [f"1a. open ({market})", f"2a. high ({market})",
       f"3a. low ({market})", f"4a. close ({market})",
       '5. volume', '6. market cap (USD)']
       


if __name__ == '__main__':

    pp = pprint.PrettyPrinter(indent=2)

    cc = Cryptomarket(os.environ['API_KEY'])

    symbol = 'btc'

    data, meta_data = cc.fetch_daily_between(symbol=symbol, start_date="2021-9-18", end_date="2021-10-22")

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
