import discord
from discord.ext import commands
from discord.ext.commands import Cog
from discord.ext.commands import command

class Math(Cog):
    @Cog.listener()
    async def onready(self):
        print("Math cog ready")


def setup(client):
    client.add_cog(Math(client))