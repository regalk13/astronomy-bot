import discord
from discord.ext import commands
from discord.ext.commands import Cog
from discord.ext.commands import command

class Meta(Cog):
    @Cog.listener()
    async def onready(self):
        print("Fun cog ready")




def setup(client):
    client.add_cog(Meta(client))