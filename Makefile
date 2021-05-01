.PHONY: all check type isort black lint bandit quickstart

CMD:=poetry run
PYMODULE:=pycture

all: check type isort black lint bandit

check:
	poetry check

type:
	$(CMD) mypy $(PYMODULE)

isort:
	$(CMD) isort $(PYMODULE)

black:
	$(CMD) black $(PYMODULE)

lint:
	$(CMD) flake8 $(PYMODULE)

bandit:
	$(CMD) bandit -r $(PYMODULE)

quickstart:
	$(CMD) $(PYMODULE) --help | pbcopy
