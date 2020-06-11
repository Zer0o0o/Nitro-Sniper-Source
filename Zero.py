import discord
import asyncio
from discord.ext import commands
import re,requests
from colorama import Fore, init
import os

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="NItro"))
    print("ready")

@bot.event
async def on_message(message):
    Userowner = bot.get_user() # Your id discord
    if message.content.startswith('https://discord.gift/'):
        code = re.search("https://discord.gift/(.*)", message.content).group(1)
        if len(code) != 16:
            print("[X] fake code")
            await message.channel.send("[x] fake code : https://discord.gift/"+code) # sent message to channel it afteryou
        else:
            print(Fore.RED+"[+-] Snipped code : https://discord.gift/"+code+Fore.RESET)
            await Userowner.send("[+-] Snipped code : https://discordapp.com/gifts"+code)
            r = requests
            result = r.post('https://discordapp.com/api/v6/entitlements/gift-codes/'+code+'/redeem')
            if 'This gift has been redeemed already.' in result:
                print("[-] already reddem")
            elif 'nitro' in result:
                print(Fore.GREEN+"[+] found nitro : https://discord.gift/"+code+Fore.RESET)
                await Userowner.send("[+] found nitro : https://discordapp.com/gifts"+code)
            elif 'Unknow Gift Code' in result:
                print("[-] Invaild Code")

    if message.content.startswith('https://discordapp.com/gifts'):
        codes = re.search("https://discordapp.com/gifts/(.*)", message.content).group(1)
        if len(codes) != 16:
            print("[X] fake code")
            await message.channel.send("[x] fake code : https://discordapp.com/gifts/"+codes) # sent message to channel it afterup
        else:
            print(Fore.RED+"[+-] Snipped code : https://discordapp.com/gifts/"+codes+Fore.RESET)
            await Userowner.send("[+-] Snipped code : https://discordapp.com/gifts"+code)
            r = requests
            result = r.post('https://discordapp.com/api/v6/entitlements/gift-codes/'+codes+'/redeem')
            if 'This gift has been redeemed already.' in result:
                print("[-] already reddem")
            elif 'nitro' in result:
                print(Fore.GREEN+"[+] found nitro : https://discordapp.com/gifts"+codes+Fore.RESET)
                await Userowner.send("[+] found nitro : https://discordapp.com/gifts"+codes)
            elif 'Unknow Gift Code' in result:
                print("[-] Invaild Code")


bot.run('')
