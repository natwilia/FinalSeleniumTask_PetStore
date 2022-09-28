from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base


class PaymentPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    card_number = "//input[@name='order.creditCard']"
    expiry_date = "//input[@name='order.expiryDate']"
    continue_button = "//input[@name='newOrder']"

    # Getters
    def get_card_number(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.card_number)))

    def get_expiry_date(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.expiry_date)))

    def get_continue_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.continue_button)))

    # Actions
    def input_card_number(self, card_number):
        self.get_card_number().send_keys(card_number)

    def input_expiry_date(self, expiry_date):
        self.get_expiry_date().send_keys(expiry_date)

    def click_continue_button(self):
        self.get_continue_button().click()

    # Methods
    def enter_payment_data(self):
        self.get_current_url()
        self.assert_url("https://petstore.octoperf.com/actions/Order.action?newOrderForm=")
        card_number = self.driver.find_element(By.XPATH, self.card_number)
        card_number.send_keys(Keys.CONTROL + "a")
        card_number.send_keys(Keys.DELETE)
        self.input_card_number("4242424242424242")
        expiry_date = self.driver.find_element(By.XPATH, self.expiry_date)
        expiry_date.send_keys(Keys.CONTROL + "a")
        expiry_date.send_keys(Keys.DELETE)
        self.input_expiry_date("10/25")
