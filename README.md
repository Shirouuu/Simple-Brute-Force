# Brute Force Login Script
This is a brute force script developed for educational purposes, demonstrating a basic brute force attack technique to discover login credentials. The script attempts various combinations of username and password until it finds the correct one. This project was created to help beginner pentesters understand how brute force scripts work.

## Warning: 
This script should only be used in controlled environments with explicit permission. Unauthorized use of this script on unauthorized systems is illegal and can lead to severe legal consequences.

# How It Works
The script attempts to log in by sending POST requests to a specific URL. It uses a list of possible passwords stored in a text file and checks if the server's response indicates a successful login.

# Requirements

* Python 3.x
* requests library
* A locally running web server with a login form.

  
