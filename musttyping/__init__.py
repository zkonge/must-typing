from gc import get_objects
from sys import stderr
from types import FunctionType

from .core import need_typing
from .printer import print_function_context

__all__ = ('LackAnnotationException', 'must_typing')


class LackAnnotationException(Exception):
    pass


def must_typing() -> None:
    for obj in get_objects():
        if callable(obj):
            lack_type = need_typing(obj)
            if lack_type:
                assert isinstance(obj, FunctionType), "obj is not FunctionType, please feedback to musttyping author"
                print_function_context(obj)
                print(f">> It lack of {lack_type.name} type annotation <<", file=stderr)
                raise LackAnnotationException(f"{obj} need type annotation(s)")
