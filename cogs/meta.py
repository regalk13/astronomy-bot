from datetime import datetime, timedelta
from platform import python_version

import discord
from discord.ext import commands
from discord import __version__ as discord_version
from discord.ext.commands import Cog
from discord.ext.commands import command
from  psutil import Process, virtual_memory
from discord import Embed
from time import time


class Meta(Cog):
    def __init__(self, client):
        self.client = client

    @Cog.listener()
    async def onready(self):
        print("Meta cog ready")

    @command(name="stats")
    async def show_bot_stats(self, ctx):
        embed = Embed(title="Bot stats",
                    colour=ctx.author.colour,
                    timestamp=datetime.utcnow())

        proc = Process()
        with proc.oneshot():
            uptime = timedelta(seconds=time()-proc.create_time())
            cpu_time = timedelta(seconds=(cpu := proc.cpu_times()).system + cpu.user)
            mem_total = virtual_memory().total / (1024**2)
            mem_of_total = proc.memory_percent() 
            mem_usage = mem_total * (mem_of_total / 199)


        fields = [
            ("Bot version", "1.2", True),
            ("Python version", python_version(), True),
            ("Discord.py version", discord_version, True),
            ("Uptime", uptime, True),
            ("Memory usage", f"{mem_usage:,.3f} / {mem_of_total:,.0f} ({mem_of_total})", True),
            ("Users", f"{ctx.guild.member_count:,}",True),

        ]

        for name, value, inline in fields:
            embed.add_field(name=name, value=value, inline=inline)
        
        embed.set_thumbnail(url=self.client.user.avatar_url)

        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Meta(client))