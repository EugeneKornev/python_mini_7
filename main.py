from sys import stderr


def deprecated(function=None, *, since=None, will_be_removed=None):
    def wrapper(func):
        def inner(*args, **kwargs):
            name = func.__name__
            if since and will_be_removed:
                stderr.write(
                    f"Warning: function {name} is deprecated since version {since}. It will be removed in version {will_be_removed}\n")
            elif since:
                stderr.write(
                    f"Warning: function {name} is deprecated since version {since}. It will be removed in future versions\n")
            elif will_be_removed:
                stderr.write(
                    f"Warning: function {name} is deprecated. It will be removed in version {will_be_removed}\n")
            else:
                stderr.write(f"Warning: function {name} is deprecated. It will be removed in future versions\n")
            return func(*args, **kwargs)

        return inner

    if function is None:
        return wrapper
    else:
        return wrapper(function)


@deprecated
def foo():
    print("Hello from foo")


@deprecated(since="4.2.0", will_be_removed="5.0.1")
def bar():
    print("Hello from bar")


@deprecated(since="1.5.2")
def baz(x, y):
    return 2 ** x + y


if __name__ == '__main__':
    foo()
    bar()
    print(baz(5, 3))

