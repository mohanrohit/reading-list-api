# books_controller.py -- the Books controller

from end_statement import end

from flask import request, render_template, url_for, redirect
from flask_classy import FlaskView, route

from app.models import Book

class BooksController(FlaskView):
  @route("/books") # GET /books
  def index(self):
    books = Book.query.all()

    return render_template("books/index.json", books=books)
  end

  @route("/books/<int:id>") # GET /books/<id>
  def get(self, id):
    book = Book.query.get(id)
    if not book:
      return render_template("error.json", error_code=404, error_message="No book with id {id} found.".format(id=id))
    end

    print book.data

    return render_template("books/get.json", book=book)
  end

  @route("/books", methods=["POST"]) # POST /books
  def post(self):
    book = Book()
    book.save()

    return render_template("books/get.json", book=book)
  end
end