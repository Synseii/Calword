import asyncio
import os
import sys
import os.path
import requests
import webbrowser
from time import sleep
from colored import fg, attr
from requests.api import options
import getpass
username = getpass.getuser()

from utilities.Settings.common import *


def menu():
    Write.Print(f"""

                                ▄▄·  ▄▄▄· ▄▄▌  ▄▄▌ ▐ ▄▌      ▄▄▄  ·▄▄▄▄  
                               ▐█ ▌▪▐█ ▀█ ██•  ██· █▌▐█▪     ▀▄ █·██▪ ██  
                               ██ ▄▄▄█▀▀█ ██▪  ██▪▐█▐▐▌ ▄█▀▄ ▐▀▀▄ ▐█· ▐█▌ calword.lol
                               ▐███▌▐█ ▪▐▌▐█▌▐▌▐█▌██▐█▌▐█▌.▐▌▐█•█▌██. ██  Found {counttokens} Tokens
                               ·▀▀▀  ▀  ▀ .▀▀▀  ▀▀▀▀ ▀▪ ▀█▄▀▪.▀  ▀▀▀▀▀▀•  discord.gg/calword     """)
    Write.Print("                               ╭╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╮\n", custom, interval=0.000)
    print(Colorate.Horizontal(custom, f"                                        [01] Server Info\n", custom, interval=0.000))
    print(Colorate.Horizontal(custom, f"                                        [02] Exit\n", custom, interval=0.000))
    Write.Print("                               ╰╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╯\n", custom, interval=0.000)
menu()

option = Write.Input(f"          [calword@{username}] <~> ", custom, interval=0.0025)


def fetch_data():
        menu()
if option == 1:
        sleep(1)

        headers = {
            'User-Agent' : 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.12) Gecko/20050915 Firefox/1.0.7',
            'Authorization' : Write.Input(f"\n [calword@token] <~>", custom, interval=0.009)
        }

        guildId = Write.Input(f"\n [calword@serverid] <~>", custom, interval=0.009)

        response = requests.get(
            f"https://discord.com/api/guilds/{guildId}",
            headers = headers,
            params = {"with_counts" : True}
        ).json()

        owner = requests.get(
            f"https://discord.com/api/guilds/{guildId}/members/{response['owner_id']}",
            headers = headers,
            params = {"with_counts" : True}
        ).json()
        Write.Print("╭╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╮\n", custom, interval=0.000)
        print(f"""

[calword@name] </> {response['name']} 
[calword@id] </> {response['id']}
[calword@owner] </> {owner['user']['username']}#{owner['user']['discriminator']} 
[calword@ownerid] </> {response['owner_id']}
[calword@members] </> {response['approximate_member_count']}
[calword@region] </> {response['region']}
[calword@icon] </> https://cdn.discordapp.com/icons/{guildId}/{response['icon']}.webp?size=256
""")
        Write.Print("╰╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╯\n", custom, interval=0.000)
        Write.Input(f'\n [calword@back] <~> Press anything to go back.', custom, interval=0.009)
        sleep(6)
