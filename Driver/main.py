from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Import functions from login.py and forgotpassword.py
from login import login, logout
from forgotpassword import reset_password  # Ensure this exists and is implemented in forgotpassword.py

def main():
    # Set up the WebDriver (ensure you have the appropriate driver installed)
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    try:
        # Scenario 1: Valid login
        print("\nTesting: Valid login")
        login(driver, "coreudaymajhi@gmail.com", "Core@#$123")
        logout(driver)  # Log out after successful login

        # Scenario 2: Invalid username
        print("\nTesting: Invalid username")
        login(driver, "invalidemail@example.com", "Core@#$123")

        # Scenario 3: Invalid password
        print("\nTesting: Invalid password")
        login(driver, "coreudaymajhi@gmail.com", "wrongpassword")

        # Scenario 4: Empty email and password fields
        print("\nTesting: Empty email and password")
        login(driver, "", "")

        # Scenario 5: Reset password (valid email)
        print("\nTesting: Reset password for valid email")
        reset_password(driver, "coreudaymajhi@gmail.com")

        # Scenario 6: Reset password (invalid email)
        print("\nTesting: Reset password for invalid email")
        reset_password(driver, "invalidemail@example.com")

        # Optional: Wait for the response or confirmation message
        time.sleep(5)  # Adjust this delay if needed (consider using WebDriverWait for better handling)

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        # Close the browser after the actions are done
        print("Closing the browser...")
        driver.quit()

# Run the main function
if __name__ == "__main__":
    main()
