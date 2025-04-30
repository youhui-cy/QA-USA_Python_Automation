import time

from selenium import webdriver
import data
import helpers
import pages
from pages import UrbanRoutesPage



webdriver.Chrome()

class TestUrbanRoutes:
    @classmethod
    def setup_class(cls):
        # do not modify - we need additional logging enabled in order to retrieve phone confirmation code
        from selenium.webdriver import DesiredCapabilities
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        cls.driver = webdriver.Chrome()
        # Add implicit waits for web elements to have time to load
        cls.driver.implicitly_wait(3)
        # Check if server is reachable
        if helpers.is_url_reachable(data.URBAN_ROUTES_URL):
            print("Connected to the Urban Routes server.")
        else:
            print("Cannot connect to Urban Routes. Check the server is on and still running.")

    def retrieve_sms_code(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = pages.UrbanRoutesPage(self.driver)
        routes_page.enter_sms_complete(self)


    @classmethod
    def teardown_class(cls):
        cls.driver.quit()