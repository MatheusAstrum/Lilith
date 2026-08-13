import discord
from discord.ext import commands
import json
import asyncio

with open("config.json") as file:
    data = json.load(file)
    TOKEN = data["TOKEN"]
    
intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():

    await bot.tree.sync()
    print("Lilith iniciada")
    

async def main():
    async with bot:
        await bot.load_extension("cogs.ping")
        await bot.start(TOKEN)

asyncio.run(main())
