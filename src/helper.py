import datetime

def validate_date(date_str: str):
    try:
        datetime.datetime.strptime(date_str, '%Y-%m-%d')
    except ValueError:
        raise ValueError("Invalid data format, should be YYYY-MM-DD")

def validate_intraday_interval(interval: str):
    # supports only 1min, 5min, 15min, 30min, 60min intervals

    valid_intraday_intervals = {"1min", "5min", "15min", "30min", "60min"}

    if interval not in valid_intraday_intervals:
        raise ValueError("Invalid intraday interval, only 1min, 5min, 15min, 30min, 60min intervals accepted")
