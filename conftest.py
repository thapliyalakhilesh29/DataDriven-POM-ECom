import pytest
from selenium import webdriver


@pytest.fixture(scope='class')
def setup(request):
    driver = webdriver.Chrome()
    driver.maximize_window()
    request.cls.driver = driver
    driver.get('https://tutorialsninja.com/demo')
    yield
    driver.quit()
