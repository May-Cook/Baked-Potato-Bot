# bot.py
import os
import random

import discord
# from dotenv import load_dotenv

# load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

newVerse = True

currenterse = None

adviceList = [
    ["Wash your hands and stay indoors.", "Only go to grocery stores."],
    ["Keep some distance, Make some space.", "Remember not to touch your face."],
    ["Do be good. Don\'t be bad.", "Do be happy. Don\'t be sad."],
    ["Do be early. Don\'t be late.", "Allways eat what\'s on your plate."],   
]


@client.event # this is called a decorator
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message): 
    global newVerse
    global currentVerse

    if (message.content == "!potato"):
        print(message.author)
        if (newVerse == True):
            currentVerse = random.choice(adviceList)
            await message.channel.send(currentVerse[0])
            newVerse = False
        else:
            await message.channel.send(currentVerse[1])
            newVerse = True



client.run("Njk3MTI3NDE3NjMzOTY0MjIz.Xozc1A.EdQL_bGry8JLApjOeFy6IKcLrwY")