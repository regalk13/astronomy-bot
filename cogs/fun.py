import discord
import requests
import random
from discord.ext import commands
from discord.ext.commands import Cog
from discord.ext.commands import command

class Fun(Cog):
    @Cog.listener()
    async def onready(self):
        print("Fun cog ready")

    @command(name="gif", aliases=["giphy"])
    async def gif(self, ctx, gname):
        random_number = random.randint(0, 9)
        response = requests.get(f'https://api.giphy.com/v1/gifs/search?api_key{your_api_key}={gname}&limit=10&offset=0&rating=g&lang=en')
        getters = response.json()
        data = getters['data']
        gif_data = data[random_number]['images']['original']['url']

        embed = discord.Embed(
            colour=discord.Colour.blue()
        )

        embed.set_image(url=gif_data)

        await ctx.send(embed=embed)

    @command(name="rangif", aliases=["randomgif", "gifrandom"])
    async def rangif(self, ctx):
        random_number = random.randint(0, 9)
        response = requests.get(f'https://api.giphy.com/v1/gifs/random?api_key={your_api_key}&tag=&rating=g')
        getters = response.json()
        data = getters['data']
        gif_data = data['images']['original']['url']

        embed = discord.Embed(
            colour=discord.Colour.blue()
        )

        embed.set_image(url=gif_data)

        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Fun(client))