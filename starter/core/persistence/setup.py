def install():
    db.drop_all()
    db.create_all()

    with db.Session() as session:
        role_admin = Role(key='ADMIN', name='ADMIN')
        session.add(role_admin)

        role_user = Role(key='USER', name='FELHASZNÁLÓ')
        session.add(role_user)

        user = User()
        user.username = 'admin'
        user.password = 'Admin123.'
        user.role = role_admin
        session.add(user)

        session.commit()


from starter.core.persistence import db
from starter.modules.users.models import Role, User
