# Password Manager

## Description

This is a simple command-line password manager written in Python. It allows users to register with a master password, log in, and securely store and retrieve passwords for various websites. Passwords are encrypted using the `cryptography` library to ensure security.

## Features

- Register with a master password
- Login with the master password
- Add and save passwords for websites
- Retrieve saved passwords for websites
- View a list of saved websites
- Passwords are encrypted for security

## Requirements

- Python 3.12
- `cryptography` library
- `pyperclip` library

## Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/ghalibfaruqe101/password_manager.git
    cd password_manager
    ```

2. **Install required libraries:**
    ```bash
    pip install cryptography pyperclip
    ```

## Usage

1. **Run the script:**
    ```bash
    python password_manager.py
    ```

2. **Follow the on-screen prompts:**
    - Choose option `1` to register a new user.
    - Choose option `2` to log in with an existing user.
    - After logging in, choose from the following options:
        - `1` to add a new password.
        - `2` to retrieve a saved password.
        - `3` to view saved websites.
        - `4` to quit.

## Example

