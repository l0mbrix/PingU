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
conn = sqlite3.connect("registrations.db") # Create/open a database file
cursor = conn.cursor() # 'Pen' allowing to write in the database -> execute and fetch
cursor.execute("""
    CREATE TABLE IF NOT EXISTS registrations (
        user_id INTEGER, 
        game TEXT)
""") # Creating a table if none
conn.commit() # Saving changes

# Add or check user in 'registrations' db
def add_user_to_db(user_id, game):
    cursor.execute("SELECT * FROM registrations WHERE user_id = ? AND game = ?", (user_id, game)) # Check both parameters before doing anything
    result = cursor.fetchone() # Fetch first line found or none if nothing found
    if result is None:
        cursor.execute("INSERT INTO registrations (user_id, game) VALUES (?, ?)", (user_id, game))
        conn.commit()
    else:
        print(f"User {user_id} is already registered in the database for {game}.")

# Remove user in 'registrations' db
def remove_user_from_db(user_id, game):
    cursor.execute("DELETE FROM registrations WHERE user_id = ? AND game = ?", (user_id, game))
    conn.commit()
    print(f"User {user_id} has been removed from the database for {game}.")

# Discord intents
intents = discord.Intents.default()
intents.reactions = True # To get reactions
intents.members = True # To get members
intents.message_content = True # To get message content

# Giving the bot what to "hear"
bot = commands.Bot(command_prefix="!", intents=intents)

# Funny answers #
valo_answers = [
    "Answer 1",
    "Answer 2",
    "Answer 3",
    "Answer 4",
    "Answer 5",
]

moria_answers = [
    "Answer 1",
    "Answer 2",
    "Answer 3",
    "Answer 4",
    "Answer 5",
]

hd2_answers = [
    "Answer 1",
    "Answer 2",
    "Answer 3",
    "Answer 4",
    "Answer 5",
]

aoe_answers = [
    "Answer 1",
    "Answer 2",
    "Answer 3",
    "Answer 4",
    "Answer 5",
]

@bot.event
# Initial check for reaction
async def on_ready():
    await bot.tree.sync()
    print(f"{bot.user} is ready !")

    channel = bot.get_channel(1260591984985378940)
    message = await channel.fetch_message(1361274589992194128)

    for reaction in message.reactions:
        async for user in reaction.users():
            if user.bot:
                continue

            # Check if the user is already in the database
            # cursor.execute("SELECT * FROM registrations WHERE user_id = ? AND game = ?", (user.id, "Valorant"))
            # result = cursor.fetchone()
            # if result is None:
                # add_user_to_db(user.id, "Valorant")

            emoji = str(reaction.emoji)

            if emoji == "🔫":
                add_user_to_db(user.id, "Valorant")
            elif emoji == "🏔":
                add_user_to_db(user.id, "Moria")
            elif emoji == "🫡":
                add_user_to_db(user.id, "Helldivers 2")
            elif emoji =="⚔️":
                add_user_to_db(user.id, "AoE")

# Check reactions
@bot.event
async def on_reaction_add(reaction, user):
    if user.bot:
        return

    if reaction.message.id == 1361274589992194128:
        emoji = str(reaction.emoji)

        if emoji == "🔫":
            print(f"{user.name} reacted with {emoji} at {reaction.message.id}") # Console check
            add_user_to_db(user.id, "Valorant")

        elif emoji == "🏔":
            print(f"{user.name} reacted with {emoji} at {reaction.message.id}") # Console check
            add_user_to_db(user.id, "Moria")

        elif emoji == "🫡":
            print(f"{user.name} reacted with {emoji} at {reaction.message.id}") # Console check
            add_user_to_db(user.id, "Helldivers 2")

        elif emoji == "⚔️":
            print(f"{user.name} reacted with {emoji} at {reaction.message.id}") # Console check
            add_user_to_db(user.id, "AoE")

# On reaction remove
@bot.event
async def on_reaction_remove(reaction, user):
    if user.bot:
        return

    if reaction.message.id == 1361274589992194128:
        emoji = str(reaction.emoji)

        if emoji == "🔫":
            remove_user_from_db(user.id, "Valorant")

        elif emoji == "🏔":
            remove_user_from_db(user.id, "Moria")

        elif emoji == "🫡":
            remove_user_from_db(user.id, "Helldivers 2")

        elif emoji == "⚔️":
            remove_user_from_db(user.id, "AoE")

@bot.tree.command(name="valo", description="Ping les joueurs de Valorant 🔫")
async def valo(interaction: discord.Interaction):

    cursor.execute("SELECT user_id FROM registrations WHERE game = ?", ("Valorant",))
    user_ids = cursor.fetchall()

    mentions = []
    for row in user_ids:
        user_id = row[0]
        user = await bot.fetch_user(user_id)
        mentions.append(user.mention)

    if mentions:
        message = random.choice(valo_answers) + "\n" + " ".join(mentions)
    else:
        message = "Oups ! Aucun autre agent disponible pour désamorcer le spike... Il va falloir 'piou piou' solo. 🔫"
    await interaction.response.send_message(message)

@bot.tree.command(name="nains", description="Ping les joueurs de Return To The Moria 🏔")
async def nains(interaction: discord.Interaction):

    cursor.execute("SELECT user_id FROM registrations WHERE game = ?", ("Moria",))
    user_ids = cursor.fetchall()

    mentions = []
    for row in user_ids:
        user_id = row[0]
        user = await bot.fetch_user(user_id)
        mentions.append(user.mention)

    if mentions:
        message = random.choice(moria_answers) + "\n" + " ".join(mentions)
    else:
        message = "Pas de nain autre que toi dans la liste... Courage, la Moria a besoin de toi ! 🏔"
    await interaction.response.send_message(message)

@bot.tree.command(name="démocratie", description="Ping les joueurs de Helldivers 2 🫡")
async def democratie(interaction: discord.Interaction):

    cursor.execute("SELECT user_id FROM registrations WHERE game = ?", ("Helldivers 2",))
    user_ids = cursor.fetchall()

    mentions = []
    for row in user_ids:
        user_id = row[0]
        user = await bot.fetch_user(user_id)
        mentions.append(user.mention)

    if mentions:
        message = random.choice(hd2_answers) + "\n" + " ".join(mentions)
    else:
        message = "Aucun soldat n'est encore inscrit ! La démocratie ne peut compter que sur toi. 🫡"
    await interaction.response.send_message(message)

@bot.tree.command(name="aoe", description="Ping les joueurs d'Age of Empires ⚔️")
async def aoe(interaction: discord.Interaction):

    cursor.execute("SELECT user_id FROM registrations WHERE game = ?", ("AoE",))
    user_ids = cursor.fetchall()

    mentions = []
    for row in user_ids:
        user_id = row[0]
        user = await bot.fetch_user(user_id)
        mentions.append(user.mention)

    if mentions:
        message = random.choice(aoe_answers) + "\n" + " ".join(mentions)
    else:
        message = "Il n'y a pas encore d'inscrit sur la liste d'Age of Empires. Déso Seb, il va falloir jouer solo. ⚔️"
    await interaction.response.send_message(message)

@bot.tree.command(name="liste", description="Liste des jeux auxquels un utilisateur est inscrit")
async def liste(interaction: discord.Interaction):
    cursor.execute("SELECT game FROM registrations WHERE user_id = ?", (interaction.user.id,))
    game = cursor.fetchall()
    game_names = [g[0] for g in game] # Fetch all game names for the user
    if game_names:
        message = (f"Voici les jeux auxquels tu es inscrit :" + "\n" + " ".join(game_names))
    else:
        message = "Tu n'es inscrit à aucun jeu. Pour le faire, rends-toi sur [ce message](https://discord.com/channels/1260548119926542417/1260591984985378940/1361274589992194128) et clique sur l'emoji correspondant au jeu auquel tu veux participer !"
    await interaction.response.send_message(message)

# @bot.event
# async def on_message(message):
    # print("Pong !")
    # Check if the message is from a bot
    # if message.author.bot:
        # return


bot.run(TOKEN)