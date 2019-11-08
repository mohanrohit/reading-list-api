end = 0

import pytest

def incomplete_user_data():
    data = [
        { "last_name": "Copernicus", "email": "nicky@me.com", "password": "P@55w0rd", "is_active": False },
        { "first_name": "Nicolas", "email": "nicky@me.com", "password": "P@55w0rd", "is_active": False },
        { "first_name": "Nicolas", "last_name": "Copernicus", "password": "P@55w0rd", "is_active": False },
        { "first_name": "Nicolas", "last_name": "Copernicus", "email": "nicky@me.com", "is_active": False }
    ]

    return data
end

def test_get_all_users(api):
    user_list, status = api.get("users")

    assert(status == 200)
    assert(len(user_list["users"]) == 4)
end

def test_get_one_user(api):
    user_data, status = api.get("users/1")

    assert(status == 200)
    assert(user_data["url"] == "/api/v1/users/1")
    assert(user_data["first_name"] == "Albert")
end

def test_create_inactive_user(api):
    data = {
        "first_name": "Isaac",
        "last_name": "Newton",
        "email": "apples@me.com",
        "password": "P@55w0rd",
        "is_active": False
    }

    user_data, status = api.post("users", data=data)

    assert(status == 201)
    assert(user_data["first_name"] == "Isaac")
    assert(user_data["last_name"] == "Newton")
    assert(user_data["email"] == "apples@me.com")
    assert(user_data["is_active"] == False)
end

def test_create_active_user(api):
    data = {
        "first_name": "Galileo",
        "last_name": "Galilei",
        "password": "P@55w0rd",
        "email": "pisa@me.com",
        "is_active": True
    }

    user_data, status = api.post("users", data=data)

    assert(status == 201)
    assert(user_data["first_name"] == "Galileo")
    assert(user_data["last_name"] == "Galilei")
    assert(user_data["email"] == "pisa@me.com")
    assert(user_data["is_active"] == True)
end

@pytest.mark.parametrize("user_data", incomplete_user_data())
def test_create_user_with_missing_required_field(api, user_data):
    error_data, status = api.post("users", data=user_data)

    assert(status == 400)
    assert(error_data["code"] == 400)
    assert("required" in error_data["message"])
end

def test_add_new_book_to_user(api):
    data = {
        "title": "Harry Potter and the Goblet of Fire"
    }

    book_data, status = api.post("users/1/books", data=data)

    assert(status == 201)
    assert(book_data["title"] == "Harry Potter and the Goblet of Fire")
    assert(book_data["is_read"] == False)
end

def test_add_existing_book_to_user(api):
    data = {
        "book_id": 2
    }

    book_data, status = api.post("users/1/books", data=data)

    assert(status == 201)
    assert(book_data["title"] == "Harry Potter and the Chamber of Secrets")
    assert(book_data["is_read"] == False)
end

@pytest.mark.parametrize("read_status", [True, False])
def test_set_book_read(api, read_status):
    data = {
        "is_read": read_status
    }

    book_data, status = api.put("users/1/books/2", data)

    assert(status == 200)
    assert(book_data["url"] == "/api/v1/books/2")
    assert(book_data["is_read"] == read_status)
end

@pytest.mark.parametrize("read_status", [True, False])
def test_set_non_existent_book_read(api, read_status):
    data = {
        "is_read": read_status
    }

    error_data, status = api.put("users/1/books/10", data)

    assert(status == 400)
    assert(error_data["code"] == 400)
    assert("not found" in error_data["message"])
end

@pytest.mark.parametrize("read_status", [True, False])
def test_set_unowned_book_read(api, read_status):
    data = {
        "is_read": read_status
    }

    error_data, status = api.put("users/1/books/3", data)

    assert(status == 400)
    assert(error_data["code"] == 400)
    assert("does not have" in error_data["message"])
end

@pytest.mark.parametrize("read_status", [True, False])
def test_set_book_read_for_non_existent_user(api, read_status):
    data = {
        "is_read": read_status
    }

    error_data, status = api.put("users/10/books/3", data)

    assert(status == 404)
    assert(error_data["code"] == 404)
    assert("not found" in error_data["message"])
end

def test_delete_existing_user(api):
    user_data, status = api.delete("users/1")

    assert(status == 204)
end

def test_delete_non_existent_user(api):
    error_data, status = api.delete("users/10")

    assert(status == 404)
    assert(error_data["code"] == 404)
    assert("not found" in error_data["message"])
end
