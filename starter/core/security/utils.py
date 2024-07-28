from flask import g


def check_granted(*roles):
    if not g.user:
        return False

    roles = [arg.upper() for arg in roles]

    return ('IS_AUTHENTICATED_FULLY' in roles
            or 'ROLE_' + g.user.role.key in roles)


def check_owner_or_granted(entity, *roles):
    if not g.user:
        return False

    if hasattr(entity, 'owner_id') and entity.owner_id == g.user.id:
        return True

    counter = 1

    while hasattr(entity, f'owner_{counter}_id'):
        if getattr(entity, f'owner_{counter}_id') == g.user.id:
            return True

        counter += 1

    roles = [arg.upper() for arg in roles]

    return ('IS_AUTHENTICATED_FULLY' in roles
            or 'ROLE_' + g.user.role.key in roles)
