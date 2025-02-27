Here’s a more concise and focused `README.md` tailored specifically for the PyPI package, including a link to the GitHub repository for detailed documentation.

---

# MailShip

[![PyPI version](https://badge.fury.io/py/mail-ship.svg)](https://badge.fury.io/py/mail-ship)  
MailShip is a Python library designed to simplify Gmail automation for developers and testers. It offers tools for email generation, email content extraction, and seamless integration with CI/CD pipelines and testing frameworks.

## Features

- Generate unique email addresses for testing.
- Wait for and retrieve emails in real time.
- Extract tokens and links from email content.
- Perform regex-based searches on email content.
- Automatically refresh Gmail API tokens via cron jobs or pipelines.
- CI/CD ready with GitHub Actions integration.

## Installation

Install the library using pip:

```bash
pip install mailship
```

## Configuration

Before using MailShip, you need to set up a Google Cloud project and configure OAuth credentials. Follow the steps below:

### Step 1: Create a Google Cloud Project

1. Visit the [Google Cloud Console](https://console.cloud.google.com/).
2. Click on the project selector at the top and choose "New Project."
3. Enter a name for your project (e.g., "MailShip") and click "Create."
4. Select your new project from the project dropdown once it's created.

### Step 2: Enable the Gmail API

1. Go to "APIs & Services" > "Library" in the left sidebar.
2. Search for "Gmail API" and select it.
3. Click "Enable" to activate the API for your project.

### Step 3: Configure the OAuth Consent Screen

1. Navigate to "APIs & Services" > "OAuth consent screen."
2. Select "External" (or "Internal" for Google Workspace accounts).
3. Fill in the following fields:
   - **App Name**: MailShip
   - **User Support Email**: Your email address
   - **Developer Contact Information**: Your email address
4. Add these required scopes on the "Scopes" page:
   - https://www.googleapis.com/auth/gmail.readonly
   - https://www.googleapis.com/auth/userinfo.email
5. Save the settings and add your Gmail account under "Test Users."

### Step 4: Create an OAuth 2.0 Client ID

1. Go to "APIs & Services" > "Credentials."
2. Click "Create Credentials" > "OAuth client ID."
3. Choose "Desktop app" as the application type.
4. Name the client (e.g., "MailShip Desktop Client") and click "Create."
5. Download the `client_secrets.json` file and place it in your project directory.


## Getting Started

After getting your credentials, you can initialize the setup process:

Run one of the following commands to set up your Gmail API credentials:

### Option 1: Setup Gmail Authentication

Run the following command to set up your Gmail API credentials without automatic token refreshing setup. 

Note: TOkens would expire if app is not used for long periods of time

```bash
mail-ship-setup
```

This will guide you through the setup process, including storing credentials and setting environment variables.

### Option 2: Set Up Automatic Token Refreshing (Linux)

- To set up a **cron job** (Linux/macOS) for automatic token refreshing, run:
  ```bash
  mail-ship-setup --setup-cron
  ```

### Option 3: Set Up Automatic Token Refreshing (Windows)
 
- To set up a **scheduled task** (Windows), run:
  ```bash
  mail-ship-setup --setup-task
  ```

For more detailed setup instructions, visit the GitHub repository.

---

## Basic Usage

Here’s a quick example of how to use MailShip:

```python
from mailship import GmailAutomator

automator = GmailAutomator(verbose=True)

# Generate a unique email for testing
email = automator.generate_email()
print(f"Generated email: {email}")

# Wait for an email
received_email = automator.wait_for_email(email, timeout=120)

if received_email:
    print(f"Received email: {received_email['subject']}")
    # Extract a token from the email
    token = automator.extract_token(received_email)
    print(f"Extracted token: {token}")
else:
    print("No email received within the timeout period.")
```

---

## CI/CD Integration

MailShip is designed to work seamlessly in CI/CD pipelines. Add the following step in your GitHub Actions workflow to refresh Gmail API tokens:

```yaml
- name: Refresh Tokens
  env:
    GMAIL_CLIENT_ID: ${{ secrets.GMAIL_CLIENT_ID }}
    GMAIL_CLIENT_SECRET: ${{ secrets.GMAIL_CLIENT_SECRET }}
    GMAIL_AUTH_REFRESH_TOKEN: ${{ secrets.GMAIL_AUTH_REFRESH_TOKEN }}
    GMAIL_AUTH_SALT: ${{ secrets.GMAIL_AUTH_SALT }}
  run: python -m mailship.setup_auth --refresh-tokens
```

---

## Documentation

For detailed documentation, advanced features, and contributing guidelines, visit the [GitHub repository](https://github.com/BlazinArtemis/mail_ship/).

---

## License

This project is licensed under a Custom Repository License. See the [GitHub repository](https://github.com/BlazinArtemis/mail_ship/) for details.

---

## Contact

For questions or support, reach out on:
- **Twitter**: [@OluwaseyiAjadi4](https://twitter.com/OluwaseyiAjadi4)
- **LinkedIn**: [Oluwaseyi Ajadi](https://www.linkedin.com/in/oluwaseyi-ajadi/)

---

This `README.md` is concise, focused on installation and usage, and directs users to the GitHub repository for in-depth information. Let me know if you’d like further refinements!