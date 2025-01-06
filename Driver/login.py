# login.py
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def login(driver, email, password):
    """
    Function to log in to the account.
    :param driver: WebDriver instance.
    :param email: Email address.
    :param password: Password.
    """
    driver.get("https://account.mydriver.au/login")
    driver.maximize_window()

    # Wait until the email input field is present
    email_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@id='driver-login-email-input']"))
    )
    email_input.send_keys(email)

    # Use the TAB key to move to the password field
    email_input.send_keys(Keys.TAB)

    # Wait until the password input field is present
    password_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@id='driver-login-password-input']"))
    )
    password_input.send_keys(password)

    # Simulate pressing "Enter" to submit the form
    password_input.send_keys(Keys.ENTER)

    # Wait for the page to load after login (URL change)
    WebDriverWait(driver, 10).until(
        EC.url_changes("https://account.mydriver.au/login")
    )

    print("Login successful!")

def logout(driver):
    """
    Function to log out of the account.
    :param driver: WebDriver instance.
    """
    # Wait until the profile link (Uday Majhi) is clickable, then click it
    profile_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//a[normalize-space()="Uday Majhi"]'))
    )
    profile_link.click()

    print("Profile opened successfully!")

    # Wait for the Log Out link to be clickable, then click it
    logout_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//a[normalize-space()="Log Out"]'))
    )
    logout_button.click()

    print("Logged out successfully!")
