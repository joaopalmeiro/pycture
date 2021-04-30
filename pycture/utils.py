def emoji_name_to_filename(name: str, extension: str = "svg") -> str:
    # Based on:
    # - https://inflection.readthedocs.io/en/latest/_modules/inflection.html
    name = name.replace(" ", "_")
    name = name.lower()

    return f"{name}.{extension}"
