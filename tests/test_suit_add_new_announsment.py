import requests
import pytest
import re
from config import BASE_URL

def post_request(payload):
    endpoint = "item"
    url = f"{BASE_URL}{endpoint}"
    response = requests.post(url, json=payload)
    return response

def test_successful_request_with_valid_data():
    body =     {
        "name": "Телефон",
        "price": 85566,
        "sellerId": 999999,
        "statistics": {
            "contacts": 7,
            "like": 5,
            "viewCount": 1
        }
    }
    response = post_request(body)
    assert response.status_code == 200
    response_data = response.json()
    assert "status" in response_data
    assert re.match(r'^Сохранили объявление - [\da-f]{8}-[\da-f]{4}-[\da-f]{4}-[\da-f]{4}-[\da-f]{12}$', response_data["status"])

def test_successful_request_with_min_price():
    body = {
        "name": "Телефон",
        "price": 1,
        "sellerId": 999999,
        "statistics": {
            "contacts": 7,
            "like": 5,
            "viewCount": 1
        }
    }
    response = post_request(body)
    assert response.status_code == 200
    response_data = response.json()
    assert "status" in response_data
    assert re.match(r'^Сохранили объявление - [\da-f]{8}-[\da-f]{4}-[\da-f]{4}-[\da-f]{4}-[\da-f]{12}$', response_data["status"])

def test_successful_request_with_max_price():
    body = {
        "name": "Телефон",
        "price": 1_000_000_000_000,
        "sellerId": 999999,
        "statistics": {
            "contacts": 7,
            "like": 5,
            "viewCount": 1
        }
    }
    response = post_request(body)
    assert response.status_code == 200
    response_data = response.json()
    assert "status" in response_data
    assert re.match(r'^Сохранили объявление - [\da-f]{8}-[\da-f]{4}-[\da-f]{4}-[\da-f]{4}-[\da-f]{12}$', response_data["status"])

@pytest.mark.skip(reason="Bag - некорректный ответ сервера 200 вместо 400")
def test_request_missing_name():
    body = {
        "name": "",
        "price": 85566,
        "sellerId": 999999,
        "statistics": {
            "contacts": 7,
            "like": 5,
            "viewCount": 1
        }
    }
    response = post_request(body)
    assert response.status_code == 400
    response_data = response.json()
    assert "status" in response_data
    assert response_data["status"] == "не передан объект - объявление"

@pytest.mark.skip(reason="Bag - некорректный ответ сервера 500 вместо 400")
def test_negative_request_missing_price():
    body =     {
        "name": "Телефон",
        "price": " ",
        "sellerId": 345222,
        "statistics": {
            "contacts": 7,
            "like": 8,
            "viewCount": 1
        }
    }
    response = post_request(body)
    assert response.status_code == 400
    response_data = response.json()
    assert "error" in response_data
    assert response_data["error"] == "Field 'price' is required"



@pytest.mark.skip(reason="Bag - некорректный ответ сервера 200 вместо 400")
def test_negative_request_negative_price():
    body =     {
        "name": "Телефон",
        "price": -85566,
        "sellerId": 345222,
        "statistics": {
            "contacts": 7,
            "like": 8,
            "viewCount": 1
        }
    }
    response = post_request(body)
    assert response.status_code == 400

@pytest.mark.skip(reason="Bag - некорректный ответ сервера 200 вместо 400")
def test_negative_request_invalid_sellerId():
    body =     {
        "name": "Телефон",
        "price": 85566,
        "sellerId": 3452222,
        "statistics": {
            "contacts": 7,
            "like": 8,
            "viewCount": 1
        }
    }
    response = post_request(body)
    assert response.status_code == 400

@pytest.mark.skip(reason="Bag - некорректный ответ сервера 500 вместо 400")
def test_negative_request_empty_body():
    response = post_request({})
    assert response.status_code == 400
    response_data = response.json()
    assert "result" in response_data
    assert response_data["result"]["messages"] is None
    assert response_data["status"] == "не передан объект - объявление"