import xml.etree.ElementTree as ET
from xml.dom.minidom import parseString

import click
import requests

from . import __version__
from .constants import NAMESPACE_URI, PRETTY_HELP, TWEMOJI_URL


# More info:
# - https://click.palletsprojects.com/en/7.x/options/#boolean-flags
@click.command()
@click.option("--pretty", is_flag=True, help=PRETTY_HELP)
@click.version_option(version=__version__)
def main(pretty):
    """Get emojis as files and favicons."""
    response = requests.get(TWEMOJI_URL.format(code="1f948"))

    # click.echo(response.headers)
    # lick.echo(response.text)

    ET.register_namespace("", NAMESPACE_URI)

    # Source: https://stackoverflow.com/a/17402424
    svg_string = parseString(response.text).toprettyxml() if pretty else response.text
    tree = ET.ElementTree(ET.fromstring(svg_string))

    with open("test.svg", "w") as f:
        # Source: https://stackoverflow.com/a/37713268
        tree.write(f, encoding="unicode", method="xml")
