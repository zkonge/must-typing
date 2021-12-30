# Must-typing

Force you (or your user) annotate function types.

**Notice: It's more like a joke, use it carefully.**

**If you call `must_typing` in your module, all your user will be affected.**


## Requirement

+ Python3.6+

## Usage

```python
from musttyping import must_typing

# Your code

must_typing()
```

once a function lack of annotation...

```
Function 'f' located in test.py at line 4
>> def f():
    def f():
        ...
    ...

>> It lack of Return type annotation <<
Traceback (most recent call last):
  File "test.py", line 11, in <module>
    musttyping.must_typing()
  File "musttyping\__init__.py", line 23, in must_typing
    raise LackAnnotationException(f"{obj} need type annotation(s)")
musttyping.LackAnnotationException: <function f at 0x0000018F2167F0D0> need type annotation(s)
```

## Under the hood

`must_typing` will scan all function objects in current runtime, and pick out those defined by user.

Then, it will check if the function lack of annotation, and raise an exception.

It will only scan functions defined by user, which means all function in other module would be ignored, including Python
builtin modules and 3rd party modules.

Once `must_typing` detect running in debugger, it would be turned off automatically.

### detect targets

+ user defined functions
+ user defined class methods

### non detect target

+ builtin and 3rd party module functions
+ functions written in C
+ lambda functions
+ functions defined in closure
+ functions defined in other thread (coming soon)
+ return annotation in class magic methods

## Why this package

Just for fun.

It's better to use `--disallow-untyped-calls` in *mypy* or some other equivalents.

## License

MIT
