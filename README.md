# Brute Force Login Script
This is a brute force script developed for educational purposes, demonstrating a basic brute force attack technique to discover login credentials. The script attempts various combinations of username and password until it finds the correct one. This project was created to help beginner pentesters understand how brute force scripts work.

## Warning: 
This script should only be used in controlled environments with explicit permission. Unauthorized use of this script on unauthorized systems is illegal and can lead to severe legal consequences.

# How It Works
The script attempts to log in by sending POST requests to a specific URL. It uses a list of possible passwords stored in a text file and checks if the server's response indicates a successful login.

### Requirements

* Python 3.x
* requests library
* A locally running web server with a login form.

### Download
To download the project, you can clone the repository using Git:

git clone https://github.com/yourusername/brute_force_login_script.git

Alternatively, you can download the ZIP file directly from GitHub and extract it to your preferred location.


# Setup and Execution
### 1. Server Setup

Before running the brute force script, you need to set up a web server that contains a login form. Below is an example of a simple HTML login form:

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login Page</title>
</head>
<body>
    <h2>Login</h2>
    <form method="POST" action="/login">
        <label for="username">Username:</label><br>
        <input type="text" id="username" name="username"><br><br>
        <label for="password">Password:</label><br>
        <input type="password" id="password" name="password"><br><br>
        <input type="submit" value="Login">
    </form>
</body>
</html>



