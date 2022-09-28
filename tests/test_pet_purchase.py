import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from pages.cart_page import CartPage
from pages.main_page import MainPage
from pages.order_confirmation_page import OrderConfirmationPage
from pages.payment_page import PaymentPage
from pages.pet_details_page import PetDetailsPage
from pages.register_page import RegisterPage
from pages.sign_in_page import SignInPage


def test_cat_purchase():
    # Open browser and link
    options = Options()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    chrome_service = Service(r'C:\Users\nkurakina\PycharmProjects\resources\chromedriver.exe')
    driver = webdriver.Chrome(service=chrome_service, options=options)
    # Register new account
    register_page = RegisterPage(driver)
    register_page.register_new_account()
    # Sign in with registered account
    sign_in_page = SignInPage(driver)
    sign_in_page.sign_in_with_registered_user()
    # Select pet and add to cart
    main_page = MainPage(driver)
    main_page.click_cats_category()
    pet_details_page = PetDetailsPage(driver)
    pet_details_page.choose_persian_female_cat()
    # Update quantity anc check price in cart and proceed to checkout
    cart_page = CartPage(driver)
    cart_page.change_quantity()
    cart_page.click_proceed_to_checkout_button()
    # Enter payment details
    payment_page = PaymentPage(driver)
    payment_page.enter_payment_data()
    payment_page.click_continue_button()
    # Confirm order
    order_confirmation = OrderConfirmationPage(driver)
    order_confirmation.click_confirm_button()
    # Check that the order is placed successfully
    order_confirmation.check_order_success()
    time.sleep(5)