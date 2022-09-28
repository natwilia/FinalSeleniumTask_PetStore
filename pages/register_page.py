from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from selenium.webdriver.support.ui import Select


class RegisterPage(Base):

    register_url = "https://petstore.octoperf.com/actions/Account.action?newAccountForm="

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    username = "//input[@name='username']"
    register_password = "//input[@name='password']"
    confirm_password = "//input[@name='repeatedPassword']"
    first_name = "//input[@name='account.firstName']"
    last_name = "//input[@name='account.lastName']"
    email = "//input[@name='account.email']"
    phone = "//input[@name='account.phone']"
    address_line1 = "//input[@name='account.address1']"
    city = "//input[@name='account.city']"
    state = "//input[@name='account.state']"
    zip = "//input[@name='account.zip']"
    country = "//input[@name='account.country']"
    favorite_category = "//select[@name='account.favouriteCategoryId']"
    save_account_button = "//input[@name='newAccount']"

    # Getters
    def get_username(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.username)))

    def get_register_password(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.register_password)))

    def get_confirm_password(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.confirm_password)))

    def get_first_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.first_name)))

    def get_last_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.last_name)))

    def get_email(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.email)))

    def get_phone(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.phone)))

    def get_address_first_line(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.address_line1)))

    def get_city(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.city)))

    def get_state(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.state)))

    def get_zip(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.zip)))

    def get_country(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.country)))

    def get_favorite_category(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.favorite_category)))

    def get_save_account_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.save_account_button)))

    # Actions
    def input_username(self, username):
        self.get_username().send_keys(username)

    def input_register_password(self, new_password):
        self.get_register_password().send_keys(new_password)

    def input_confirm_password(self, repeat_password):
        self.get_confirm_password().send_keys(repeat_password)

    def input_first_name(self, first_name):
        self.get_first_name().send_keys(first_name)

    def input_last_name(self, last_name):
        self.get_last_name().send_keys(last_name)

    def input_email(self, email_address):
        self.get_email().send_keys(email_address)

    def input_phone(self, phone_number):
        self.get_phone().send_keys(phone_number)

    def input_address_first_line(self, address):
        self.get_address_first_line().send_keys(address)

    def input_city(self, city):
        self.get_city().send_keys(city)

    def input_state(self, state):
        self.get_state().send_keys(state)

    def input_zip(self, zip_code):
        self.get_zip().send_keys(zip_code)

    def input_country(self, country):
        self.get_country().send_keys(country)

    def click_favorite_category(self):
        self.get_favorite_category().click()

    def click_save_account_button(self):
        self.get_save_account_button().click()

    # Methods
    def select_cats_category_from_dropdown(self):
        select = Select(WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.favorite_category))))
        self.click_favorite_category()
        select.select_by_value("CATS")

    credentials = {"username": "", "password": ""}

    def register_new_account(self):
        self.driver.get(self.register_url)
        self.driver.maximize_window()
        # Enter User Information
        generated_username = "test" + self.define_now_datetime()
        self.input_username(generated_username)
        generated_password = "selenium" + self.define_now_datetime()
        self.input_register_password(generated_password)
        self.input_confirm_password(generated_password)
        # Enter Account Information
        self.input_first_name("Test")
        self.input_last_name("User")
        generated_email = generated_username + "@test.com"
        self.input_email(generated_email)
        self.input_phone("8112223333")
        self.input_address_first_line("9 Oak Street")
        self.input_city("New York")
        self.input_state("NY")
        self.input_zip("10001")
        self.input_country("USA")
        # Enter Profile Information
        self.select_cats_category_from_dropdown()
        self.click_save_account_button()
        self.credentials["username"] = generated_username
        self.credentials["password"] = generated_password

