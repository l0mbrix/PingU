# Importations
from dotenv import load_dotenv
import os
import discord
from discord import app_commands
from discord.ext import commands
import random
import sqlite3

# Loadings
load_dotenv()
TOKEN = os.getenv("TOKEN")

# Database creation

# Intents Discord to be defined
intents = discord.Intents.default()

# Creating a bot listening to !
bot = commands.Bot(command_prefix="!", intents=intents)

# Funny answers #
VALO_ANSWERS = [
    "Answer 1",
    "Answer 2",
    "Answer 3",
    "Answer 4",
    "Answer 5",
]

@bot.event
# Check reactions
async def on_reaction_add(reaction, user):
    if user.bot:
        return

    if reaction.message.id == 1361274589992194128:
        if str(reaction.emoji.valorant) == "🔫":
            print(f"{user.name} reacted with {reaction.emoji.valorant} at {reaction.message.id}") # Console check
            add_user_to_db(user.id, "Valorant")

        if str(reaction.emoji.moria) == "🏔":
            print(f"{user.name} reacted with {reaction.emoji.moria} at {reaction.message.id}") # Console check
            add_user_to_db(user.id, "Moria")

        if str(reaction.emoji.helldivers2) == "🫡":
            print(f"{user.name} reacted with {reaction.emoji.helldivers2} at {reaction.message.id}") # Console check
            add_user_to_db(user.id, "Helldivers2")

        if str(reaction.emoji.aoe) == "⚔️":
            print(f"{user.name} reacted with {reaction.emoji.aoe} at {reaction.message.id}") # Console check
            add_user_to_db(user.id, "AoE")

# Check !ping
@bot.tree.command(name="valo", description="Someone wants to play Valorant in your server.")
async def valo(interaction: discord.Interaction):
    await interaction.response.send_message(random.choice(VALO_ANSWERS))

# @bot.event
# async def on_message(message):
    # print("Pong !")
    # Check if the message is from a bot
    # if message.author.bot:
        # return

@bot.event
async def on_ready():
    await bot.tree.sync()
    print(f"{bot.user} is ready !")

# Discord token
bot.run(TOKEN)