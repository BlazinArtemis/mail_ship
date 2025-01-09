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

## Getting Started

After installing the package, you can initialize the setup process:

### Step 1: Setup Gmail Authentication
Run the following command to set up your Gmail API credentials:

```bash
mail-ship-setup
```

This will guide you through the setup process, including storing credentials and setting environment variables.

### Step 2: Set Up Automatic Token Refreshing

- To set up a **cron job** (Linux/macOS) for automatic token refreshing, run:
  ```bash
  mail-ship-setup --setup-cron
  ```
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