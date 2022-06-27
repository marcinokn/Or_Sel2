# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class Test1():
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_1(self):
        self.driver.get("https://www.google.pl/")
        self.driver.set_window_size(1597, 1012)
        self.driver.find_element(By.CSS_SELECTOR, "#L2AGLb > .QS5gu").click()
        self.driver.find_element(By.NAME, "q").click()
        self.driver.find_element(By.NAME, "q").send_keys("bilety do kina")
        time.sleep(3)
        self.driver.find_element(By.NAME, "q").send_keys(Keys.ARROW_DOWN)
        self.driver.find_element(By.NAME, "q").send_keys(Keys.ARROW_DOWN)
        self.driver.find_element(By.NAME, "q").send_keys(Keys.ARROW_DOWN)
        time.sleep(3)
        self.driver.find_element(By.NAME, "q").send_keys(Keys.ARROW_DOWN)
        self.driver.find_element(By.NAME, "q").send_keys(Keys.ENTER)
        # self.driver.find_element(By.CLASS_NAME, "wM6W7d").click()
        time.sleep(10)
        # self.driver.find_element(By.NAME, "q").send_keys(Keys.ENTER)
        # self.driver.find_element(By.CSS_SELECTOR, ".g:nth-child(16) .LC20lb").click()
        # self.driver.find_element(By.CSS_SELECTOR, ".cookies-wrapp").click()
        # self.driver.find_element(By.ID, "cookie-accep").click()
        # self.driver.find_element(By.LINK_TEXT, "Pyrkon").click()
        self.driver.close()
