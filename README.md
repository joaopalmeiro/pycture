# pycture

[![security: bandit](https://img.shields.io/badge/security-bandit-yellow.svg)](https://github.com/PyCQA/bandit)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

A Python CLI for obtaining emojis as files and favicons.

## Quickstart

```sh
Usage: pycture [OPTIONS] EMOJI

  Get EMOJI as a file or favicon via its CLDR short name.

  Use Unicode 9.0 and Emoji 3.0 as a reference.

Options:
  -o, --output-dir DIRECTORY      The path to the output directory.  [default:
                                  (current directory)]

  -p, --pretty                    Pretty-print the SVG code.
  -s, --source [Twemoji|OpenMoji]
                                  The source of the emoji to obtain.
                                  [default: Twemoji]

  --version                       Show the version and exit.
  --help                          Show this message and exit.
```

## Tech Stack

- [Click](https://click.palletsprojects.com/) (for the interface)
- [Requests](https://github.com/psf/requests) (for HTTP requests)
- [defusedxml](https://github.com/tiran/defusedxml) (for parsing XML/SVG data)

### Packaging and Development

- [Poetry](https://python-poetry.org/)
- [Mypy](http://mypy-lang.org/)
- [isort](https://pycqa.github.io/isort/)
- [Black](https://github.com/psf/black)
- [Flake8](https://flake8.pycqa.org/)
  - [flake8-bugbear](https://github.com/PyCQA/flake8-bugbear)
  - [flake8-comprehensions](https://github.com/adamchainz/flake8-comprehensions)
  - [pep8-naming](https://github.com/PyCQA/pep8-naming)
  - [flake8-builtins](https://github.com/gforcada/flake8-builtins)
- [Bandit](https://bandit.readthedocs.io/)

This CLI was created with [Cookiecutter](https://github.com/audreyr/cookiecutter) and the [`joaopalmeiro/cookiecutter-templates/python-cli`](https://github.com/joaopalmeiro/cookiecutter-templates) project template.

## Notes

- [click-contrib](https://github.com/click-contrib) (a collection of third-party extensions).
  - [click-man](https://github.com/click-contrib/click-man) package (man pages).
  - [click-help-colors](https://github.com/click-contrib/click-help-colors) package.
  - [click-didyoumean](https://github.com/click-contrib/click-didyoumean) package.
  - [click_params](https://github.com/click-contrib/click_params) package (extra types).
- [OpenMoji](https://openmoji.org/).
- [emoji](https://github.com/carpedm20/emoji) package.
- [demoji](https://github.com/bsolomon1124/demoji) package.
- [Twemoji](https://github.com/twitter/twemoji).
- [Inflection](https://inflection.readthedocs.io/en/latest/) package.
- Unicode:
  - [Full Emoji List](https://unicode.org/emoji/charts/full-emoji-list.html).
  - [Full Emoji Modifier Sequences](http://www.unicode.org/emoji/charts/full-emoji-modifiers.html).
  - [Emoji Counts](http://www.unicode.org/emoji/charts/emoji-counts.html).
  - [Emoji List, v13.0](https://unicode.org/emoji/charts-13.0/emoji-list.html).
  - [unicodedata](https://docs.python.org/3.6/library/unicodedata.html) (Python 3.6 -> Unicode 9.0).
  - [Emoji Version 3.0](https://emojipedia.org/emoji-3.0/) (this emoji version coincided with the release of Unicode 9.0).
- [cookiecutter-poetry](https://github.com/johanvergeer/cookiecutter-poetry) (only the `pyproject.toml` file and no `poetry.lock` file).
- `cli.py` or `console.py`.
- [Asyncio integration](https://github.com/pallets/click/issues/85) issue (Click).
- [asyncclick](https://github.com/python-trio/asyncclick) package (fork of Click).
- [XML vulnerabilities](https://docs.python.org/3/library/xml.html#xml-vulnerabilities).
- Bandit:
  - [B405 complains about any xml.etree.ElementTree import, not just parse-related ones](https://github.com/PyCQA/bandit/issues/709) (open) issue.
  - [from xml.etree.ElementTree import Element Flagged](https://github.com/PyCQA/bandit/issues/602) (open) issue.
  - [Error message refers to "defusedxml.defuse_stdlib()" but calling that does not silence bandit](https://github.com/PyCQA/bandit/issues/708) (open) issue.
  - [defusedxml](https://github.com/tiran/defusedxml) provides alternatives for parsing-related functions.
- [Shell completion](https://click.palletsprojects.com/en/7.x/bashcomplete/) (for commands, options, and choice values):
  - Generate the [activation script](https://click.palletsprojects.com/en/7.x/bashcomplete/#activation-script): `_PYCTURE_COMPLETE=source_zsh pycture > pycture-complete.sh`.
- [aiohttp](https://github.com/aio-libs/aiohttp) package (vs. [Requests](https://github.com/psf/requests)):
  - "(...) you can picture the session object as a user starting and closing a browser: it wouldn't make sense to do that every time you want to load a new tab." ([source](https://docs.aiohttp.org/en/stable/http_request_lifecycle.html))

```python
# aiohttp
async with aiohttp.ClientSession() as session:
    async with session.get("http://python.org") as response:
        print(await response.text())

# vs.

# Requests
response = requests.get("http://python.org")
print(response.text)

# or

with requests.Session() as session:
    response = session.get("http://python.org")
    print(response.text)
```
