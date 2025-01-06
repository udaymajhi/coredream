from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def click_main_button(url):
    # Setup the WebDriver (using Chrome in this example)
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    try:
        # Open the webpage
        driver.get(url)

        # Find the main button (use an appropriate selector such as class, id, etc.)
        main_button = driver.find_element(By.CSS_SELECTOR,
                                          "button.main-button")  # Change the selector to match your button

        # Optionally, you can use ActionChains if you need to hover or perform other actions before clicking
        actions = ActionChains(driver)
        actions.move_to_element(main_button).click().perform()  # Click the button

        print("Button clicked successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Close the WebDriver
        driver.quit()


# Example usage:
click_main_button('https://www.example.com')  # Replace with your desired URL
