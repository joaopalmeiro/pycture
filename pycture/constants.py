from typing import Callable, Dict, List

# CLI
OUTPUT_DIR_HELP: str = "The path to the output directory."
PRETTY_HELP: str = "Pretty-print the SVG code."
SOURCE_HELP: str = "The source of the emoji to obtain."

SOURCES: List[str] = ["Twemoji", "OpenMoji"]

# URLs
TWEMOJI_URL: str = (
    "https://raw.githubusercontent.com/twitter/twemoji/v13.0.2/assets/svg/{code}.svg"
)
OPENMOJI_URL: str = (
    "https://raw.githubusercontent.com/hfg-gmuend/openmoji/13.0.0/color/svg/{code}.svg"
)

URLS: Dict[str, str] = {SOURCES[0]: TWEMOJI_URL, SOURCES[1]: OPENMOJI_URL}
CODE_CASES: Dict[str, Callable[[str], str]] = {
    SOURCES[0]: str.lower,
    SOURCES[1]: str.upper,
}

# SVG
NAMESPACE_URI: str = "http://www.w3.org/2000/svg"
