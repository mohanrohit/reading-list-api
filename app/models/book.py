from .model import Model, db

class Book(Model):
    __tablename__ = "books"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, index=True)
    title = db.Column(db.String(128), nullable=False)

    def __repr__(self):
        return f"Book ({self.title})"
