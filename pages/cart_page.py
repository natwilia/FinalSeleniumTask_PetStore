from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base


class CartPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    list_price = "//div[@id='Cart']/form/table/tbody/tr[2]/td[6]"
    total_cost = "//div[@id='Cart']/form/table/tbody/tr[2]/td[7]"
    quantity_field = "//input[@name='EST-16']"
    update_cart_button = "//input[@name='updateCartQuantities']"
    proceed_to_checkout_button = "//div[@id='Cart']/a"

    # Getters
    def get_list_price(self):
        return WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, self.list_price)))

    def get_total_cost(self):
        return WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, self.total_cost)))

    def get_quantity_field(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.quantity_field)))

    def get_update_cart_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.update_cart_button)))

    def get_proceed_to_checkout_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.proceed_to_checkout_button)))

    # Actions
    def input_quantity(self, quantity):
        self.get_quantity_field().send_keys(quantity)

    def click_update_cart_button(self):
        self.get_update_cart_button().click()

    def click_proceed_to_checkout_button(self):
        self.get_proceed_to_checkout_button().click()

    # Methods
    def change_quantity(self):
        self.get_current_url()
        quantity_field = self.driver.find_element(By.XPATH, self.quantity_field)
        quantity_field.send_keys(Keys.CONTROL + "a")
        quantity_field.send_keys(Keys.DELETE)
        self.input_quantity("2")
        self.click_update_cart_button()
        pet_price = "{:.2f}".format(float(self.get_list_price().text[1:]))
        total_pet_price = "{:.2f}".format(float(pet_price) * 2)
        assert self.get_total_cost().text == "$" + total_pet_price
        print(f"Total price is calculated correctly: ${pet_price} * 2 = ${total_pet_price}.")
