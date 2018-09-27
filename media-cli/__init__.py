import click
import logging
import sys

__version__ = '0.0.1'
__description__ = 'Media Cli'
__author__ = 'sjoeboo'
__email__ = 'sjoeboo@sjoeboo.com'

logger = logging.getLogger('media-cli')


def setup_logging():
    handler = logging.StreamHandler(sys.stdout)
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)


@click.group(help='Media Cli')
@click.pass_context
def cli(ctx):
    setup_logging()

    ctx.obj = {}
