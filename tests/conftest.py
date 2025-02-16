import pytest
import allure
from datetime import datetime

@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    if not config.option.allure_report_dir:
        config.option.allure_report_dir = "allure-results"

@pytest.fixture(scope="function", autouse=True)
def add_allure_environment_property(request):
    """Фикстура для добавления информации об окружении в Allure."""
    # allure.environment(
    #     tester="Ваше Имя",
    #     environment="Тестовый",
    #     browser="Chrome",
    #     date=str(datetime.now())
    # )
