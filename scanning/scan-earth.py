from os import *
from colorama import *
from rich.tree import Tree
from rich import print as rprint
import socket
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
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠛⠛⠛⠛⠋⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀

                        ©️ Project : Moon Copright to TheSadError

                        ---INFO---
                        DIR : /moon/scanning/
                        IP  : {ip}
    """)
    tree = Tree(Fore.RED+"[Scanning Tools]")
    tree.add(Fore.RED+"[1] Information Gathering By Username (OSINT)")
    tree.add(Fore.RED+"[2] Port Scanning (Find vulnerable port with versions)")

    rprint(tree)


def main():
    menu()
    print(" ")
    cmd = input(Fore.BLUE+"[!] Choice : ")

    if cmd == "1":
        system("sudo python3 ./scanning/osint.py")
    elif cmd == "2":
        system("sudo python3 ./scanning/portscan.py")

if __name__ == "__main__":
    user = geteuid()
    if user == 0:
        system("clear")
        main()
    else:
        print(Fore.RED+"[!] WARNING : Mr. Moon need privileges! Please run code by sudo!")
