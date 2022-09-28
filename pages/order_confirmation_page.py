from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base


class OrderConfirmationPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    confirm_button = "//div[@id='Catalog']/a"
    success_message = "//div[@id='Content']/ul/li"

    # Getters
    def get_confirm_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.confirm_button)))

    def get_success_message(self):
        return WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, self.success_message)))

    # Actions
    def click_confirm_button(self):
        self.get_confirm_button().click()

    # Methods
    def check_order_success(self):
        self.get_current_url()
        self.assert_url("https://petstore.octoperf.com/actions/Order.action?newOrder=&confirmed=true")
        self.assert_text(self.get_success_message(), "Thank you, your order has been submitted.")
        self.create_screenshot()
        print("Order is completed successfully.")
