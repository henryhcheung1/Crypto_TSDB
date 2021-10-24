import click

from cryptodb import CryptoDB
from data.config import Config

@click.group()
@click.pass_context
def cli(ctx):

    if ctx.obj is None:
        ctx.obj = dict()

    ctx.obj['cryptodb'] = CryptoDB(Config())
    


@click.command()
@click.option('--symbol', '-b', required=True, type=str, help='Cryptocurrency symbol')
@click.option('--start-date', '-s', type=str, help='Start date YYYY-MM-DD format')
@click.option('--end-date', '-e', type=str, help='End date YYYY-MM-DD format')
@click.option('--store', '-t', default=False, help='Persist collected metrics into backend TSDB')
# @click.option('--interval', '-i', help='Time interval')
@click.pass_context
def pull_data(ctx, symbol: str, start_date: str, end_date: str, store: bool):

    click.echo(f"from {start_date} to {end_date}")
    ctx.obj['cryptodb'].pull_data(symbol=symbol, start_date=start_date, end_date=end_date, store_tsdb=store)



cli.add_command(pull_data)

if __name__ == '__main__':
    cli()