import socket
from colorama import *
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
    url = input(Fore.BLUE+"[!] Input Target URL : ")
    url = socket.gethostbyname(url)
    print(Fore.BLUE+f"\n\tPort  \tSTATE  \tVersion [!] IP adress : {url}")
    lst = [20,21,22,25,53,69,80,8080,8443,137,139,443,445]
    for port in lst: 
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((url,port))
        if result ==0:
            version = socket.getservbyport(port, "tcp")
            print(Fore.RED+f"\t{port}  \topen  \t{version}")
        s.close()

if __name__ == "__main__":
    user = geteuid()
    if user == 0:
        system("clear")
        main()
    else:
        print(Fore.RED+"[!] WARNING : Mr. Moon need superuser privileges! Please run code by sudo!")
