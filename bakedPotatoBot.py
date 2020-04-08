# bot.py
import os
import random

import discord

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
        if self.newVerse == True:
            self.currentVerse = random.choice(self.adviceList)
            self.newVerse = False
            return self.currentVerse[0]
        else:
            self.newVerse = True
            return self.currentVerse[1]

class Antitato(Potato):
    def __init__(self):
        super().__init__()
        self.adviceList = [
            ["Leave your hands, Don\'t stay indoors.", "Go to many different stores."],
            ["Keep no distance. Make no space.", "Remember you must touch your face."],
            ["Don\'t be good, Do be bad.", "Don\'t be happy. Do be sad."],
            ["Don\'t be early. Do be late.", "Never eat what\'s on your plate."]
        ]


class Contradictato(Potato):
    def __init__(self):
        super().__init__()
        self.adviceList = [
            ["Wash your hands and stay indoors.", "Leave your hands, Don\'t stay indoors."],
            ["Only go to grocery stores.", "Go to many different stores."],
            ["Keep some distance, Make some space.", "Keep no distance. Make no space"],
            ["Remember not to touch your face.", "Remember you must touch your face."],
            ["Do be good. Don\'t be bad.", "Don\'t be good, Do be bad."],
            ["Do be happy. Don\'t be sad.", "Don\'t be happy. Do be sad."],
            ["Do be early. Don\'t be late.", "Don\'t be early. Do be late."],
            ["Allways eat what\'s on your plate.", "Never eat what\'s on your plate."]      
        ]




potato = Potato()
antitato = Antitato()
contradictato = Contradictato()

@client.event # this is called a decorator
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message): 
    global potato, antitato

    if message.content == "!help":
        print(str(message.author) + ": !help")
        response = ""
        response += "!help - Gives a list of options\n"
        response += "!potato - Gives a conventional potato response\n"
        response += "!antitato - Gives a reverse potato response\n"
        response += "!contradictato - Gives a conventional potato response, followed by the corresponding reverse potato response\n"
        response += "!spell - Reminds you how to spell \"baked potato\" \n"
        response += "!misspell - Reminds you how to spell somthing vaguely simmilar to \"baked potato \""
        await message.channel.send(response)
    elif message.content == "!potato":
        print(str(message.author) + ": !potato")
        await message.channel.send(potato.getResponse())
    elif message.content == "!antitato":
        print(str(message.author) + ": !antitato")
        await message.channel.send(antitato.getResponse())
    elif message.content == "!contradictato":
        print(str(message.author) + ": !contradictato")
        await message.channel.send(contradictato.getResponse())
    elif message.content == "!spell":
        print(str(message.author) + ": !spell")
        await message.channel.send("**B**")
        await message.channel.send("**A**")      
        await message.channel.send("**K**")
        await message.channel.send("**E**")
        await message.channel.send("**D**")
        await message.channel.send("**P**") 
        await message.channel.send("**O**")
        await message.channel.send("**T**")
        await message.channel.send("**A**")
        await message.channel.send("**T**")
        await message.channel.send("**O**")
        await message.channel.send("Baked Potato")
    elif message.content == "!misspell":
        print(str(message.author) + ": !misspell")
        Alphabet = ["**A**", "**B**", "**C**", "**D**", "**E**", "**F**", "**G**", "**H**", "**I**", "**J**", "**K**", "**L**", "**M**", "**N**", "**O**", "**P**", "**Q**", "**R**", "**S**", "**T**", "**U**", "**V**", "**W**", "**X**", "**Y**", "**Z**"]
        lettersArray = ["**B**", "**A**", "**K**", "**E**", "**D**", "**P**", "**O**", "**T**", "**A**", "**T**", "**O**"]
        count = 0
        response = ""
        while count != len(lettersArray):
            rand = random.randint(0,5)
            if (rand == 4):
                letter = random.choice(Alphabet)
                response += letter[2]
                await message.channel.send(letter)
            elif rand == 3:
                count += 1
            else:
                letter = lettersArray[count]
                response += letter[2]
                await message.channel.send(letter)
                count += 1
        # response = response.lower()
        # firstLetter = response[0]
        # finalResponse = ""
        # for i in range(0, len(response)):
        #     if (i == 0):
        #         finalResponse += response[i]
        #     else:
        #         finalResponse += response[i].lower()
        await message.channel.send(response.title())


        
print(TOKEN)
client.run(TOKEN)