from json.decoder import JSONDecodeError
from operator import ge
import discord
from discord.ext import commands
from discord.ext.commands.errors import ExpectedClosingQuoteError
import requests
from googletrans import Translator
import random
from pathlib import Path
from glob import glob
import time

from requests.api import request

client = commands.Bot(command_prefix = '>')
cogs = [p.stem for p in Path(".").glob("./cogs/*.py")]


@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.idle, activity=discord.Game('Traveling the Universe...'))
    print('Bot is ready')
    setup(client)

@client.command()
async def ping(ctx):
    start = time.time()
    message = await ctx.send(f"Pong! latencia: {client.latency*1000:,.0f} ms.")
    end = time.time()

    await message.edit(content=f"Pong! latencia: {client.latency*1000:,.0f} ms. Tiempo de respuesta: {(end-start)*1000:,.0f} ms.")

def setup(client):
    for cog in cogs:
        client.load_extension(f"cogs.{cog}")
        print(f"{cog} cog loaded")
    
    print("setup complete")

if __name__ == '__main__':
    client.run(Your_Token)

