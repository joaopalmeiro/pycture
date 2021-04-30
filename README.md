# pycture

[![security: bandit](https://img.shields.io/badge/security-bandit-yellow.svg)](https://github.com/PyCQA/bandit)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

A Python CLI for obtaining emojis as files and favicons.

## Tech Stack

- [Click](https://click.palletsprojects.com/) (for the interface)
- [Requests](https://github.com/psf/requests) (for HTTP requests)

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

- [OpenMoji](https://openmoji.org/).
- [emoji](https://github.com/carpedm20/emoji) package.
- [Twemoji](https://github.com/twitter/twemoji).
- Unicode:
  - [Full Emoji List](https://unicode.org/emoji/charts/full-emoji-list.html).
  - [Full Emoji Modifier Sequences](http://www.unicode.org/emoji/charts/full-emoji-modifiers.html).
  - [Emoji Counts](http://www.unicode.org/emoji/charts/emoji-counts.html).
  - [Emoji List, v13.0](https://unicode.org/emoji/charts-13.0/emoji-list.html).
- [cookiecutter-poetry](https://github.com/johanvergeer/cookiecutter-poetry) (only the `pyproject.toml` file and no `poetry.lock` file).
- `cli.py` or `console.py`.
- [Asyncio integration](https://github.com/pallets/click/issues/85) issue (Click).
- [asyncclick](https://github.com/python-trio/asyncclick) package (fork of Click).
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
