from json.decoder import JSONDecodeError
from operator import ge
import discord
from discord.ext import commands
from discord.ext.commands.errors import ExpectedClosingQuoteError
import requests
from googletrans import Translator
import random
from discord.ext.commands import Cog
from discord.ext.commands import command

"""Cog intended for everything about astronomy commands"""

class Astronomy(Cog):
    def __init__(self, client):
        self.client = client

    @command(name="daily", aliases=["diario"])
    async def daily(self, ctx):
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

        embed.set_footer(text='Powered by NASA Daily image', icon_url='https://cdn.discordapp.com/emojis/764531877012308010.png?v=1')
        embed.set_image(url=getters['hdurl'])


        await ctx.send(embed=embed)

    @command(name="rover", aliases=["mars"])
    async def rover(self, ctx):
        response = requests.get("https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=1000&api_key=ol67wRzFoXgOlng82F2pHe8t6iezEbb9vxCbWJil")
        getters = response.json()
        random_number = random.randint(1, 100)
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

        embed.set_footer(text='Powered by NASA rovers images', icon_url='https://cdn.discordapp.com/emojis/764531877012308010.png?v=1')
        embed.set_image(url=image_src)

        await ctx.send(embed=embed)

    @command(name="data")
    async def data(self, ctx,*,target):
        try:
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
                colour = discord.Colour.orange()
            )

            embed.add_field(name="Aquí encontraras datos exactos acerca de tu petición:", value=f'> **Nombre**: {name}/{name_es.text}.\n> **Planeta**: {planet}.\n> **Masa**: {mass_value}.\n> **Volumen**: {vol_value}.\n> **Densidad**: {density}.\n> **Gravedad**: {gravity}.',inline=False)
            embed.set_footer(text='Powered by Solaire API', icon_url='https://api.le-systeme-solaire.net/assets/images/logo.png')
            await ctx.send(embed=embed)
        
        except JSONDecodeError:
            await ctx.send("<:bmori:853933148076638228> No se encuentra el objeto pedido...")


    @command(name="iss", aliases=["eei"])
    async def iss(self, ctx):
        response = requests.get("https://api.wheretheiss.at/v1/satellites/25544")
        getters = response.json()
        iss_latitude = getters['latitude']
        iss_longitude = getters['longitude']
        iss_altitude = getters['altitude']
        iss_velocity = getters['velocity']

        embed = discord.Embed(
            title="Estación Espacial Internacional",
            colour = discord.Colour.green()
        )

        embed.add_field(name=f'**Datos en base al sitio de toma:**', value=f'> Latitud: {iss_latitude} Km.\n> Longitud: {iss_longitude} Km.\n> Altitud: {iss_altitude} Km.\n> Velocidad: {iss_velocity} K/h.',inline=False)
        embed.set_thumbnail(url='https://upload.wikimedia.org/wikipedia/commons/thumb/b/bb/ISS_insignia.svg/240px-ISS_insignia.svg.png')
        await ctx.send(embed=embed)


    @Cog.listener()
    async def onready(self):
        print("Astronomy cog ready")

def setup(client):
    client.add_cog(Astronomy(client))