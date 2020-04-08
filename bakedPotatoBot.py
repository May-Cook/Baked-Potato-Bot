# bot.py
import os
import random

import discord
# from dotenv import load_dotenv

# load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()


class Potato:
    def __init__(self):
        self.adviceList = [
            ["Wash your hands and stay indoors.", "Only go to grocery stores."],
            ["Keep some distance, Make some space.", "Remember not to touch your face."],
            ["Do be good. Don\'t be bad.", "Do be happy. Don\'t be sad."],
            ["Do be early. Don\'t be late.", "Allways eat what\'s on your plate."],   
        ]
        self.newVerse = True
        self.currentVerse = None

    def getResponse(self):
        if (self.newVerse == True):
            self.currentVerse = random.choice(self.adviceList)
            self.newVerse = False
            return self.currentVerse[0]
        else:
            self.newVerse = True
            return self.currentVerse[1]






potato = Potato()

@client.event # this is called a decorator
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message): 
    global potato

    if (message.content == "!potato"):
        print(str(message.author) + ": !potato")
        await message.channel.send(potato.getResponse())


client.run("Njk3MTI3NDE3NjMzOTY0MjIz.Xozc1A.EdQL_bGry8JLApjOeFy6IKcLrwY")