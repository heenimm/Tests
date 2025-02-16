import pytest
import requests
from config import BASE_URL
import allure

@allure.step("Отправляем GET-запрос с id: {}")
def get_request(id):
    endpoint = "item"
    url = f"{BASE_URL}/{endpoint}"
    response = requests.get(f"{url}/{id}")
    return response

@pytest.mark.parametrize("id", [
    "6359a483-dae8-4231-adc8-c71c5f1eb401",
    "8d954969-0c55-4b50-af0b-00115a280ef7"
])
def test_successful_request_with_valid_id(id):
    response = get_request(id)
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"

    data = response.json()
    with allure.step("Проверяем статус-код"):
        assert isinstance(data, list), "Response should be a dictionary"
        assert isinstance(data[0].get("id"), str), "ID should be a string"
        assert isinstance(data[0].get("name"), str), "Name should be a string"
        assert isinstance(data[0].get("price"), int), "Price should be an integer"
        assert isinstance(data[0].get("sellerId"), int), "Seller ID should be an integer"
        assert isinstance(data[0].get("statistics").get("contacts"), int), "Contacts should be an integer"
        assert isinstance(data[0].get("statistics").get("likes"), int), "Likes should be an integer"
        assert isinstance(data[0].get("statistics").get("viewCount"), int), "ViewCount should be an integer"

@pytest.mark.skip(reason="Bag - некорректный ответ сервера")
@pytest.mark.parametrize("id, expected_status_code", [
    ("999", 404),
    (" ", 404),
    (999, 404)
])
def test_negative_requests_with_invalid_id(id, expected_status_code):
    response = get_request(id)
    response_data = response.json()

    assert response.status_code == expected_status_code, f"Expected status code {expected_status_code}, but got {response.status_code}"
    assert f"item {id} not found" == response_data.get("result").get("message"), "Error message should indicate not found"

