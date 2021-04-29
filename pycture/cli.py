import click

from . import __version__


@click.command()
@click.version_option(version=__version__)
def main():
    """Get emojis as files and favicons."""
    click.echo("Hello, world!")
