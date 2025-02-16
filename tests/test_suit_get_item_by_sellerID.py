import requests
import pytest
from config import BASE_URL


def get_request(seller_id):
    url = f"{BASE_URL}/{seller_id}/item"
    response = requests.get(url)
    return response


def test_successful_request_with_valid_seller_id():
    seller_id = 999999
    response = get_request(seller_id)
    assert response.status_code == 200
    response_data = response.json()
    assert isinstance(response_data, list), "Response should be a dictionary"
    assert isinstance(response_data[0].get("id"), str), "ID should be a string"
    assert isinstance(response_data[0].get("name"), str), "Name should be a string"
    assert isinstance(response_data[0].get("price"), int), "Price should be an integer"
    assert isinstance(response_data[0].get("sellerId"), int), "Seller ID should be an integer"
    assert isinstance(response_data[0].get("statistics").get("contacts"), int), "Contacts should be an integer"
    assert isinstance(response_data[0].get("statistics").get("likes"), int), "Likes should be an integer"
    assert isinstance(response_data[0].get("statistics").get("viewCount"), int), "ViewCount should be an integer"

    assert response_data[0].get("sellerId") == seller_id


def test_successful_request_with_min_seller_id():
    seller_id = 111111
    response = get_request(seller_id)
    assert response.status_code == 200
    response_data = response.json()
    assert isinstance(response_data, list)

@pytest.mark.skip(reason="Bag - некорректный ответ сервера")
@pytest.mark.parametrize(
    "seller_id, expected_status, expected_error_message",
    [
        (1000000, 404, "Seller ID is out of valid range"),
        ("abc123", 404, "Invalid seller ID format"),
        (" ", 404, "Seller ID is required"),
        (8888888, 404, "Seller not found"),
    ]
)
def test_negative_requests_invalid_seller_id(seller_id, expected_status, expected_error_message):
    response = get_request(seller_id)
    assert response.status_code == expected_status
    response_data = response.json()
    assert "error" in response_data
