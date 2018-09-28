import click
import logging
import sys
import yaml
from pathlib import Path
from mcli.backends import plex_client
from mcli.backends import sickbeard_client



__version__ = '0.0.1'
__description__ = 'Media Cli'
__author__ = 'sjoeboo'
__email__ = 'sjoeboo@sjoeboo.com'

logger = logging.getLogger('media-cli')
home = str(Path.home())


def setup_logging():
    handler = logging.StreamHandler(sys.stdout)
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)


def load_config(config_file):
    with open(config_file, 'r') as f:
        config = yaml.load(f)
        return config


@click.group(help='Media Cli')
@click.option('--config_file', envvar='MCLI_CONFIG', help='Config location', default='{}/.mcli.yml'.format(home))
@click.pass_context
def cli(ctx, config_file):
    setup_logging()
    config = load_config(config_file)
    ctx.obj = {'config': config}



@cli.command(name='plex', help='Do plex things')
@click.option('--sync')
@click.pass_obj
def plex(ctx, sync):
    plex_config=ctx['config']['services']['plex']
    if sync:
        plex_client.sync(plex_config)


@cli.command(name='sickbeard', help='Do sickbeard things')
@click.option('--upcoming', is_flag=True)
@click.option('--history', is_flag=True)
@click.pass_obj
def sickbeard(ctx, upcoming, history):
    sb_config=ctx['config']['services']['sickbeard']
    if upcoming:
        sickbeard_client.upcoming(sb_config)
    elif history:
        sickbeard_client.history(sb_config)
