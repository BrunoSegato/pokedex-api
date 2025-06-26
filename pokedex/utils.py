import importlib
from typing import Any


def load_identifier(name: str) -> Any:
    if "." not in name:
        raise AttributeError(f"Invalid identifier [{name}]")

    module_name, identifier = name.rsplit(".", 1)
    try:
        module = importlib.import_module(module_name)
    except ModuleNotFoundError as error:
        raise AttributeError(f"Module not found {error}") from error
    return getattr(module, identifier)
