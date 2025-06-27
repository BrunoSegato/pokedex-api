from contextvars import ContextVar
from typing import Any, Dict

_context_vars: Dict[str, ContextVar] = {}


def set_context(key: str, value: Any) -> None:
    var = _context_vars.get(key)
    if not var:
        var = ContextVar(key, default=None)
        _context_vars[key] = var
    var.set(value)


def get_context(key: str, default: Any = None) -> Any:
    var = _context_vars.get(key)
    if not var:
        return default
    return var.get()
