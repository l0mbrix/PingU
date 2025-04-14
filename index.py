# Importations
from dotenv import load_dotenv
import os
import discord
import random

# Loadings
load_dotenv()
TOKEN = os.getenv("TOKEN")

# Intents Discord to be defined
intents = discord.Intents.default()
intents.message_content = True

# Creating a client intent
client = discord.Client(intents=intents)

# Funny answers #
PING_ANSWERS = [
    "Answer 1",
    "Answer 2",
    "Answer 3",
    "Answer 4",
    "Answer 5",
]


@client.event
async def on_message(message):
    print("Pong !")
    # Check if the message is from a bot
    if message.author.bot:
        return

    # Check if the message is a ping
    if message.content.startswith("!ping"):
        print("Ping received !")
        # Send a random answer from the list
        await message.channel.send(random.choice(PING_ANSWERS))

# Discord token
client.run(TOKEN)