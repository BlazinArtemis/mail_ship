from mailship.operations import GmailAutomator
from playwright.sync_api import sync_playwright
import time
import re

test2_url = "http://mybp.d4devs.com/"


def colorize(text, color_code):
    return f"{color_code}{text}\033[0m"


def login_token(playwright, test_url):
    automator = GmailAutomator(verbose=False)
    email_unique = automator.generate_email()
    print(f"Generated email: {email_unique}")

    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context(viewport={"width": 1200, "height": 800})
    page = context.new_page()

    try:
        page.goto(test_url)
        page.fill("#phone", "08088430233")
        page.fill("#email", email_unique)
        page.click("button.auth-form-btn.mt-4")
        print("Waiting for an email (timeout: 120 seconds)...")
        
        received_email = automator.wait_for_email(email_unique, timeout=120)
        if received_email:
            print("Successful!")
            print(received_email)
            token = automator.extract_token(received_email, token_length=4)
            print(token)
        else:
            print("No email received. Exiting or retrying.")
    except Exception as e:
        print(e)
        print(colorize("Test failed - Login Token", "\033[91m"))
    finally:
        browser.close()


def login_link(playwright, test_url):
    automator = GmailAutomator(verbose=False)
    email_unique = automator.generate_email()
    print(f"Generated email: {email_unique}")

    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context(viewport={"width": 1200, "height": 800})
    page = context.new_page()

    try:
        page.goto(test_url)
        page.fill("#email", email_unique)
        page.click("button.btn.btn-primary")
        print("Waiting for an email (timeout: 120 seconds)...")

        received_email = automator.wait_for_email(email_unique, timeout=120)
        if received_email:
            print("Successful!")
            token = automator.extract_link(received_email)
            print(token)
        else:
            print("No email received. Exiting or retrying.")
    except Exception as e:
        print(e)
        print(colorize("Test failed - Login Link", "\033[91m"))
    finally:
        browser.close()


def login_regex(playwright, test_url):
    automator = GmailAutomator(verbose=False)
    email_unique = automator.generate_email()
    print(f"Generated email: {email_unique}")

    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context(viewport={"width": 1200, "height": 800})
    page = context.new_page()

    try:
        page.goto(test_url)
        page.fill("#email", email_unique)
        page.click("button.btn.btn-primary")
        print("Waiting for an email (timeout: 120 seconds)...")

        received_email = automator.wait_for_email(email_unique, timeout=120)
        if received_email:
            print("Successful!")
            token = automator.search_by_regex(received_email, pattern="([A-Z])\w+")
            print(token)
        else:
            print("No email received. Exiting or retrying.")
    except Exception as e:
        print(e)
        print(colorize("Test failed - Login Regex", "\033[91m"))
    finally:
        browser.close()


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
    with sync_playwright() as playwright:
        login_link(playwright, test2_url)
        # login_token(playwright, test_url)
        login_regex(playwright, test2_url)
