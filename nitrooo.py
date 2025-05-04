import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options  # Added for Chrome options
from selenium.common.exceptions import TimeoutException, NoSuchElementException

def check_roblox_redeem_code(username, password, redeem_code):
    # Set up Chrome options to avoid user data directory conflicts
    chrome_options = Options()
    chrome_options.add_argument("--user-data-dir=/tmp/chrome-profile")  # Specify a unique directory
    chrome_options.add_argument("--no-sandbox")  # Required in some restricted environments like codespaces
    chrome_options.add_argument("--disable-extensions")  # Disable extensions to avoid issues
    chrome_options.add_argument("--headless")  # Optional: Run in headless mode to avoid opening a browser window
    
    # Initialize WebDriver with options
    driver = webdriver.Chrome(options=chrome_options)
    
    try:
        # Open Roblox redeem page
        driver.get("https://www.roblox.com/redeem")
        
        # Wait for login elements and log in
        wait = WebDriverWait(driver, 10)
        username_field = wait.until(EC.presence_of_element_located((By.ID, "login-username")))
        password_field = driver.find_element(By.ID, "login-password")
        login_button = driver.find_element(By.ID, "login-button")
        
        username_field.send_keys(username)
        password_field.send_keys(password)
        login_button.click()
        
        # Wait for login to complete and redemption form to appear
        try:
            redeem_input = wait.until(EC.presence_of_element_located((By.ID, "redeem-code-input")))  # Adjust ID if needed
            redeem_button = driver.find_element(By.ID, "redeem-button")  # Adjust based on actual HTML
            
            # Enter the redeem code and submit
            redeem_input.send_keys(redeem_code)
            redeem_button.click()
            
            # Wait for result and check for success or error
            time.sleep(2)  # Short delay for page to update
            result_element = driver.find_element(By.CLASS_NAME, "redeem-result")  # Hypothetical class; inspect page for accuracy
            if "success" in result_element.text.lower():  # Check for success text
                print(f"✅ Code '{redeem_code}' is valid!")
            else:
                print(f"❌ Code '{redeem_code}' is invalid.")
        
        except TimeoutException:
            print("❌ Redemption form not found or login failed. Ensure you're on the correct page.")
        
        except NoSuchElementException:
            print("❌ Could not find redemption elements. Page structure might have changed.")
    
    except Exception as e:
        print(f"Error: {str(e)}")
    
    finally:
        driver.quit()  # Ensure the driver is closed

# Example usage
if __name__ == "__main__":
    username = "your_username"  # Replace with actual username
    password = "your_password"  # Replace with actual password
    redeem_code = "example_code"  # Replace with the code to check
    check_roblox_redeem_code(username, password, redeem_code)
