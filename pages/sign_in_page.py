from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from pages.main_page import MainPage
from pages.register_page import RegisterPage


class SignInPage(Base):

    sign_in_url = "https://petstore.octoperf.com/actions/Account.action?signonForm="

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    register_link = "//div[@id='Catalog']/a"
    reference_text = "//div[@id='MenuContent']/a[2]"
    username = "//input[@name='username']"
    password = "//input[@name='password']"
    login_button = "//input[@name='signon']"

    # Getters
    def get_register_link(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.register_link)))

    def get_reference_text(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.reference_text)))

    def get_username(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.username)))

    def get_password(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.password)))

    def get_login_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.login_button)))

    def get_reference_text(self):
        return WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, self.reference_text)))

    # Actions
    def click_register_link(self):
        self.get_register_link().click()

    def input_username(self, username):
        self.get_username().send_keys(username)

    def input_password(self, password):
        self.get_password().send_keys(password)

    def click_login_button(self):
        self.get_login_button().click()

    # Methods
    def sign_in_with_registered_user(self):
        main_page = MainPage(self.driver)
        main_page.open_sign_in_page()
        register_page = RegisterPage(self.driver)
        self.input_username(register_page.credentials["username"])
        password_field = self.driver.find_element(By.XPATH, self.password)
        password_field.send_keys(Keys.CONTROL + "a")
        password_field.send_keys(Keys.DELETE)
        self.input_password(register_page.credentials["password"])
        self.click_login_button()
        self.assert_text(self.get_reference_text(), "Sign Out")
