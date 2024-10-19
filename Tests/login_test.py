from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("setup")
class TestLogin:
    driver = None

    def test_navigate_to_login_page(self):
        self.driver.find_element(By.XPATH, '//*[@id="top-links"]/ul/li[2]/a').click()
        self.driver.find_element(By.XPATH, '//*[@id="top-links"]/ul/li[2]/ul/li[2]/a').click()
        assert self.driver.find_element(By.XPATH, '//*[@id="content"]/div/div[2]/div/h2').is_displayed()


