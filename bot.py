from operator import ge
import discord
from discord.ext import commands
import requests
from googletrans import Translator

client = commands.Bot(command_prefix = '>')

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game('Traveling the Universe...'))
    print('Bot is ready')

@client.command()
async def ping(ctx):
    await ctx.send("Pong!")

@client.command()
async def image(ctx):
    translator = Translator()
    response = requests.get("https://api.nasa.gov/planetary/apod?api_key=ol67wRzFoXgOlng82F2pHe8t6iezEbb9vxCbWJil")
    getters = response.json()
    title = getters['title']
    titles = translator.translate(title, dest="es")
    contenten = getters['explanation']
    contentenes = translator.translate(contenten, dest="es")

    embed = discord.Embed(
        title = f"{titles.text}",
        description= f"{contentenes.text}",
        colour = discord.Colour.blue()
    )

    embed.set_footer(text='Powered by Nasa Daily image.', icon_url=ctx.author.avatar_url)
    embed.set_image(url=getters['hdurl'])


    await ctx.send(embed=embed)

client.run('ODYxMjk4MDQwNTE3Mjk2MTM4.YOHwTw.o1AAoMIDmcezW_Wdq8vxwdG7UYI')
