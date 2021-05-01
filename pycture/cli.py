import unicodedata
from pathlib import Path
from xml.etree.ElementTree import ElementTree, register_namespace  # nosec

import click
import requests

# import xml.etree.ElementTree as ET
from defusedxml.ElementTree import fromstring

# from xml.dom.minidom import parseString
from defusedxml.minidom import parseString

from . import __version__
from .constants import (
    CODE_CASES,
    NAMESPACE_URI,
    OUTPUT_DIR_HELP,
    PRETTY_HELP,
    SOURCE_HELP,
    SOURCES,
    URLS,
)
from .utils import emoji_name_to_filename, unprettify


# More info:
# - https://click.palletsprojects.com/en/7.x/options/#boolean-flags
@click.command()
@click.argument("emoji", type=str)
@click.option(
    "-o",
    "--output-dir",
    type=click.Path(exists=True, file_okay=False, dir_okay=True),
    help=OUTPUT_DIR_HELP,
    default=".",
    # show_default=True,
    show_default="current directory",
)
@click.option("-p", "--pretty", is_flag=True, help=PRETTY_HELP)
@click.option(
    "-s",
    "--source",
    type=click.Choice(SOURCES, case_sensitive=False),
    default=SOURCES[0],
    help=SOURCE_HELP,
)
@click.version_option(version=__version__)
def main(emoji: str, output_dir: str, pretty: bool, source: str) -> None:
    """Get EMOJI as a file or favicon via its CLDR short name.

    Use Unicode 9.0 and Emoji 3.0 as a reference.
    """
    # More info:
    # - https://docs.python.org/3/library/string.html#format-specification-mini-language
    emoji_symbol = unicodedata.lookup(emoji.upper())
    code = f"{ord(emoji_symbol):x}"
    code = CODE_CASES[source](code)

    url = URLS[source].format(code=code)
    click.echo(f"\n🌐 {click.style('Source', bold=True)}: {url}")

    response = requests.get(url)

    # click.echo(response.headers)
    # click.echo(response.text)

    register_namespace("", NAMESPACE_URI)

    svg_code = unprettify(response.text)

    # Source: https://stackoverflow.com/a/17402424
    svg_string = parseString(svg_code).toprettyxml() if pretty else svg_code
    tree = ElementTree(fromstring(svg_string))

    filename = emoji_name_to_filename(emoji, source)
    output_path = Path(output_dir) / filename

    with open(output_path, "w") as f:
        # Source: https://stackoverflow.com/a/37713268
        tree.write(f, encoding="unicode", method="xml")

    click.secho("\n✨ Done!", bold=True)
