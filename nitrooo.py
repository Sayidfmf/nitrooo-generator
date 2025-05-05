import subprocess
import sys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException, NoSuchElementException

def install_dependencies():
    # Install selenium via pip
    subprocess.check_call([sys.executable, "-m", "pip", "install", "selenium"])
    # Install chromium-browser and chromedriver (Debian/Ubuntu)
    subprocess.check_call(["sudo", "apt-get", "update"])
    subprocess.check_call(["sudo", "apt-get", "install", "-y", "chromium-browser", "chromium-chromedriver"])

def setup_driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--disable-software-rasterizer")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--remote-debugging-port=9222")
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--user-data-dir=/tmp/chrome-profile")
    # Use chromium binary if needed (uncomment if default Chrome not found)
    # chrome_options.binary_location = "/usr/bin/chromium-browser"
    driver = webdriver.Chrome(options=chrome_options)
    return driver

def handle_cookie_banner(driver):
    time.sleep(1)  # Wait for banner to load
    try:
        cookie_accept_button = driver.find_element(By.CSS_SELECTOR, "button#accept-cookie-button, button.cookie-accept, button.cookie-banner-accept")
        cookie_accept_button.click()
        print("Cookie banner accepted.")
    except Exception:
        driver.execute_script("""
            const banner = document.querySelector('div.cookie-banner-bg');
            if (banner) { banner.style.display = 'none'; }
        """)
        print("Cookie banner overlay removed.")

def login_with_credentials(driver, username, password):
    wait = WebDriverWait(driver, 10)
          username_field = wait.until(EC.presence_of_element_located((By.ID, "login-username")))    password_field = driver.find_element(By.ID, "<input id="login-password" name="password" type="password" class="form-control input-field" placeholder="Password" value="">")
    login_button = driver.find_element(By.ID, "<button type="button" id="login-button" class="btn-full-width login-button btn-secondary-md">Log In</button>")

    username_field.send_keys(username)
    password_field.send_keys(password)
    login_button.click()

def inject_cookies(driver, cookies):
    driver.delete_all_cookies()
    for cookie in cookies:
        driver.add_cookie(cookie)
    driver.refresh()

def check_roblox_redeem_code(username=None, password=None, redeem_code=None, cookies=None):
    driver = setup_driver()
    try:
        driver.get("https://www.roblox.com/redeem")
        handle_cookie_banner(driver)

        if cookies:
            inject_cookies(driver, cookies)
            print("Cookies injected, session restored.")
        elif username and password:
            login_with_credentials(driver, username, password)
        else:
            print("No login method provided. Provide username/password or cookies.")
            return

        wait = WebDriverWait(driver, 10)
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
    # Uncomment the next line to install dependencies on first run
    # install_dependencies()

    # Example usage:
    # Option 1: Login with username/password
    username = "sayidzaltsz2"
    password = "Bozosayid1"
    redeem_code = "example_code"

    # Option 2: Use cookies for faster login (example cookie format)
    # cookies = [
    #     {"name": ".ROBLOSECURITY", "value": "your_roblosecurity_cookie_value", "domain": ".roblox.com", "path": "/"},
    #     # Add other cookies if needed
    # ]

    # Use either login or cookies:
    check_roblox_redeem_code(username=username, password=password, redeem_code=redeem_code)
    # Or with cookies:
    # check_roblox_redeem_code(cookies=cookies, redeem_code=redeem_code)
