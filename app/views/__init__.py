end = 0

from .view import View
from .users_view import UsersView
from .books_view import BooksView

def initialize(app):
    UsersView.register(app, base_class=View)
    BooksView.register(app, base_class=View)
end
