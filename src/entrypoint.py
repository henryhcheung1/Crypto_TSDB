import click

from data.config import Config

@click.group()
@click.pass_context
def cli(ctx):

    if ctx.obj is None:
        ctx.obj = dict()

    ctx.obj['config'] = Config()
    # ctx.obj['crypto'] = Crypto()
    


@click.command()
@click.option('--start-date', '-s')
@click.option('--end-date', '-e')
@click.pass_context
def pull_data(ctx, start_date, end_date):
    click.echo(f"from {start_date} to {end_date}")

cli.add_command(pull_data)

if __name__ == '__main__':
    cli()