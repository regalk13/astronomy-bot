import discord
from discord.ext import commands
from discord.ext.commands import Cog
from discord.ext.commands import command

class Help(Cog):
    @Cog.listener()
    async def onready(self):
        print("Help cog ready")

    

def setup(client):
    client.add_cog(Help(client))