from mailship import GmailAutomator

# Initialize the automator
automator = GmailAutomator()

# Generate a unique email address
unique_email = automator.generate_email()
print(f"Using email: {unique_email}")

# Use this email to sign up for the service (simulated)
print(f"Signing up to ExampleService with {unique_email}")

# Wait for the verification email
print("Waiting for verification email...")
email = automator.wait_for_email(
    recipient=unique_email,
    sender="noreply@exampleservice.com",
    subject="Verify your account",
    timeout=300  # 5 minutes
)

if email:
    # Try to extract a verification code
    code = automator.extract_token(email)
    if code:
        print(f"Extracted verification code: {code}")
        # Use the code to verify the account (simulated)
        print(f"Verifying account with code: {code}")
    else:
        # If no code found, try to extract a verification link
        link = automator.extract_link(email, domain="exampleservice.com")
        if link:
            print(f"Extracted verification link: {link}")
            # Use the link to verify the account (simulated)
            print(f"Verifying account by visiting: {link}")
        else:
            print("Could not find a verification code or link in the email.")
else:
    print("Did not receive a verification email within the timeout period.")

# Clean up
automator.cleanup()