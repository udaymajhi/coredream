# forgotpassword.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def reset_password(driver, email):
    """
    Function to reset password.
    :param driver: WebDriver instance.
    :param email: Email address for resetting the password.
    """
    driver.get("https://account.mydriver.au/login")
    driver.maximize_window()

    # Wait for and click the "Forgot Password" link
    forgot_password_link = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//a[normalize-space()='Forgot Password']"))
    )
    forgot_password_link.click()

    # Wait for the email input field on the Forgot Password page
    email_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@id='email']"))
    )

    # Enter the email for password reset
    email_input.send_keys(email)

    # Find and click the Reset Password button
    submit_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Reset Password']"))
    )
    submit_button.click()

    print("Password reset process started!")
