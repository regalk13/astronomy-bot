import discord
from discord import colour
import requests
from discord.ext import commands
from discord.ext.commands import Cog
from discord.ext.commands import command

class Quimic(Cog):
    @Cog.listener()
    async def onready(self):
        print("Fun cog ready")

    @command(name="ptable", aliases=["tablep", "quimic"])
    async def ptable(self, ctx, element):
        try:
            response = requests.get(f"https://neelpatel05.pythonanywhere.com/element/atomicname?atomicname={element}")
            getters = response.json()
            name = getters['name']
            masa = getters['atomicMass']
            anumber = getters['atomicNumber']
            color = getters['cpkHexColor']
            density = getters['density']
            group = getters['groupBlock']
            state = getters['standardState']
            symbol = getters['symbol']
            discover = getters['yearDiscovered']

            embed = discord.Embed(
                title=f"Datos de {name}",
                colour=discord.Colour.green()
            )

            embed.add_field(name=f"Datos del elemento {name}:", value=f'> **Masa**: {masa}.\n> **Número Atomico**: $ {anumber}.\n> **Densidad**: {density}.\n> **Grupo**: {group}.\n> **Estado**: {state}. \n> **Simbolo**: {symbol}. \n> **Descubierto**: {discover}.',inline=False)
            embed.set_footer(text='Periodic Table API.')
            
            await ctx.send(embed=embed)
        
        except KeyError:
            embed = discord.Embed(
            title="Elemento no encontrado: ",
            description="Recuerda que los nombres deben ser en ingles.",
            colour = discord.Colour.green(),
            )

        embed.set_image(url='https://sciencenotes.org/wp-content/uploads/2015/08/ColorPeriodicTable2015Posterized.png')

        await ctx.send(embed=embed)


    @command(name="plist", alias=["elementnames", "elements"])
    async def plist(self, ctx):
        embed = discord.Embed(
            title="Nombre de todos los elementos: ",
            colour = discord.Colour.green(),
        )

        embed.set_image(url='https://sciencenotes.org/wp-content/uploads/2015/08/ColorPeriodicTable2015Posterized.png')

        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Quimic(client))