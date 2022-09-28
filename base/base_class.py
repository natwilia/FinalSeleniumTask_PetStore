import datetime


class Base():

    def __init__(self, driver):
        self.driver = driver

    """Method to get current URL"""

    def get_current_url(self):
        get_url = self.driver.current_url
        print(f"Current URL is {get_url}")

    """Method to assert text"""

    def assert_text(self, text, expected_result):
        text_value = text.text
        assert text_value == expected_result
        print("Text is correct.")

    """Method to assert URL"""

    def assert_url(self, expected_result):
        get_url = self.driver.current_url
        assert get_url == expected_result
        print(f"URL is correct.")

    """Method to define current datetime value"""

    def define_now_datetime(self):
        now_datetime = datetime.datetime.utcnow().strftime("%m%d%Y%H%M%S")
        return now_datetime

    """Method to create a screenshot"""

    def create_screenshot(self):
        screenshot_name = "screenshot_" + self.define_now_datetime() + ".png"
        self.driver.save_screenshot(
            "C:\\Users\\nkurakina\\PycharmProjects\\FinalSeleniumTask_PetStore\\screenshots\\" + screenshot_name)
