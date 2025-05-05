import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException, NoSuchElementException

def check_roblox_redeem_code(username, password, redeem_code):
    chrome_options = Options()
    chrome_options.add_argument("--headless=new")  # Use new headless mode for stability
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--disable-software-rasterizer")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--remote-debugging-port=9222")
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--user-data-dir=/tmp/chrome-profile")  # Unique profile dir

    driver = webdriver.Chrome(options=chrome_options)

    try:
        driver.get("https://www.roblox.com/redeem")

        wait = WebDriverWait(driver, 10)
        username_field = wait.until(EC.presence_of_element_located((By.ID, "login-username")))
        password_field = driver.find_element(By.ID, "login-password")
        login_button = driver.find_element(By.ID, "login-button")

        username_field.send_keys(username)
        password_field.send_keys(password)
        login_button.click()

        try:
            redeem_input = wait.until(EC.presence_of_element_located((By.ID, "redeem-code-input")))  # Adjust if needed
            redeem_button = driver.find_element(By.ID, "redeem-button")  # Adjust if needed

            redeem_input.send_keys(redeem_code)
            redeem_button.click()

            time.sleep(2)  # Wait for result

            result_element = driver.find_element(By.CLASS_NAME, "redeem-result")  # Adjust if needed
            if "success" in result_element.text.lower():
                print(f"✅ Code '{redeem_code}' is valid!")
            else:
                print(f"❌ Code '{redeem_code}' is invalid.")

        except TimeoutException:
            print("❌ Redemption form not found or login failed. Check page structure or login status.")
        except NoSuchElementException:
            print("❌ Redemption elements not found. Page structure may have changed.")

    except Exception as e:
        print(f"Error: {str(e)}")

    finally:
        driver.quit()

if __name__ == "__main__":
    username = "your_username"  # Replace with your Roblox username
    password = "your_password"  # Replace with your Roblox password
    redeem_code = "example_code"  # Replace with the code you want to check
    check_roblox_redeem_code(username, password, redeem_code)
