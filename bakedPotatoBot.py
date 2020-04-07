# bot.py
import os
import random

import discord
from dotenv import load_dotenv

# load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()


# adviceList = [
#     "Wash your hands and stay indoors"

    
# ]


@client.event # this is called a decorator
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message): 
    print(message.content)
    print(message.author)
    print(message)
    print("\n\n\n")

    if (message.content == "!potato"):
    
        await message.channel.send("Wash your hands, Don\'t touch your face.")


client.run("Njk3MTI3NDE3NjMzOTY0MjIz.Xozc1A.EdQL_bGry8JLApjOeFy6IKcLrwY")