import discord
from discord.ext import commands

class Ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command()
    async def ping(self, ctx):
        try:
            await ctx.send("pong")
        except Exception as e:
            print(e)

async def setup(bot):
    await bot.add_cog(Ping(bot))
