from pycoingecko import CoinGeckoAPI
import discord
from discord.ext import commands
from discord.ext.commands import Cog
from discord.ext.commands import command

class Crypto(Cog):
    @Cog.listener()
    async def onready(self):
        print("Crypto cog ready")

    @command(name="crypto", alias=["cprice"])
    async def cypto(self, ctx, cname):
        try:
            cg = CoinGeckoAPI()
            data = cg.get_price(ids=cname, vs_currencies='usd', include_24hr_change='true', include_last_updated_at='true')
            price = data[cname]["usd"]
            change = data[cname]['usd_24h_change']
            last_u = data[cname]['last_updated_at']

            embed = discord.Embed(
                colour = discord.Colour.green(),
            )

            embed.add_field(name=f"Aquí encontraras los datos mas actuales de {cname}:", value=f'> **Precio**: $ {price}.\n> **Cambio 24h**: $ {change}.\n> **Ultima actualización**: {last_u}.',inline=False)

            await ctx.send(embed=embed)
        except KeyError:
            embed = discord.Embed(
            title=" Parece que no usaste una moneda valida, mira la lista de monedas admitidas: ",
            description=f"Puedes tener la info de miles de monedas, mira la lista completa y data adicional [aquí](https://www.coingecko.com/en). ",
            colour = discord.Colour.red())
            
            await ctx.send(embed=embed)


    @command(name="clist", alias=["cryptonames", "crypton"])
    async def clist(self, ctx):
        embed = discord.Embed(
            title="Lista de monedas admitidas: ",
            description=f"Puedes tener la info de miles de monedas, mira la lista completa y data adicional [aquí](https://www.coingecko.com/en). ",
            colour = discord.Colour.green(),
        )

        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Crypto(client))