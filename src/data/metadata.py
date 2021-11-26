
class Metadata:

    DRIVER = 'postgresql' # DB driver in connection string

    DAILY = 'daily'
    WEEKLY = 'weekly'
    MONTHLY = 'monthly'

    symbols = ['btc', 'eth']
    API_NAME = 'CRYPTO_INTRADAY'
    intraday_intervals = {"1min", "5min", "15min", "30min", "60min"}
    time_intervals = {DAILY, WEEKLY, MONTHLY}

    DATE_FORMAT = '%Y-%m-%d'
    TIME_FORMAT = '%H:%M:%S'
