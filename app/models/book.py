# book.py -- the Book model

from end_statement import end

from abstract_model import Model, db

class Book(Model):
  __tablename__ = "books"

  id = db.Column(db.Integer, primary_key=True, index=True, unique=True, autoincrement=True)
  title = db.Column(db.String, nullable=False)

  def __init__(self, **kwargs):
    Model.__init__(self, **kwargs)
  end

  def __repr__(self):
    return self.title
  end
end
