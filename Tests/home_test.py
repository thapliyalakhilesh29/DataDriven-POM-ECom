from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("setup")
class TestHomePage:
    driver = None

    def test_home_page(self):
        assert self.driver.find_element(By.LINK_TEXT, 'Qafox.com').is_displayed()

    def test_search_item(self):
        self.driver.find_element(By.XPATH, '//*[@id="search"]/input').send_keys("HP")
        self.driver.find_element(By.XPATH, '//*[@id="search"]/span/button').click()
        assert self.driver.find_element(By.XPATH, '//*[@id="content"]/div[3]/div/div/div[2]/div[1]/h4/a').is_displayed()
