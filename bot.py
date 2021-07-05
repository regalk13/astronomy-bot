from json.decoder import JSONDecodeError
from operator import ge
import discord
from discord.ext import commands
from discord.ext.commands.errors import ExpectedClosingQuoteError
import requests
from googletrans import Translator
import random
from glob import glob

from requests.api import request

client = commands.Bot(command_prefix = '>')
cogs = [path.split("\\")[-1][:-3] for path in glob("./cogs/*.py")]


@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.idle, activity=discord.Game('Traveling the Universe...'))
    print('Bot is ready')
    setup(client)

@client.command()
async def ping(ctx):
    await ctx.send("Pong!")

def setup(client):
    for cog in cogs:
        client.load_extension(f"cogs.{cog}")
        print(f"{cog} cog loaded")
    
    print("setup complete")

if __name__ == '__main__':
    client.run('ODYxMjk4MDQwNTE3Mjk2MTM4.YOHwTw.w49KCFb5pOICV9lEkIc6_4kNOHU')

