import datetime
import click

from data.metadata import Metadata as meta

_crypto_options = [
    click.option('--symbol', '-b', required=True, type=str, help='Cryptocurrency symbol'),
    click.option('--start-time', '-s', type=str, default=None, help='Start date YYYY-MM-DD format or start time HH:MM:SS format'),
    click.option('--end-time', '-e', type=str, default=None, help='End date YYYY-MM-DD format or end time HH:MM:SS format'),
    click.option('--interval', '-i', required=True, help='Time interval'), # 1min, 5min, 15min, 30min, 60min, daily, weekly, monthly
    click.option('--store', '-t', default=False, help='Persist collected metrics into backend TSDB')
]

TIME_FORMAT = '%H-%M-%S'
DATE_FORMAT = '%Y-%m-%d'

def add_options(options):
    """
    Add shared options between cli commands
    """
    def _add_options(func):
        for option in reversed(options):
            func = option(func)
        return func
    return _add_options

def validate_datetime(time_str: str, validation_format: str):

    assert(validation_format == TIME_FORMAT or validation_format == DATE_FORMAT)

    try:
        datetime.datetime.strptime(time_str, validation_format)
    except ValueError:
        raise ValueError(f"Invalid date / time format, Date / time format should be {DATE_FORMAT} / {TIME_FORMAT} respectively")

def validate_datetimes(start_time: str, end_time: str, check_date: bool=True):

    if start_time is not None and end_time is not None:
        # dates are specifed

        # check date/time formats
        if check_date is True:
            # check date
            validate_datetime(start_time, DATE_FORMAT)
            validate_datetime(end_time, DATE_FORMAT)
        else:
            # check time
            validate_datetime(start_time, TIME_FORMAT)
            validate_datetime(end_time, TIME_FORMAT)

        # check start date precedes end date
        if start_time > end_time: # string comparison of ISO format is sufficient
            raise ValueError("Invalid date/time range. Start start_time does not precede end end_time")


    elif [start_time, end_time].count(None) == 1:
        # one date was specified but the other was not
        raise ValueError("Only one date/time was specified. Both start_time and end_time need to be specified")

    # else:
    #     # both None, do not filter on datetime range, (retrieve all data)


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
