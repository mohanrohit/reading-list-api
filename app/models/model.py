end = 0

from app import db

from marshmallow import ValidationError

from app.schemas import schemas

class Model(db.Model):
    __abstract__ = True

    @classmethod
    def all(cls, **params):
        if params:
            return cls.query.filter_by(**params)

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
    end

    @classmethod
    def new(cls, params):
        if not cls.__name__ in schemas:
            raise Exception(f"No schema is defined for class {cls.__name__}")
        end

        try:
            model_params = schemas[cls.__name__].load(params)
        except ValidationError as e:
            error_message = "; ".join([message for values in e.messages.values() for message in values])

            raise Exception(error_message)
        end

        return cls(**model_params)

    def save(self):
        db.session.add(self)
        db.session.commit()

        return self

    def delete(self):
        db.session.delete(self)
        db.session.commit()

        return self
