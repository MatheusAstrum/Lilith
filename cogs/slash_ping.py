import discord
from discord import app_commands
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


    @app_commands.command(name="ping", description="pong")
    async def ping2(self, interaction: discord.Interaction):
        await interaction.response.send_message("pong", ephemeral=True)
        
async def setup(bot):
    await bot.add_cog(Ping(bot))
