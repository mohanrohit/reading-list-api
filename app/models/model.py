from app import db

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

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
