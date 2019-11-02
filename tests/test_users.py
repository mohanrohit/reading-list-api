end = 0

import pytest

import json

def test_get_all_users(test_client, init_db):
    response = test_client.get("/api/v1/users")
    assert(response.status_code == 200)

    user_list = json.loads(response.data)["users"]

    assert(len(user_list) == 4)
end

def test_get_one_user(test_client, init_db):
    response = test_client.get("/api/v1/users/1")
    assert(response.status_code == 200)

    user_data = json.loads(response.data)

    assert(user_data["url"] == "/api/v1/users/1")
    assert(user_data["first_name"] == "Albert")
end

def test_create_inactive_user(test_client, init_db):
    headers = { "Content-Type": "application/json" }

    data = {
        "first_name": "Isaac",
        "last_name": "Newton",
        "email": "apples@me.com",
        "is_active": False
    }

    response = test_client.post("/api/v1/users", headers=headers, data=json.dumps(data))

    user_data = json.loads(response.data)

    assert(user_data["first_name"] == "Isaac")
    assert(user_data["last_name"] == "Newton")
    assert(user_data["email"] == "apples@me.com")
    assert(user_data["is_active"] == False)
end

def test_create_active_user(test_client, init_db):
    headers = { "Content-Type": "application/json" }

    data = {
        "first_name": "Galileo",
        "last_name": "Galilei",
        "email": "pisa@me.com",
        "is_active": True
    }

    response = test_client.post("/api/v1/users", headers=headers, data=json.dumps(data))

    user_data = json.loads(response.data)

    assert(user_data["first_name"] == "Galileo")
    assert(user_data["last_name"] == "Galilei")
    assert(user_data["email"] == "pisa@me.com")
    assert(user_data["is_active"] == True)
end
