import datetime
import click

from data.metadata import Metadata as meta

_crypto_options = [
    click.option('--symbol', '-b', required=True, type=str, help='Cryptocurrency symbol'),
    click.option('--start-date', '-s', type=str, default=None, help='Start date YYYY-MM-DD format'),
    click.option('--end-date', '-e', type=str, default=None, help='End date YYYY-MM-DD format'),
    click.option('--interval', '-i', required=True, help='Time interval'), # 1min, 5min, 15min, 30min, 60min, daily, weekly, monthly
    click.option('--store', '-t', default=False, help='Persist collected metrics into backend TSDB')
]

def add_options(options):
    """
    Add shared options to cli commands
    """
    def _add_options(func):
        for option in reversed(options):
            func = option(func)
        return func
    return _add_options

def validate_date(date_str: str):
    try:
        datetime.datetime.strptime(date_str, '%Y-%m-%d')
    except ValueError:
        raise ValueError("Invalid data format, should be YYYY-MM-DD")

def is_valid_interval(interval: str):
    # checks if interval is daily, weekly, or monthly

    if interval not in meta.time_intervals:
        return False
    return True

def is_valid_intraday_interval(interval: str):
    # checks if 1min, 5min, 15min, 30min, 60min intervals

    if interval not in meta.intraday_intervals:
        return False
    return True

def is_valid_symbol(symbol: str):

    if symbol.lower() not in meta.symbols:
        return False
    return True
