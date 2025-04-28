# Pwned Password Checker

This Python script allows users to check whether their password has been exposed in known data breaches by leveraging the **[Have I Been Pwned](https://haveibeenpwned.com/)** API. The script securely hashes the user's password using SHA-1, sends only the first five characters of the hash to the API, and retrieves a count of breaches associated with the password. This ensures maximum privacy and security while verifying the safety of passwords.

---

## Features

- Hashes passwords using SHA-1 algorithm securely.
- Sends only a partial hash (first 5 characters) to the API for enhanced user privacy.
- Checks the "leaked count" of a password from the **Pwned Passwords API**.
- Provides actionable feedback based on results (e.g., whether to change your password).
- Lightweight and easy to use from the terminal.

---

## Requirements

Ensure the following dependencies are installed before running the script:

- Python ≥ 3.6
- `requests` library

To install the required library, run:

```bash
pip install requests
