from .user import user_schema, users_schema
from .book import book_schema, books_schema
from .user_book import user_book_schema, user_books_schema
from .login import login_schema

schemas = {
    "User": user_schema,
    "Book": book_schema,
    "UserBook": user_book_schema
}
