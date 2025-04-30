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

    def test_set_route(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = pages.UrbanRoutesPage(self.driver)
        routes_page.enter_locations(data.ADDRESS_FROM, data.ADDRESS_TO)
        time.sleep(3)
        assert routes_page.get_from() == data.ADDRESS_FROM
        assert routes_page.get_to() == data.ADDRESS_TO



    def test_select_plan(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.enter_locations(data.ADDRESS_FROM, data.ADDRESS_TO)
        time.sleep(1)
        routes_page.plan_selection()
        time.sleep(1)
        assert routes_page.get_current_selected_plan() == 'Supportive'

    def test_fill_phone_number(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.enter_locations(data.ADDRESS_FROM, data.ADDRESS_TO)
        time.sleep(1)
        routes_page.plan_selection()
        #time.sleep(1)
        routes_page.click_phone_button()
        time.sleep(1)
        routes_page.enter_phone_number(data.PHONE_NUMBER)
        routes_page.click_next()
        #sms_code = helpers.retrieve_phone_code(self.driver)
        routes_page.enter_sms_complete()
        routes_page.sms_confirm()
        #routes_page.click_close_card()
        assert routes_page.get_phone_number() == data.PHONE_NUMBER


    def test_fill_card(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.enter_locations(data.ADDRESS_FROM, data.ADDRESS_TO)
        time.sleep(1)
        routes_page.plan_selection()
        time.sleep(1)
        routes_page.click_add_payment()
        routes_page.select_credit_card()
        routes_page.enter_card_number(data.CARD_NUMBER)
        routes_page.enter_card_code(data.CARD_CODE)
        routes_page.click_link()
        routes_page.click_close_card()
        assert routes_page.get_payment_method() == 'Card'



    def test_comment_for_driver(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.enter_locations(data.ADDRESS_FROM, data.ADDRESS_TO)
        time.sleep(1)
        routes_page.plan_selection()
        time.sleep(1)
        routes_page.message_driver(data.MESSAGE_FOR_DRIVER)
        time.sleep(1)
        assert routes_page.get_message_driver() == data.MESSAGE_FOR_DRIVER

    def test_order_blanket_and_handkerchiefs(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.enter_locations(data.ADDRESS_FROM, data.ADDRESS_TO)
        time.sleep(1)
        routes_page.plan_selection()
        time.sleep(1)
        routes_page.order_blanket()
        time.sleep(1)
        assert routes_page.blanket_checked()


    def test_order_2_ice_creams(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.enter_locations(data.ADDRESS_FROM, data.ADDRESS_TO)
        time.sleep(1)
        routes_page.plan_selection()
        time.sleep(3)
        number_of_ice_creams = 2
        for count in range(number_of_ice_creams):
            routes_page.order_icecream()
            time.sleep(1)
        assert int(routes_page.count_ice_cream()) == 2


    def test_car_search_model_appears(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.enter_locations(data.ADDRESS_FROM, data.ADDRESS_TO)
        time.sleep(1)
        routes_page.plan_selection()
        time.sleep(1)
        routes_page.message_driver(data.MESSAGE_FOR_DRIVER)
        time.sleep(1)
        routes_page.car_order()
        assert routes_page.get_car_search() == 'Car search'

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()