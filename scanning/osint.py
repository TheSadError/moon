from os import *
from colorama import *
from rich.tree import Tree
from rich import print as rprint
import socket
import requests
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
                        DIR : /moon/osint/
                        IP  : {ip}
    """)

def main():
    urllst = [
    "https://github.com/",
    "https://www.behance.net/",
    "https://www.instagram.com/",
    "https://forums.adobe.com/people/",
    "https://angel.co/u/",
    "http://blackplanet.com/",
    "https://www.canva.com/",
    "https://www.codementor.io/@",
    "https://evewho.com/pilot/",
    "http://www.fanpop.com/",
    "https://fotolog.com/",
    "https://www.furaffinity.net/user/",
    "https://gpodder.net/user/",
    "https://www.investing.com/traders",
    "https://www.khanacademy.org/profile/",
    "https://kiwifarms.net/members/?username=",
    "https://forum.redsun.tf/members/?username=",
    "https://creativemarket.com/users/",
    "http://pedsovet.su/index/8-0-",
    "https://radioskot.ru/index/8-0-",
    "https://coderwall.com/",
    "https://tamtam.chat/",
    "https://www.zomato.com/pl/",
    "https://mixer.com/",
    "https://world.kano.me/",
    "https://yandex.ru/collections/user/",
    "https://www.paypal.com/paypalme/",
    "https://www.crunchyroll.com/user/",
    "https://support.t-mobile.com/people/",
    "https://about.me/",
    "https://independent.academia.edu/",
    "https://airbit.com/",
    "https://www.alik.cz/u/",
    "https://allmylinks.com/",
    "https://anilist.co/user/",
    "https://developer.apple.com/forums/profile/",
    "https://discussions.apple.com/profile/",
    "https://www.artstation.com/",
    "https://asciinema.org/~",
    "https://ask.fedoraproject.org/u/",
    "https://ask.fm/",
    "https://audiojungle.net/user/",
    "https://www.autofrage.net/nutzer/",
    "https://www.avizo.cz/",
    "https://www.bazar.cz/",
    "https://bezuzyteczna.pl/uzytkownicy/",
    "https://binarysearch.io/@/",
    "https://forum.dangerousthings.com/u/",
    "https://bitbucket.org/",
    "https://bitcoinforum.com/profile/",
    "https://gitlab.com/",
    "https://www.goodreads.com/",
    "https://plugins.gradle.org/u/",
    "https://www.grailed.com/",
    "http://en.gravatar.com/",
    "https://forums.gunsandammo.com/profile/",
    "https://www.gutefrage.net/nutzer/",
    "https://hackaday.io/",
    "https://hackerearth.com/@",
    "https://news.ycombinator.com/user?id="
]
    print(" ")
    menu()
    us = input(Fore.RED+"[!] Input username of victim : ")
    print(Fore.BLUE+f"""
--> OSINT SCAN
    Username : {us}
    Websites : {len(urllst)} 
    """)
    for i in range(0,len(urllst)):
        req = requests.get(urllst[i]+us)
        if(req.status_code == 200):
            try : 
                print(Fore.GREEN+f"{[i]} User Found! URL : {urllst[i]}{us}")
            except:
                print("[-] WARNING : Please connect Internet! ")
        else:
            print(Fore.RED+f"{[i]} User Not Found! URL : {urllst[i]}{us}")
    print(" ")

if __name__ == "__main__":
    user = geteuid()
    if user == 0:
        system("clear")
        main()
    else:
        print(Fore.RED+"[!] WARNING : Mr. Moon need privileges! Please run code by sudo!")
