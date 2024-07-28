from abc import ABC, abstractmethod

from flask import g

from starter.core import local_now


class CrudRepository(ABC):
    @staticmethod
    @abstractmethod
    def find_all():
        raise NotImplementedError()

    @classmethod
    def find_by_id(cls, entity_id):
        return g.session.get(cls._model(), entity_id)

    @staticmethod
    def save(entity):
        now = local_now()

        if not entity.id:
            if hasattr(entity, 'created_at'):
                entity.created_at = now

            if hasattr(entity, 'created_by') and g.user:
                entity.created_by = g.user.id

        if hasattr(entity, 'modified_at'):
            entity.modified_at = now

        if hasattr(entity, 'modified_by') and g.user:
            entity.modified_by = g.user.id

        if not entity.id:
            g.session.add(entity)

        try:
            g.session.commit()
        except Exception as err:
            g.session.rollback()
            raise err

        return entity

    @staticmethod
    def delete(entity):
        g.session.delete(entity)

        try:
            g.session.commit()
        except Exception as err:
            g.session.rollback()
            raise err

    @staticmethod
    @abstractmethod
    def _model():
        raise NotImplementedError()
