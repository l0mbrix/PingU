# Importations #
from dotenv import load_dotenv
import os
import discord
import random

# Loadings
load_dotenv()
Token = os.getenv("DISCORD_TOKEN")

# Intents Discord to be defined

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
    # Check if the message is from a bot
    if message.author.bot:
        return

    # Check if the message is a ping
    if message.content.startswith("!ping"):
        # Send a random answer from the list
        await message.channel.send(random.choice(PING_ANSWERS))

# Insert the Discord bot token here (careful: don't share it on GitHub)
client.run(TOKEN)