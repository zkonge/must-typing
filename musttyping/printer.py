from inspect import getfile, getsourcelines
from sys import stderr
from types import FunctionType


def print_function_context(f: FunctionType) -> None:
    name, file, (source, source_line_number) = f.__name__, getfile(f), getsourcelines(f)

    print(f"Function '{name}' located in {file} at line {source_line_number}", file=stderr)
    print(">>", "".join(source[:5]), file=stderr)
