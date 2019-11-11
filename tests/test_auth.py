end = 0

import os

import jwt
import pytest

def test_register_new_user(api):
    data = {
        "first_name": "Emmy",
        "last_name": "Noether",
        "email": "noether@me.com",
        "password": "P@55w0rd"
    }

    auth_data, status = api.post("auth/register", data=data)

    assert(status == 201)
    assert(auth_data["email"] == "noether@me.com")
    assert(auth_data["verification_code"] == 197402) # dummy code for now
    assert(auth_data["is_active"] == False)
end

def test_login_user(api):
    data = {
        "email": "frizzy@me.com",
        "password": "P@55w0rd"
    }

    auth_data, status = api.post("auth/login", data=data)

    token = jwt.decode(auth_data["token"], os.getenv("JWT_SECRET"), algorithms=["HS256"])

    assert(status == 200)
    assert(token["sub"] == "frizzy@me.com")
end

invalid_credentials = [
    { "email": "dummy@me.com", "password": "P@55w0rd" }, # non-existent user
    { "email": "frizzy@me.com", "password": "invalid" } # incorrect password
]

@pytest.mark.parametrize("invalid_credentials", invalid_credentials)
def test_login_with_invalid_credentials(api, invalid_credentials):
    error_data, status = api.post("auth/login", data=invalid_credentials)

    assert(status == 400)
    assert(error_data["code"] == 400)
    assert("incorrect" in error_data["message"])
end

missing_credentials = [
    { "password": "P@55w0rd" }, # missing email
    { "email": "frizzy@me.com" } # missing password
]

@pytest.mark.parametrize("missing_credentials", missing_credentials)
def test_login_with_missing_credentials(api, missing_credentials):
    error_data, status = api.post("auth/login", data=missing_credentials)

    assert(status == 400)
    assert(error_data["code"] == 400)
    assert("required" in error_data["message"])
end
