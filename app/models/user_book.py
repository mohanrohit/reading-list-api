from .model import Model, db

class UserBook(Model):
    __tablename__ = "user_books"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, index=True)

    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    book_id = db.Column(db.Integer, db.ForeignKey("books.id"))
    is_read = db.Column(db.Boolean, default=False)

    user = db.relationship("User")
    book = db.relationship("Book")

    def __repr__(self):
        return f"UserBook (user: {self.user.email} book: {self.book.title})"
