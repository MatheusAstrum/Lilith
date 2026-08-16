import discord
from discord import app_commands
from discord.ext import commands
from random import *

class User(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command()
    async def avatar(self, ctx, avatar: discord.Member=None):
        try:
            user_avatar = avatar.display_avatar.url
            await ctx.send(user_avatar)
        except Exception as e:
            await ctx.send(e)

    @app_commands.command(name="avatar", description="mostra a foto de perfil")
    async def avatar_slash(self, interaction: discord.Interaction, member: discord.Member=None):
        try:
            user_avatar = member.display_avatar.url
            await interaction.response.send_message(user_avatar)
        except Exception as e:
            print(e)



    @commands.command()
    async def ship(self, ctx, member1: discord.Member, member2: discord.Member):
        try:
            resultado = randrange(100)
            await ctx.send(f"O amor entre {member1.mention} e {member2.mention} é de {resultado}%")
        except Exception as e:
            print(e)


    @app_commands.command(name="ship", description="valor do ship")
    async def ship_slash(self, interaction: discord.Interaction, member1: discord.Member, member2: discord.Member):
        try:
            resultado = randrange(100)
            await interaction.response.send_message(f"O ship entre {member1.mention} e {member2.mention} é de {resultado}%")
        except Exception as e:
            print(e)
async def setup(bot):
    await bot.add_cog(User(bot))

