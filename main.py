from sys import stderr
from functools import wraps


def deprecated(function=None, *, since=None, will_be_removed=None):
    def wrapper(func):
        @wraps(func)
        def inner(*args, **kwargs):
            name = func.__name__
            warning = (f"Warning: function {name} is deprecated{f' since {since}' if since else ''}. It will be "
                       f"removed in {f'version {will_be_removed}' if will_be_removed else 'future versions'}\n")
            stderr.write(warning)
            return func(*args, **kwargs)

        return inner

    if function is None:
        return wrapper
    else:
        return wrapper(function)


@deprecated
def foo():
    "This is a foo() finction"
    print("Hello from foo")


@deprecated(since="4.2.0", will_be_removed="5.0.1")
def bar():
    "And this is a bar() function"
    print("Hello from bar")


@deprecated(since="1.5.2")
def baz(x, y):
    "It is a baz() function, that do ..."
    return 2 ** x + y


if __name__ == '__main__':
    foo()
    bar()
    print(baz(5, 3))
    print(foo.__doc__)
    print(bar.__name__)

