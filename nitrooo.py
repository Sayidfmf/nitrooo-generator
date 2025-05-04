import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

def check_roblox_redeem_code(username, password, redeem_code):
    # Set up Selenium WebDriver (make sure ChromeDriver is installed and in PATH)
    driver = webdriver.Chrome()  # Or use other drivers like Firefox
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
        
        # Wait for login to complete (check for a logged-in element, e.g., user avatar or redeem form)
        try:
            # After login, the redeem form might appear; wait for it
            redeem_input = wait.until(EC.presence_of_element_located((By.ID, "redeem-code-input")))  # This ID might not be exact; inspect the page after login
            redeem_button = driver.find_element(By.ID, "redeem-button")  # Adjust based on actual HTML
            
            # Enter the redeem code and submit
            redeem_input.send_keys(redeem_code)
            redeem_button.click()
            
            # Wait for result (e.g., success or error message)
            time.sleep(2)  # Short delay to allow page to update
            result_element = driver.find_element(By.CLASS_NAME, "redeem-result")  # Hypothetical class; check actual HTML for success/error indicators
            
            # Parse result (this is simplistic; you'd need to inspect the page for actual elements)
            if "success" in result_element.text.lower():  # Adjust based on real text or elements
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
        driver.quit()  # Close the browser

# Example usage (replace with your credentials and code)
if __name__ == "__main__":
    username = "your_username"  # Replace with actual username
    password = "your_password"  # Replace with actual password
    redeem_code = "example_code"  # Replace with the code to check
    check_roblox_redeem_code(username, password, redeem_code)
