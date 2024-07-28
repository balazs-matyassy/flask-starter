from starter.core.persistence.decorators import scalars, scalar
from starter.core.persistence.repository import CrudRepository


class RoleRepository(CrudRepository):
    @staticmethod
    @scalars
    def find_all():
        return (
            Role
            .select()
            .order_by(Role.key)
        )

    @staticmethod
    def _model():
        return Role


class UserRepository(CrudRepository):
    @staticmethod
    @scalars
    def find_all():
        return (
            User
            .select()
            .join(Role)
            .order_by(Role.key, User.username)
        )

    @staticmethod
    @scalar
    def find_by_username(username):
        return (
            User
            .select()
            .where(User.username == username)
        )

    @staticmethod
    @scalars
    def find_all_by_username_like(username):
        return (
            User
            .select()
            .join(Role)
            .where(User.username.like(f'%{username}%'))
            .order_by(Role.key, User.username)
        )

    @staticmethod
    def _model():
        return User


from starter.modules.users.models import User, Role
