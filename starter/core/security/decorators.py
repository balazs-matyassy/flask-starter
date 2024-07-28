import functools

from flask import abort

from starter.core.security import check_granted, check_owner_or_granted


def is_granted(*roles):
    _roles = [arg.upper() for arg in roles]

    def is_granted_decorator(view):
        @functools.wraps(view)
        def wrapped_view(*args, **kwargs):
            if not check_granted(*roles):
                abort(401)

            return view(*args, **kwargs)

        return wrapped_view

    return is_granted_decorator


def is_owner_or_is_granted(key, *roles):
    _roles = [arg.upper() for arg in roles]

    def is_owner_or_is_granted_decorator(view):
        @functools.wraps(view)
        def wrapped_view(*args, **kwargs):
            if not check_owner_or_granted(kwargs[key], *roles):
                abort(401)

            return view(*args, **kwargs)

        return wrapped_view

    return is_owner_or_is_granted_decorator
