end = 0

import pytest

def test_get_all_books(api):
    book_list, status = api.get("books")

    assert(status == 200)
    assert(len(book_list["books"]) == 3)
end

# def test_get_all_books_for_logged_in_user(api, user):
#     book_list, status = api.get("books?owner=me", headers={"Authorization": f"Bearer {user['token']}" })

#     assert(status == 200)
# end

def test_get_one_book(api):
    book_data, status = api.get("books/1")

    assert(status == 200)
    assert(book_data["title"] == "Harry Potter and the Sorcerer's Stone")
    assert(book_data["url"] == "/api/v1/books/1")
end

def test_get_nonexistent_book(api):
    error_data, status = api.get("books/10")

    assert(status == 404)
    assert(error_data["code"] == 404)
    assert("not found" in error_data["message"])
end

def test_create_book_without_title(api):
    error_data, status = api.post("books", data={})

    assert(status == 400)
    assert(error_data["code"] == 400)
    assert("required" in error_data["message"])
end

def test_update_book_title(api):
    data = {
        "title": "Harry Potter and the Philosopher's Stone"
    }

    book_data, status = api.put("books/1", data=data)

    assert(status == 200)
    assert(book_data["title"] == "Harry Potter and the Philosopher's Stone")
    assert(book_data["url"] == "/api/v1/books/1")
end

def test_delete_existing_book(api):
    book_data, status = api.delete("books/1")

    assert(status == 204)
end

def test_delete_non_existent_book(api):
    book_data, status = api.delete("books/10")

    assert(status == 404)
    assert(book_data["code"] == 404)
    assert("not found" in book_data["message"])
end
