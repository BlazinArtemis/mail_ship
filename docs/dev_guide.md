# MailShip: Developer Documentation

## Table of Contents

1. [Overview](#overview)
2. [Architecture](#architecture)
3. [Core Components](#core-components)
   - [Authentication (auth.py)](#authentication-authpy)
   - [Email Generation (email_generator.py)](#email-generation-email_generatorpy)
   - [Email Listener (email_listener.py)](#email-listener-email_listenerpy)
   - [Email Parser (email_parser.py)](#email-parser-email_parserpy)
   - [Main Operations (operations.py)](#main-operations-operationspy)
4. [Authentication Flow](#authentication-flow)
5. [Email Generation Process](#email-generation-process)
6. [Email Listening Mechanism](#email-listening-mechanism)
7. [Email Parsing and Content Extraction](#email-parsing-and-content-extraction)
8. [Integration with Selenium](#integration-with-selenium)
9. [CI/CD Implementation](#cicd-implementation)
10. [Error Handling and Logging](#error-handling-and-logging)
11. [Performance Considerations](#performance-considerations)
12. [Security Measures](#security-measures)
13. [Future Enhancements](#future-enhancements)

## Overview

The MailShip library is designed to provide a robust and flexible solution for automating Gmail-related tasks, particularly in testing and automation scenarios. It leverages the Gmail API, implements OAuth 2.0 for secure authentication, and offers functionalities like email generation, listening, parsing, and content extraction.

## Architecture

The library follows a modular architecture, with each component responsible for a specific set of functionalities:

1. Authentication Module (auth.py)
2. Email Generation Module (email_generator.py)
3. Email Listener Module (email_listener.py)
4. Email Parser Module (email_parser.py)
5. Main Operations Module (operations.py)

This modular approach allows for easier maintenance, testing, and future enhancements.

## Core Components

### Authentication (auth.py)

The authentication module handles OAuth 2.0 authentication with the Gmail API. Key functionalities include:

- Loading and managing client configurations
- Implementing the OAuth 2.0 flow
- Securely storing and refreshing access tokens
- Managing environment variables for credential storage

#### Key Functions:

- `load_client_config()`: Loads the OAuth client configuration from a JSON file.
- `set_persistent_env_var()`: Sets or updates environment variables across different operating systems.
- `get_encryption_key()`: Generates an encryption key for secure token storage.
- `encrypt_value()` and `decrypt_value()`: Encrypt and decrypt sensitive data.
- `check_and_refresh_credentials()`: Manages the OAuth flow, including token refresh.

#### Thought Process:

The authentication module is designed with security and cross-platform compatibility in mind. It uses environment variables for persistent storage of encrypted credentials, allowing for secure usage in various environments, including CI/CD pipelines.

### Email Generation (email_generator.py)

This module is responsible for creating unique email addresses based on the user's Gmail account.

#### Key Functions:

- `generate_unique_email()`: Creates a unique email address using timestamp and random string.
- `store_generated_email()`: Stores generated emails for future reference.
- `is_valid_generated_email()`: Validates the generated email format.

#### Thought Process:

The email generation process ensures uniqueness by combining the user's base email with a timestamp and random string. This approach allows for creating multiple unique emails for a single Gmail account, which is crucial for testing scenarios.

### Email Listener (email_listener.py)

The email listener module handles real-time monitoring of incoming emails using the Gmail API.

#### Key Functions:

- `start_listening()`: Initiates the email monitoring process in a separate thread.
- `_listen()`: Core function that polls the Gmail API for new messages.
- `process_new_email()`: Processes newly received emails, extracting relevant information.

#### Thought Process:

The listener uses a polling mechanism with rate limiting to respect Gmail API quotas. It implements a threaded approach to allow for non-blocking operation in the main application flow.

### Email Parser (email_parser.py)

This module is responsible for extracting and processing information from emails.

#### Key Functions:

- `extract_token()`: Extracts numeric tokens from email content.
- `extract_link()`: Extracts links from email content, with optional domain filtering.
- `search_by_regex()`: Performs custom regex searches on email content.

#### Thought Process:

The parser is designed to be flexible, allowing for various types of content extraction. It handles both HTML and plain text emails, using BeautifulSoup for HTML parsing when necessary.

### Main Operations (operations.py)

The operations module serves as the main interface for the library, coordinating functionalities from other modules.

#### Key Class: GmailAutomator

- Initializes with authentication credentials
- Provides high-level methods for email operations
- Manages logging and error handling

#### Key Methods:

- `generate_email()`: Generates a unique email address.
- `wait_for_email()`: Waits for an email to arrive at a specified address.
- `extract_token()`, `extract_link()`, `search_by_regex()`: Wrapper methods for email parsing functions.

#### Thought Process:

The GmailAutomator class is designed as a facade, providing a simple interface for complex operations. It handles the coordination between different modules, making it easier for users to perform email automation tasks.

## Authentication Flow

1. The user runs `setup_auth.py` to initialize the authentication process.
2. The script prompts for Google Cloud project credentials (client ID and secret).
3. It initiates the OAuth flow, directing the user to authorize the application.
4. Upon authorization, the script securely stores the refresh token and other necessary information as environment variables.
5. Subsequent runs use the stored refresh token to obtain new access tokens as needed.

## Email Generation Process

1. The base email is split into local part and domain.
2. A unique identifier is created using a timestamp and random string.
3. The new email is formed by inserting the identifier between the local part and the '+' symbol.
4. The generated email is validated and stored for future reference.

## Email Listening Mechanism

1. The listener runs in a separate thread to avoid blocking the main application.
2. It uses the Gmail API's history and messages endpoints to efficiently check for new emails.
3. When a new email is detected, it's processed and added to a queue.
4. The main application can then retrieve new emails from this queue.

## Email Parsing and Content Extraction

1. For token extraction, the parser uses regex patterns to find numeric sequences.
2. Link extraction involves parsing HTML content (if available) or using regex for plain text.
3. The parser can handle both MIME and simple text messages.
4. Custom regex searches allow for flexible content extraction based on user needs.

## Integration with Selenium

The library is designed to work seamlessly with Selenium for end-to-end testing scenarios. The integration process typically involves:

1. Setting up a Selenium WebDriver (e.g., Chrome or Firefox).
2. Using MailShip to generate a unique email address.
3. Inputting this email into a web form using Selenium.
4. Waiting for an email response using MailShip's `wait_for_email` method.
5. Extracting necessary information (like verification links or codes) from the received email.
6. Using this information to continue the Selenium-driven test flow.

## CI/CD Implementation

The library supports CI/CD pipelines, particularly with GitHub Actions. Key considerations in the CI/CD setup include:

1. Using environment secrets to store sensitive information (OAuth credentials, etc.).
2. Setting up a headless browser environment for Selenium tests.
3. Implementing the email listening and parsing process in a non-interactive manner.
4. Ensuring proper error handling and logging for CI/CD debugging.

## Error Handling and Logging

- The library uses Python's built-in `logging` module for consistent log output.
- Each module has its own logger, allowing for granular control over log levels.
- Custom exceptions (e.g., `EmailParserError`, `EmailListenerError`) are used for specific error scenarios.
- The `GmailAutomator` class provides a `verbose` option to control the level of logging detail.

## Performance Considerations

1. **Rate Limiting**: The email listener implements rate limiting to respect Gmail API quotas.
2. **Efficient Polling**: The listener uses the Gmail API's history endpoint to efficiently check for new messages.
3. **Threaded Operations**: Email listening runs in a separate thread to maintain application responsiveness.
4. **Caching**: Generated emails are cached to avoid unnecessary regeneration.

## Security Measures

1. **OAuth 2.0**: Utilizes secure OAuth 2.0 flow for authentication.
2. **Encryption**: Sensitive data (like refresh tokens) is encrypted before storage.
3. **Environment Variables**: Credentials are stored as environment variables, not in files.
4. **Minimal Scope**: The library requests only the necessary Gmail API scopes.

## Future Enhancements

Potential areas for future development include:

1. Support for sending emails (currently focused on reading and parsing).
2. Enhanced email filtering capabilities.
3. Integration with other email providers beyond Gmail.
4. Improved error recovery and retry mechanisms.
5. Extended Selenium integration helpers for common testing scenarios.

