import click
import requests

from . import __version__
from .constants import TWEMOJI_URL


@click.command()
@click.version_option(version=__version__)
def main():
    """Get emojis as files and favicons."""
    response = requests.get(TWEMOJI_URL.format(code="1f004"))

    # click.echo(response.headers)
    click.echo(response.text)
