from .model import Model, db

class UserBook(Model):
    __tablename__ = "user_books"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, index=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    book_id = db.Column(db.Integer, db.ForeignKey("books.id"))

    def __repr__(self):
        return f"UserBook user_id: {self.user_id} book_id: {self.book_id}"
