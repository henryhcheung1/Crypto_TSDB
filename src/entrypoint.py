import click

from cryptodb import CryptoDB
from data.config import Config
from helper.helper import add_options, _crypto_options
import helper.logger

@click.group()
@click.pass_context
def cli(ctx):

    if ctx.obj is None:
        ctx.obj = dict()

    ctx.obj['cryptodb'] = CryptoDB(Config())
    

@click.command()
@click.pass_context
@add_options(_crypto_options)
def pull_data(ctx, symbol: str, start_date: str, end_date: str, interval: str, store: bool):

    click.echo(f"from {start_date} to {end_date}")
    ctx.obj['cryptodb'].pull_data(symbol=symbol, start_date=start_date, end_date=end_date, interval=interval, store_tsdb=store)

cli.add_command(pull_data)

if __name__ == '__main__':
    cli()