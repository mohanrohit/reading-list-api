end = 0

import pytest

import json
import api

def test_get_all_users(test_client, init_db):
    user_list, status = api.get(test_client, "users")

    assert(status == 200)
    assert(len(user_list["users"]) == 4)
end

def test_get_one_user(test_client, init_db):
    user_data, status = api.get(test_client, "users/1")

    assert(status == 200)
    assert(user_data["url"] == "/api/v1/users/1")
    assert(user_data["first_name"] == "Albert")
end

def test_create_inactive_user(test_client, init_db):
    data = {
        "first_name": "Isaac",
        "last_name": "Newton",
        "email": "apples@me.com",
        "is_active": False
    }

    user_data, status = api.post(test_client, "users", data=data)

    assert(status == 201)
    assert(user_data["first_name"] == "Isaac")
    assert(user_data["last_name"] == "Newton")
    assert(user_data["email"] == "apples@me.com")
    assert(user_data["is_active"] == False)
end

def test_create_active_user(test_client, init_db):
    data = {
        "first_name": "Galileo",
        "last_name": "Galilei",
        "email": "pisa@me.com",
        "is_active": True
    }

    user_data, status = api.post(test_client, "users", data=data)

    assert(status == 201)
    assert(user_data["first_name"] == "Galileo")
    assert(user_data["last_name"] == "Galilei")
    assert(user_data["email"] == "pisa@me.com")
    assert(user_data["is_active"] == True)
end

def test_create_new_user_without_first_name(test_client, init_db):
    data = {
        "last_name": "Copernicus",
        "email": "nicky@me.com",
        "is_active": False
    }

    error_data, status = api.post(test_client, "users", data=data)

    assert(status == 400)
    assert(error_data["code"] == 400)
    assert("required" in error_data["message"])
end

def test_add_new_book_to_user(test_client, init_db):
    data = {
        "title": "Harry Potter and the Goblet of Fire"
    }

    book_data, status = api.post(test_client, "users/1/books", data=data)

    assert(status == 201)
    assert(book_data["title"] == "Harry Potter and the Goblet of Fire")
    assert(book_data["is_read"] == False)
end

def test_add_existing_book_to_user(test_client, init_db):
    data = {
        "book_id": 1
    }

    book_data, status = api.post(test_client, "users/1/books", data=data)

    assert(status == 201)
    assert(book_data["title"] == "Harry Potter and the Sorcerer's Stone")
    assert(book_data["is_read"] == False)
end
