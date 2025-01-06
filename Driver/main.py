# main.py
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Import functions from login.py and forgotpassword.py
from login import login, logout
from forgotpassword import reset_password

def main():
    # Set up the WebDriver (ensure you have the appropriate driver installed)
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    try:
        # Step 1: Login
        login(driver, "coreudaymajhi@gmail.com", "Core@#$123")

        # Step 2: Logout
        logout(driver)

        # Step 3: Reset Password
        reset_password(driver, "coreudaymajhi@gmail.com")

        # Optional: Wait for the response or confirmation message
        time.sleep(5)  # Adjust this delay if needed

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        # Close the browser after the actions are done
        driver.quit()

# Run the main function
if __name__ == "__main__":
    main()


