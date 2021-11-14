from data.config import Config
from cryptoapi import CryptoAPI
from tsdb import TSDB
from data.metadata import Metadata as meta
from helper.helper import is_valid_symbol

import logging

import pprint


log = logging.getLogger(__name__)

class CryptoDB:

    def __init__(self, config: Config):
        
        self.config = config
        self.crypto_api = CryptoAPI(config.API_KEY)


    def pull_data(self, symbol: str, start_date: str, end_date: str, start_time: str, end_time: str, interval: str, store_tsdb: bool=False):
        """
        Fetch data from Crypto API, filter between start and end date ranges and optionally store in TSDB
        """

        log.info(f"Fetching cryptocurrency prices")

        # validate symbol
        if not is_valid_symbol(symbol):
            # invalid symbol
            raise ValueError(f"Unrecognized cryptocurrency symbol: {symbol}. List of recognized cryptocurrency symbols: {meta.symbols}")

        # validate interval
        if interval in meta.time_intervals:
            # fetch from daily, weekly, monthly API
            data = self.crypto_api.fetch_data_between(
                symbol=symbol, 
                start_time=start_time, end_time=end_time, 
                interval=interval
            )

        elif interval in meta.intraday_intervals:
            # fetch from intraday API
            data = self.crypto_api.fetch_intraday_data(
                symbol=symbol, 
                start_date=start_date, end_date=end_date, 
                start_time=start_time, end_time=end_time, 
                interval=interval
            )

        else:
            # invalid interval
            raise ValueError(f"Invalid interval provided: {interval}")


        pprint.pprint(data)


        ## Store into TSDB here
        # NOTE: avoid rewriting to DB if time period already exists



