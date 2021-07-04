from operator import ge
import discord
from discord.ext import commands
import requests
from googletrans import Translator
import random

from requests.api import request

client = commands.Bot(command_prefix = '>')

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game('Traveling the Universe...'))
    print('Bot is ready')

@client.command()
async def ping(ctx):
    await ctx.send("Pong!")

@client.command()
async def daily(ctx):
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

@client.command()
async def rober(ctx, *, target):
    response = requests.get("https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=1000&api_key=ol67wRzFoXgOlng82F2pHe8t6iezEbb9vxCbWJil")
    getters = response.json()
    random_number = random.randint(1, 1000)
    image = getters['photos']
    images = image[random_number]
    image_src = images['img_src']
    bot = images['rover']
    bot_name = bot['name']
    date = images['earth_date']

    embed = discord.Embed(
        title = "Imagen de marte:",
        description = f"Imagen tomada por **{bot_name}** el _{date}_ :",
        colour = discord.Colour.red()
    )

    embed.set_footer(text='Powered by Curiosity bot.', icon_url=ctx.author.avatar_url)
    embed.set_image(url=image_src)

    await ctx.send(embed=embed)


@client.command()
async def data(ctx,*,target):
    translator = Translator()
    response = requests.get(f"https://api.le-systeme-solaire.net/rest/bodies/{target}")
    getters = response.json()
    name = getters['englishName']
    name_es = translator.translate(name, dest="es")
    planet  = getters['isPlanet']
    mass_data = getters['mass']
    mass_value = mass_data['massValue']
    vol_data = getters['vol']
    vol_value = vol_data['volValue']
    density = getters['density']
    gravity = getters['gravity']


    embed = discord.Embed(
        title = f"Datos de {name_es.text}:",
        colour = discord.Colour.red()
    )

    embed.add_field(name="Aqui encontraras datos exactos acerca de tu peticion:", value=f'> Nombre: {name}/{name_es.text}.\n> Planeta: {planet}.\n> Masa: {mass_value}.\n> Volumen: {vol_value}.\n> Densidad: {density}.\n> Gravedad: {gravity}.',inline=False)
    embed.set_footer(text='Powered by Solaire API.')

    await ctx.send(embed=embed)

@client.command()
async def iss(ctx):
    response = requests.get("https://api.wheretheiss.at/v1/satellites/25544")
    getters = response.json()
    iss_latitude = getters['latitude']
    iss_longitude = getters['longitude']
    iss_altitude = getters['altitude']
    iss_velocity = getters['velocity']

    embed = discord.Embed(
        title="Estación espacial",
        colour = discord.Colour.green()
    )

    embed.add_field(name=f'**Datos en base al sitio de toma:**', value=f'> Latitud: {iss_latitude}Km.\n> Longitud: {iss_longitude}Km.\n> Altitud: {iss_altitude}Km.\n> Velocidad: {iss_velocity}K/h.',inline=False)

    await ctx.send(embed=embed)

client.run('ODYxMjk4MDQwNTE3Mjk2MTM4.YOHwTw.oFFFpTaCujN4uNJATvhZnlbj8ig')
