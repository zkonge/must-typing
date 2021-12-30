from enum import Enum, auto
from pathlib import Path
from sys import base_exec_prefix, base_prefix, exec_prefix, gettrace, intern, prefix
from types import FunctionType
from typing import Any, List, Optional

from _sitebuiltins import Quitter

_always_ignore: bool = False
_libs_root_paths: List[Path] = [Path(x) for x in (prefix, base_prefix, exec_prefix, base_exec_prefix)]

_lambda_string: str = intern("<lambda>")
_main_string: str = intern("__main__")
_spec_string: str = intern("__spec__")
_return_string: str = intern("return")
_double_underline_string: str = intern("__")

# we won't detect if it needs annotation running in debugger (or some other tracing environments)
if gettrace() or not isinstance(exit, Quitter):
    _always_ignore = True


class LackType(Enum):
    Argument = auto()
    Return = auto()


def need_func_typing(f: FunctionType) -> Optional[LackType]:
    name = f.__name__
    code = f.__code__
    args = code.co_varnames[: code.co_argcount]
    annotations = f.__annotations__
    is_method = f.__name__ != f.__qualname__

    # as a method, skip 'self' and 'cls'
    if is_method:
        args = args[1:]

    for arg in args:
        if arg not in annotations:
            return LackType.Argument

    # magic method needn't return annotation
    if is_method and name[:2] == name[-2:] == _double_underline_string:
        return None
    else:
        return LackType.Return if _return_string not in annotations else None


def need_typing(f: Any) -> Optional[LackType]:
    if _always_ignore:
        return None

    # only focus on functions written in Python
    if not isinstance(f, FunctionType):
        return None

    # make type hint for lambda ?
    if f.__name__ == _lambda_string:
        return None

    # it's bad to annotate a closure
    if f.__closure__:
        return None

    # main module has no module spec
    if f.__module__ == _main_string:
        return need_func_typing(f)

    module_spec = f.__globals__.get(_spec_string, None)
    if not module_spec:
        return None

    if not module_spec.has_location:
        return None

    module_path = Path(module_spec.origin).absolute()
    # ignore builtin and 3rd party modules
    if any(module_path.is_relative_to(p) for p in _libs_root_paths):
        return None

    return need_func_typing(f)
