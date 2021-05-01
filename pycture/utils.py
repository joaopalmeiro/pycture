# More info:
# - https://stackoverflow.com/a/37032111
def emoji_name_to_filename(*names: str, extension: str = "svg") -> str:
    # Based on:
    # - https://inflection.readthedocs.io/en/latest/_modules/inflection.html
    name = "_".join(names)

    name = name.replace(" ", "_")
    name = name.lower()

    return f"{name}.{extension}"
