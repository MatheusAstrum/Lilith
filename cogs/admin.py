import discord
from discord import app_commands
from discord.ext import commands

class Admin(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(administrator=True)
    
    async def ban(self, ctx, member: discord.Member, reason=None):

        await ctx.send(f"usuário banido {member.name}")
        await member.ban(reason=reason)

    @app_commands.command(name="banir", description="banee")
    @commands.has_permissions(administrator=True)
    async def banir(self, interaction: discord.Interaction, member: discord.Member):
        await member.ban(reason="banido")
        await Interaction.response.send_message(f"Usuário {member.mention} banido.")

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def kickar(self, ctx, member: discord.Member):

        await member.kick(reason="kickado")
        await ctx.send(f"Membro {member.mention} expulso.")


    @app_commands.command(name="kick", description="kicka um usuário")
    @commands.has_permissions(administrator=True)
    async def kick(self, interaction: discord.Interaction, member: discord.Member):

        await member.kick(reason="kickado")
        await interaction.response.send_message(f"Usuario {member.mention} expulso.")
    
async def setup(bot):
    await bot.add_cog(Admin(bot))
