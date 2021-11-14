from helper.helper import validate_datetimes
from data.metadata import Metadata as meta

from alpha_vantage.cryptocurrencies import CryptoCurrencies
import requests
import json
import logging

import pprint
import os

log = logging.getLogger(__name__)

# Notes: Alpha Vantage API Python bindings currently doesnt provide intra day measurements. 
# To obtain intra day measurements (e.g. measurement intervals of 15 minutes), need to hit API directly
# https://www.alphavantage.co/documentation/#crypto-intraday

class CryptoAPI:

    def __init__(self, api_key: str):
        self.api_key = api_key

        self.output_format = 'pandas' # or json
        self.outputsize = 'full' # or compact

    def fetch_data_between(self, symbol: str, start_time: str, end_time: str, interval: str, market: str='USD'):
        
        # check dates are valid
        validate_datetimes(start_time, end_time)


        log.info(f"Fetching {symbol} at {interval} intervals")


        cc = CryptoCurrencies(key=self.api_key, output_format=self.output_format)

        # Call appropriate time interval API
        data = None
        if interval == meta.DAILY:
            data, _ = cc.get_digital_currency_daily(symbol=symbol, market=market)

        elif interval == meta.WEEKLY:
            data, _ = cc.get_digital_currency_weekly(symbol=symbol, market=market)

        elif interval == meta.MONTHLY:
            data, _ = cc.get_digital_currency_monthly(symbol=symbol, market=market)


        if start_time is not None and end_time is not None:
            # filter data between range of dates

            log.info(f"Filtering dates between {start_time} and {end_time}")
            data = data[start_time:end_time]

        return data[self.__get_desired_columns(market)]



    def fetch_intraday_data(self, symbol: str, start_time: str, end_time: str, interval: str, market: str='USD'):
        # Alpha vantage Python bindings currently do not support intraday, therefore required to call alpha vantage endpoints directly

        # validate time range
        validate_datetimes(start_time, end_time, check_date=False)

        url = f"https://www.alphavantage.co/query?function={meta.API_NAME}&symbol={symbol}&market={market}&interval={interval}&apikey={self.api_key}&outputsize={self.outputsize}"

        log.info(f"Fetching {symbol} at {interval} intervals")

        try:
            response = requests.get(url)
            response.raise_for_status()
        except requests.exceptions.HTTPError as err:
            raise ValueError(f"HTTP Error, {err}")

        json_response = json.loads(response.text)

        return json_response



    def __get_desired_columns(self, market: str) -> list:
        # Alpha Vantage API specific column headers

        return [f"1a. open ({market})", f"2a. high ({market})",
       f"3a. low ({market})", f"4a. close ({market})",
       '5. volume', '6. market cap (USD)']


    # def __filter_date(self, data: , start_time: str, end_time: str):

    #     if start_time is not None and end_time is not None:
    #         # filter data between range of dates

    #         log.info(f"Filtering dates between {start_time} and {end_time}")
    #         data = data[start_time:end_time]
       


if __name__ == '__main__':

    pp = pprint.PrettyPrinter(indent=2)

    cc = CryptoAPI(os.environ['API_KEY'])

    symbol = 'btc'
    interval = '5min'

    # data, meta_data = cc.fetch_daily_between(symbol=symbol, start_date="2021-9-18", end_date="2021-10-22")

    # pp.pprint(data)
    # pp.pprint(meta_data)
    # pp.pprint(data.columns)
    # pp.pprint(data.head())

    response = cc.fetch_intraday_data(symbol=symbol, interval=interval)
    pprint.pprint(response)

    # print(response.text)
