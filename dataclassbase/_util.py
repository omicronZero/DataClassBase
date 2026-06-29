import types as _types
import typing as _typing

type E[T] = T | _types.EllipsisType


def throws(f: _typing.Callable[[], _typing.Any], *exception_types: type[BaseException]) -> bool:
    """
    Makes the indicated call and returns whether an exception of one of the indicated types occurred. Exceptions of
    other types do not get caught.

    :param f: The function to invoke.
    :param exception_types: The exception types to check for.
    :return: `True` if an exception occurred that satisfied one of the supplied exception types, `False` if no exception
        occurred.
    """
    try:
        f()
    except BaseException as ex:
        if isinstance(ex, exception_types):
            return True

        raise

    return False
