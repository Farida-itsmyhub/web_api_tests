import os
import pytest
from .BaseContext import BaseContext
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class WebTestContext(BaseContext):
    base_url: str = "https://reqres.in"
    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    @classmethod
    def teardown_class(cls):
        cls.driver.implicitly_wait(5)
        cls.driver.close()
        cls.driver.quit()
