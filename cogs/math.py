import discord
from discord.ext import commands
from discord.ext.commands import Cog
from discord.ext.commands import command
import math

"""Cog intended for everything about math commands"""
class Math(Cog):
    @Cog.listener()
    async def onready(self):
        print("Math cog ready")

    @command(name="sum", aliases=["plus","add"])
    async def suma(self, ctx, num1, num2):
        try:
            result = float(num1) + float(num2)
            embed = discord.Embed(
                title="Resultado de la suma: ",
                description=f"{num1} + {num2} = {result}",
                colour=discord.Colour.blue()
            )

            await ctx.send(embed=embed)
        except ValueError:
            embed = discord.Embed(
                title="Resultado de la suma: ",
                description=f"Solo puedes sumar enteros, o flotantes",
                colour=discord.Colour.red()
            )

            await ctx.send(embed=embed)
    
    @command(name="rest", aliases=["minus"])
    async def resta(self, ctx, num1, num2):
        try:
            result = float(num1) - float(num2)
            embed = discord.Embed(
                title="Resultado de la resta: ",
                description=f"{num1} - {num2} = {result}",
                colour=discord.Colour.red()
            )

            await ctx.send(embed=embed)

        except ValueError:
            embed = discord.Embed(
                title="Resultado de la resta: ",
                description=f"Solo puedes restar enteros, o flotantes",
                colour=discord.Colour.red()
            )

            await ctx.send(embed=embed)

    @command(name="mult", aliases=["multiplica"])
    async def multiplication(self, ctx, num1, num2):
        try:
            result = float(num1) * float(num2)
            embed = discord.Embed(
                title="Resultado de la multiplicación: ",
                description=f"{num1} x {num2} = {result}",
                colour=discord.Colour.green()
            )

            await ctx.send(embed=embed)
        except ValueError:
            embed = discord.Embed(
                title="Resultado de la multiplicación: ",
                description=f"Solo puedes multiplicar enteros, o flotantes",
                colour=discord.Colour.red()
            )

            await ctx.send(embed=embed)

    @command(name="div", aliases=["divide"])
    async def division(self, ctx, num1, num2):
        try:
            result = float(num1) / float(num2)
            embed = discord.Embed(
                title="Resultado de la división: ",
                description=f"{num1} / {num2} = {result}",
                colour=discord.Colour.green()
            )

            await ctx.send(embed=embed)
        except(ValueError, ZeroDivisionError):
            embed = discord.Embed(
                title="Resultado de la división: ",
                description=f"Solo puedes dividir enteros, o flotantes. Y recuerda no dividir entre ceros",
                colour=discord.Colour.red()
            )

            await ctx.send(embed=embed)
    
    @command(name="fact", aliases=["factorial"])
    async def fact(self, ctx, num):
        try:
            result = math.factorial(int(num))
            embed = discord.Embed(
                title=f"El factorial de {num} es: ",
                description=f"S{result}",
                colour=discord.Colour.green()
            )

            await ctx.send(embed=embed)
        except(ValueError):
            embed = discord.Embed(
                title=f"Error al conseguir el factorial de {num}: ",
                description=f"Solo puedes conseguir el factorial de un número entero y positivo...",
                colour=discord.Colour.red()
            )

            await ctx.send(embed=embed)

    @command(name="pi")
    async def fact(self, ctx):
        numpi = math.pi
        embed = discord.Embed(
                title=f"Número Pi: ",
                description=f"{numpi}",
                colour=discord.Colour.blue()
        )
        await ctx.send(embed=embed)

    @command(name="pow", aliases=["potencia"])
    async def power(self, ctx, num, num2):
        try:
            result = pow(float(num), float(num2))
            embed = discord.Embed(
                    title=f"La potencia de {num} a la {num2} es: ",
                    description=f"{result}",
                    colour=discord.Colour.blue()
            )
            await ctx.send(embed=embed)
        except(ValueError):
            embed = discord.Embed(
                    title=f"Error en sacar la potencia ",
                    description=f"Recuerda solo usar enteros o flotantes",
                    colour=discord.Colour.red()
            )
            await ctx.send(embed=embed)

    @command(name="sqrt", aliases=["raiz"])
    async def raiz(self, ctx, num):
        try:
            result = math.sqrt(int(num))
            embed = discord.Embed(
                    title=f"La raiz cuadrada de {num} es: ",
                    description=f"{result}",
                    colour=discord.Colour.blue()
            )
            await ctx.send(embed=embed)


        except ValueError:
            embed = discord.Embed(
                    title=f"Error en sacar la raiz:  ",
                    description=f"Recuerda solo usar enteros o flotantes",
                    colour=discord.Colour.red()
            )

            await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Math(client))