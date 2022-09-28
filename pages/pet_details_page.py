from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base


class PetDetailsPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    persian_cat = "//div[@id='Catalog']/table/tbody/tr[3]/td[1]/a"
    persian_female_cat = "//div[@id='Catalog']/table/tbody/tr[2]/td[1]/a"
    add_to_cart_button = "//div[@id='Catalog']/table/tbody/tr[7]/td/a"

    # Getters
    def get_persian_cat(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.persian_cat)))

    def get_persian_female_cat(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.persian_female_cat)))

    def get_add_to_cart_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.add_to_cart_button)))

    # Actions
    def click_persian_cat(self):
        self.get_persian_cat().click()

    def click_persian_femail_cat(self):
        self.get_persian_female_cat().click()

    def click_add_to_cart_button(self):
        self.get_add_to_cart_button().click()

    # Methods
    def choose_persian_female_cat(self):
        self.click_persian_cat()
        self.click_persian_femail_cat()
        self.click_add_to_cart_button()
        print("Selected pet is added to cart.")