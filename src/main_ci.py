
from mailship.operations import GmailAutomator
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
# from webdriver_manager.chrome import ChromeDriverManager
import chromedriver_autoinstaller
from pyvirtualdisplay import Display

import json
import time
import re
import requests


test2_url = "http://mybp.d4devs.com/"
def colorize(text, color_code):
    return f"{color_code}{text}\033[0m"

def login_token(test_url,):

    automator = GmailAutomator(verbose=False)
    email_unique = automator.generate_email()
    print(f"Generated email: {email_unique}")
    # Set up the Chrome driver service with headless mode
    
    

    display = Display(visible=False, size=(1920, 1080))
    display.start()


    chromedriver_autoinstaller.install()  # Check if the current version of chromedriver exists
                                        # and if it doesn't exist, download it automatically,
                                        # then add chromedriver to path

    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run Chrome in headless mode
    chrome_options.add_argument("--no-sandbox")  # Needed in CI environments
    chrome_options.add_argument("--disable-dev-shm-usage")  # Prevent crashes
    chrome_options.add_argument("--disable-gpu")  # Disable GPU for headless
    chrome_options.add_argument("--window-size=1920,1080")  # Set screen size
    chrome_options.add_argument("--remote-debugging-port=9222")  # Debugging
    chrome_options.binary_location = "/usr/bin/chromium-browser"  # Ensure correct Chrome binary location



        
    driver = webdriver.Chrome(options = chrome_options)
    # Navigate to the URL
    driver.get(test_url)

    # Wait for the page to load (you may need to adjust the wait time)
    max_wait_time = 1
     
    
    # Click I understand
    try:
        phone_field = WebDriverWait(driver, max_wait_time).until(EC.presence_of_element_located((By.ID, "phone")))
        phone_field.send_keys("08088430233")
        email_field = WebDriverWait(driver, max_wait_time).until(EC.presence_of_element_located((By.ID, "email")))
        email_field.send_keys(email_unique)
        continue_field = WebDriverWait(driver, max_wait_time).until(EC.presence_of_element_located((By.CSS_SELECTOR, "button.auth-form-btn.mt-4")))
        continue_field.click()
        email_field = WebDriverWait(driver, max_wait_time).until(EC.presence_of_element_located((By.CSS_SELECTOR, "span.font-medium.text-green7.text-sm.underline.mt-10.cursor-pointer")))
        email_field.click()
        print("Waiting for an email (timeout: 60 seconds)...")
        received_email = automator.wait_for_email(email_unique, timeout=120)

        if received_email:
            print("succesful")
            print(received_email)
            token  = automator.extract_token(received_email, token_length=4)
            print(token)

    # Proceed with the next step in Selenium after receiving the email
        else:
            print("No email received. Exiting or retrying.")
            return
    
    
    # Perform actions with the element (e.g., click

    except Exception as e:
        print(e)
        print(colorize("Test failed - Click I understand", "\033[91m"))

def login_link(test_url):

    automator = GmailAutomator(verbose=False)
    email_unique = automator.generate_email()
    print(f"Generated email: {email_unique}")
    # Set up the Chrome driver service with headless mode
    # Set up Chrome options for headless mode
    display = Display(visible=False, size=(1920, 1080))
    display.start()


    chromedriver_autoinstaller.install()  # Check if the current version of chromedriver exists
                                        # and if it doesn't exist, download it automatically,
                                        # then add chromedriver to path

    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run Chrome in headless mode
    chrome_options.add_argument("--no-sandbox")  # Needed in CI environments
    chrome_options.add_argument("--disable-dev-shm-usage")  # Prevent crashes
    chrome_options.add_argument("--disable-gpu")  # Disable GPU for headless
    chrome_options.add_argument("--window-size=1920,1080")  # Set screen size
    chrome_options.add_argument("--remote-debugging-port=9222")  # Debugging
    chrome_options.binary_location = "/usr/bin/chromium-browser"  # Ensure correct Chrome binary location


        
    driver = webdriver.Chrome(options = chrome_options)

    # Navigate to the URL
    driver.get(test_url)

    # Wait for the page to load (you may need to adjust the wait time)
    driver.implicitly_wait(60)  
    max_wait_time = 1
     
    
    # Click I understand
    try:
        email_field = WebDriverWait(driver, max_wait_time).until(EC.presence_of_element_located((By.ID, "email")))
        email_field.send_keys(email_unique)
        continue_field = WebDriverWait(driver, max_wait_time).until(EC.presence_of_element_located((By.CSS_SELECTOR, "button.btn.btn-primary")))
        continue_field.click()
        print("Waiting for an email (timeout: 60 seconds)...")
        received_email = automator.wait_for_email(email_unique, timeout=120)

        if received_email:
            print("succesful")
            # print(received_email)
            token  = automator.extract_link(received_email)
            print(token)

    # Proceed with the next step in Selenium after receiving the email
        else:
            print("No email received. Exiting or retrying.")
            return
    # Perform actions with the element (e.g., click)
    except Exception as e:
        print(e)
        print(colorize("Test failed - Click I understand", "\033[91m"))

    driver.get(test_url)
    try:
        email_field = WebDriverWait(driver, max_wait_time).until(EC.presence_of_element_located((By.ID, "email")))
        email_field.send_keys(email_unique)
        continue_field = WebDriverWait(driver, max_wait_time).until(EC.presence_of_element_located((By.CSS_SELECTOR, "button.btn.btn-primary")))
        continue_field.click()
        print("Waiting for an email (timeout: 60 seconds)...")
        received_email = automator.wait_for_email(email_unique, subject='Your Magic Link to Simple BP Tracker', timeout=120)

        if received_email:
            print("succesful")
            # print(received_email)
            token  = automator.extract_link(received_email, domain='mybp.d4devs.com')
            print(token)

    # Proceed with the next step in Selenium after receiving the email
        else:
            print("No email received. Exiting or retrying.")
            return
    
    
    # Perform actions with the element (e.g., click)
    except Exception as e:
        print(e)
        print(colorize("Test failed - Click I understand", "\033[91m"))
    
def login_regex(test_url):

    automator = GmailAutomator(verbose=False)
    email_unique = automator.generate_email()
    print(f"Generated email: {email_unique}")
    # Set up the Chrome driver service with headless mode
    # Set up Chrome options for headless mode
    display = Display(visible=False, size=(1920, 1080))
    display.start()


    chromedriver_autoinstaller.install()  # Check if the current version of chromedriver exists
                                        # and if it doesn't exist, download it automatically,
                                        # then add chromedriver to path

    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run Chrome in headless mode
    chrome_options.add_argument("--no-sandbox")  # Needed in CI environments
    chrome_options.add_argument("--disable-dev-shm-usage")  # Prevent crashes
    chrome_options.add_argument("--disable-gpu")  # Disable GPU for headless
    chrome_options.add_argument("--window-size=1920,1080")  # Set screen size
    chrome_options.add_argument("--remote-debugging-port=9222")  # Debugging
    chrome_options.binary_location = "/usr/bin/chromium-browser"  # Ensure correct Chrome binary location

        
    driver = webdriver.Chrome(options = chrome_options)

    # Navigate to the URL
    driver.get(test_url)

    # Wait for the page to load (you may need to adjust the wait time)
    driver.implicitly_wait(60)  
    max_wait_time = 1
     
    
    # Click I understand
    try:
        email_field = WebDriverWait(driver, max_wait_time).until(EC.presence_of_element_located((By.ID, "email")))
        email_field.send_keys(email_unique)
        continue_field = WebDriverWait(driver, max_wait_time).until(EC.presence_of_element_located((By.CSS_SELECTOR, "button.btn.btn-primary")))
        continue_field.click()
        print("Waiting for an email (timeout: 60 seconds)...")
        received_email = automator.wait_for_email(email_unique, timeout=120)
        if received_email:
            print("succesful")
            # print(received_email)
            token  = automator.search_by_regex(received_email, pattern="([A-Z])\w+")
            print(token)

    # Proceed with the next step in Selenium after receiving the email
        else:
            print("No email received. Exiting or retrying.")
            return
    # Perform actions with the element (e.g., click)
    except Exception as e:
        print(e)
        print(colorize("Test failed - Click I understand", "\033[91m"))

   

def run_example():
    """
    Run a simple example of the GmailAutomator functionality.
    This can be used as a quick test or demonstration.
    """
    automator = GmailAutomator(verbose=True)
    
    try:
        email = automator.generate_email()
        print(f"Generated email: {email}")
        
        print("Waiting for an email (timeout: 60 seconds)...")
        received_email = automator.wait_for_email(email, timeout=120)
        
        if received_email:
            print(f"Received email: {received_email['subject']}")
        else:
            print("No email received within the timeout period.")
    
    finally:
        automator.cleanup()

if __name__ == "__main__":
    login_link(test2_url)
    # login_token(test_url)
    login_regex(test2_url)