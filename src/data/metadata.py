
class Metadata:

    DAILY = 'daily'
    WEEKLY = 'weekly'
    MONTHLY = 'monthly'

    symbols = ['btc', 'eth']
    API_NAME = 'CRYPTO_INTRADAY'
    intraday_intervals = {"1min", "5min", "15min", "30min", "60min"}
    time_intervals = {DAILY, WEEKLY, MONTHLY}
