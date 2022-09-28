from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base


class MainPage(Base):

    url = "https://petstore.octoperf.com/actions/Catalog.action"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    sign_in_link = "//div[@id='MenuContent']/a[2]"
    reference_text = "//div[@id='Catalog']/form/p[1]"
    cats_category = "//div[@id='SidebarContent']/a[3]"

    # Getters
    def get_sign_in_link(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.sign_in_link)))

    def get_reference_text(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.reference_text)))

    def get_cats_category(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cats_category)))

    # Actions
    def click_sign_in_link(self):
        self.get_sign_in_link().click()

    def click_cats_category(self):
        self.get_cats_category().click()

    # Methods
    def open_sign_in_page(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url()
        self.click_sign_in_link()
        self.get_current_url()
        self.assert_text(self.get_reference_text(), "Please enter your username and password.")