import functools

from flask import g, abort


def scalar(view):
    @functools.wraps(view)
    def wrapped_view(*args, **kwargs):
        return g.session.scalar(view(*args, **kwargs))

    return wrapped_view


def scalars(view):
    @functools.wraps(view)
    def wrapped_view(*args, **kwargs):
        return g.session.scalars(view(*args, **kwargs))

    return wrapped_view


def param(name, factory, *keys, keep_keys=False):
    def param_decorator(view):
        @functools.wraps(view)
        def wrapped_view(*args, **kwargs):
            value = factory(*[kwargs[key] for key in keys])

            if value is None:
                abort(404)

            _kwargs = {key: kwargs[key] for key in kwargs} \
                if keep_keys \
                else {key: kwargs[key] for key in kwargs if key not in keys}

            _kwargs[name] = value

            return view(*args, **_kwargs)

        return wrapped_view

    return param_decorator
