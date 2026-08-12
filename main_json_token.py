import discord
from discord.ext import commands
import json

with open("config.json") as file:
    data = json.load(file)
    TOKEN = data["TOKEN"]
    
intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print("Lilith iniciada")

bot.run(TOKEN)
