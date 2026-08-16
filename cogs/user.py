import discord
from discord import app_commands
from discord.ext import commands

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
    async def avatar_(self, interaction: discord.Interaction, member: discord.Member=None):
        try:
            user_avatar = member.display_avatar.url
            await interaction.response.send_message(user_avatar)
        except Exception as e:
            print(e)
async def setup(bot):
    await bot.add_cog(User(bot))
        
