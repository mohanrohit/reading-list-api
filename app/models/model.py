from app import db

from marshmallow import ValidationError

class Model(db.Model):
    __abstract__ = True

    @classmethod
    def all(cls):
        return cls.query.all()

    @classmethod
    def find(cls, id):
        return cls.query.get(id)

    @classmethod
    def find_one(cls, **params):
        return cls.query.filter_by(**params).first()

    @classmethod
    def exists(cls, **params):
        result = cls.find_one(**params)

        return True if result else False

    @classmethod
    def new(cls, params):
        try:
            model_params = cls.schema.load(params)
        except ValidationError as e:
            error_message = "; ".join([message for values in e.messages.values() for message in values])

            raise Exception(error_message)

        return cls(**model_params)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
