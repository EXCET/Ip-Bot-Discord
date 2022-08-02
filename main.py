import discord 
from discord.ext import commands
import os
import time
import string
import random
import threading
import requests

token = "OTM0MTkyOTY5MDcyOTM1MDU1.GugHTq.AIDYANQpbKYHv1xvVV4k_RVATz3AansFJurhv0"

prefix = "!"

bot = commands.Bot(command_prefix=prefix, help_command=None)

@bot.command()
async def iplocate(ctx, ip):
  headers = {
        'authority': 'ipinfo.io',
        'accept': '*/*',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'content-type': 'application/json',
        'referer': 'https://ipinfo.io/',
        'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
        }
  r = requests.get(f'https://ipinfo.io/widget/demo/{ip}', headers=headers)
  ip = r.json()['data']['ip']
  city = r.json()['data']['city']
  region = r.json()['data']['region']
  country = r.json()['data']['country']
  timezone = r.json()['data']['timezone']
  address = r.json()['data']['abuse']['address']
  country = r.json()['data']['abuse']['country']
  await ctx.send(ip)
  await ctx.send(city)
  await ctx.send(region)
  await ctx.send(country)
  await ctx.send(address)
  await ctx.send(timezone)
  
bot.run(token)
