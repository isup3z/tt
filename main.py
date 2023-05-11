
import string
import random
import requests
from bs4 import BeautifulSoup
import time
import os

def get_proxy_list(file_path):
    with open(file_path, 'r') as file:
        return file.readlines()

def generate_username(username_length, username_type):
    if username_type == '1':
        chars = string.ascii_letters
    elif username_type == '2':
        chars = string.ascii_letters + string.digits
    else:
        raise ValueError("Invalid username type. Must be 1 or 2")

    return ''.join(random.choice(chars) for _ in range(username_length))

def check_tiktok_username(username, proxy=None):
    url = f"https://www.tiktok.com/@{username}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }

    try:
        if proxy:
            response = requests.get(url, headers=headers, proxies={"http": proxy, "https": proxy}, timeout=10)
        else:
            response = requests.get(url, headers=headers, timeout=10)

        soup = BeautifulSoup(response.content, "html.parser")
        return not bool(soup.find("div", {"class": "jsx-1045706518 main"}))
    except:
        return False

def main():
    username_length = int(input("Enter the username length: "))
    username_type = input("Enter the username type (1 for letters only, 2 for letters and numbers): ")
    proxy_file = input("Enter proxy list file path (leave empty to not use proxies): ")

    proxies = []
    if proxy_file:
        proxies = get_proxy_list(proxy_file)

    available_usernames = []

    while True:
        username = generate_username(username_length, username_type)
        proxy = random.choice(proxies) if proxies else None
        is_available = check_tiktok_username(username, proxy)

        if is_available:
            available_usernames.append(username)
            print(f"Available username: {username}")

            with open("results.txt", "a") as file:
                file.write(f"{username}\n")
        else:
            print(f"Username {username} is not available")

        time.sleep(1)

if __name__ == "__main__":
    main()
