from data.config import Config
from cryptoapi import CryptoAPI
from tsdb import TSDB

class CryptoDB:

    def __init__(self, config: Config):
        
        self.config = config
        self.crypto_api = CryptoAPI(config.API_KEY)


    def pull_data(self, symbol: str, start_date: str, end_date: str, store_tsdb=False):
        """
        Fetch data from Crypto API, filter between start and end date ranges and optionally store in TSDB
        """

        data = self.crypto_api.fetch_data_between(symbol=symbol, start_date=start_date, end_date=end_date)

        print(data)

        ## Store into TSDB here



