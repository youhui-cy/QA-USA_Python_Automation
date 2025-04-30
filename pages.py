import time

from selenium.webdriver import Keys
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from helpers import retrieve_phone_code

# Defining the page class, locators and method in the class
class UrbanRoutesPage:
    # Locators as class attributes
    FROM_LOCATOR = (By.ID, 'from')
    TO_LOCATOR = (By.XPATH, '//*[@id="to"]')
    # Tariffs Locators
    SUPPORTIVE_PLAN_CARD = (By.XPATH, '//div[text()="Supportive"]')
    SUPPORTIVE_PLAN_CARD_PARENT = (By.XPATH, '//div[text()="Supportive"]//..')
    ACTIVE_PLAN_CARD = (By.XPATH, '//div[@class="tcard active"]//div[@class="tcard-title"]')
    CALL_TAXI_BUTTON = (By.XPATH, '//button[contains(text(), "Call a taxi")]')
    PHONE_BUTTON = (By.CLASS_NAME, 'np-text')
    PHONE_FIELD_LOCATOR = (By.ID, 'phone') #(By.XPATH, '//div[@id="phone"]//div[@class="input"]')
    PHONE_NEXT_BUTTON = (By.XPATH, '//button[contains(text(), "Next")]')
    SMS_FIELD_LOCATOR = (By.ID, 'code')
    SMS_CODE_CONFIRM_LOCATOR = (By.XPATH, '//button[contains(text(), "Confirm")]')
    ADD_PAYMENT_METHOD_LOCATOR = (By.XPATH, '//div[@class="pp-value-text"]')
    CREDIT_CARD_LOCATOR = (By.XPATH, '//div[text()="Add card"]')
    CARD_NUMBER_LOCATOR = (By.ID, 'number')
    CARD_CODE_LOCATOR = (By.CSS_SELECTOR, '#code.card-input')
    LINK_CARD_LOCATOR = (By.XPATH, '//button[contains(text(), "Link")]')
    CARD_PAYMENT_LOCATOR = (By.XPATH, '//div[@class="pp-title"], //div[text()="Card"]')
    CLOSE_CARD_BUTTON_LOCATOR = (By.XPATH, '//div[@class="payment-picker open"]//button[@class="close-button section-close"]')
    MESSAGE_FIELD_LOCATOR = (By.ID, 'comment')
    BLANKET_SLIDER_LOCATOR = (By.XPATH, '//span[@class="slider round"][1]')
    # SWITCH_INPUT_LOCATOR = (By.XPATH, "//div[contains(text(), 'Blanket and handkerchiefs')]/following-sibling::div//input[@type='checkbox']")
    SWITCH_INPUT_LOCATOR = (By.XPATH, '(//input[@type="checkbox"])[2]')
    ICE_CREAM_PLUS_LOCATOR = (By.XPATH, "//div[contains(@class, 'counter-plus') and text()='+']")
    #(By.XPATH, '//div[contains(text(),"Ice-cream"]//div[contains(text(), "+"]')
    ICE_CREAM_COUNTER = (By.XPATH, "//div[contains(@class, 'counter-label') and text()='Ice cream']/../..//div[@class='counter-value']")
    #(By.XPATH, '//div[@class="counter-value"]//div[contains(text(),"Ice-cream"]')
    CAR_ORDER_LOCATOR = (By.XPATH, '//div[@class="smart-button-wrapper"]')
    CAR_SEARCH_LOCATOR = (By.CLASS_NAME, 'order-header-title')



    def __init__(self, driver):
        self.driver = driver  # Initialize the driver

    def enter_from_location(self, from_text):
        # Enter From
       self.driver.find_element(*self.FROM_LOCATOR).send_keys(from_text)

    def enter_to_location(self, to_text):
        # Enter To
        self.driver.find_element(*self.TO_LOCATOR).send_keys(to_text)

    # Get value FROM and TO fields
    def get_from(self):
        return self.driver.find_element(*self.FROM_LOCATOR).get_property('value')

    def get_to(self):
        return self.driver.find_element(*self.TO_LOCATOR).get_property('value')

    def click_call_a_taxi(self):
        # Click Call a taxi button
        self.driver.find_element(*self.CALL_TAXI_BUTTON).click()

    def select_supportive_plan(self):
        # Click Supportive tariff
        self.driver.find_element(*self.SUPPORTIVE_PLAN_CARD).click()

    def get_current_selected_plan(self):
        # Return the "Supportive" text
        return self.driver.find_element(*self.ACTIVE_PLAN_CARD).text

    def get_phone_number(self):
        # Get value from Phone Field
        return self.driver.find_element(*self.PHONE_BUTTON).text

    def click_phone_button(self):
        # Click on Phone Number Input Field to Open Phone Number screen
        self.driver.find_element(*self.PHONE_BUTTON).click()

    def enter_phone_number(self, phone_number):
        # Fill number in Phone Number Input Field
        self.driver.find_element(*self.PHONE_FIELD_LOCATOR).send_keys(phone_number)

    def click_next(self):
        # Click Next after entering phone number
        self.driver.find_element(*self.PHONE_NEXT_BUTTON).click()

    def enter_sms_complete(self):
        # Get and Enter SMS confirmation code
        sms_text = retrieve_phone_code(self.driver)
        print(f"Retrieved SMS code: {sms_text}")  # Add this line
        self.driver.find_element(*self.SMS_FIELD_LOCATOR).send_keys(sms_text)

    def sms_confirm(self):
        # Click to confirm SMS code
        self.driver.find_element(*self.SMS_CODE_CONFIRM_LOCATOR).click()

    def click_add_payment(self):
        # Click on Payment Method to open Payment Screen
        self.driver.find_element(*self.ADD_PAYMENT_METHOD_LOCATOR).click()

    def select_credit_card(self):
        # Click to Select Credit Card
        self.driver.find_element(*self.CREDIT_CARD_LOCATOR).click()

    def enter_card_number(self, card_number):
        # Enter Card Number in Field
        self.driver.find_element(*self.CARD_NUMBER_LOCATOR).send_keys(card_number)

    def enter_card_code(self, card_code):
        # Enter CVV code in Field
        self.driver.find_element(*self.CARD_CODE_LOCATOR).send_keys(card_code)

    def click_link(self):
        # Click to Link CC to Acct.
        self.driver.find_element(*self.CARD_CODE_LOCATOR).send_keys(Keys.TAB)
        self.driver.find_element(*self.LINK_CARD_LOCATOR).click()

    def get_payment_method(self):
        # Check if Payment Method is using Card
        return self.driver.find_element(*self.ADD_PAYMENT_METHOD_LOCATOR).text

    def click_close_card(self):
        # Click to Close Payment Screen
        self.driver.find_element(*self.CLOSE_CARD_BUTTON_LOCATOR).click()

    def message_driver(self, driver_message):
        # Fill in Message to Driver
        self.driver.find_element(*self.MESSAGE_FIELD_LOCATOR).send_keys(driver_message)

    def get_message_driver(self):
        # Get message to driver text
        return self.driver.find_element(*self.MESSAGE_FIELD_LOCATOR).get_property('value')

    def order_blanket(self):
        # Click on the Blanket slider
        self.driver.find_element(*self.BLANKET_SLIDER_LOCATOR).click()

    def blanket_checked(self):
        # Assert Blanket switch checked
        return self.driver.find_element(*self.SWITCH_INPUT_LOCATOR).get_property('checked')

    def order_icecream(self):
        # Add ice-cream to order
        self.driver.find_element(*self.ICE_CREAM_PLUS_LOCATOR).click()

    def count_ice_cream(self):
        return self.driver.find_element(*self.ICE_CREAM_COUNTER).text

    def car_order(self):
        # Click on Car Order
        self.driver.find_element(*self.CAR_ORDER_LOCATOR).click()

    def get_car_search(self):
        return self.driver.find_element(*self.CAR_SEARCH_LOCATOR).text

    # Step to enter both "From" and "To" locations
    def enter_locations(self, from_text, to_text):
        self.enter_from_location(from_text)
        self.enter_to_location(to_text)
        time.sleep(1)
        self.click_call_a_taxi()

    def plan_selection(self):
        self.select_supportive_plan()