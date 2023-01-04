# bot.py
import os
import random
import string
import asyncio
import discord

TOKEN = os.getenv('DISCORD_TOKEN') # get the the bot's token from the corresponding environemnt variable

intents = discord.Intents.default() # initialise intents as having all but presences, members and message_content
intents.message_content = True # enable the message_content intent

client = discord.Client(intents=intents) # initialise the class representing the connection to discord


class Potato:
    def __init__(self, adviceList):
        self.adviceList = adviceList
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

potato = Potato([["Wash your hands and stay indoors.", "Only go to grocery stores."],
                ["Keep some distance, Make some space.", "Remember not to touch your face."],
                ["Do be good. Don\'t be bad.", "Do be happy. Don\'t be sad."],
                ["Do be early. Don\'t be late.", "Allways eat what\'s on your plate."]])

antitato = Potato([["Leave your hands, Don\'t stay indoors.", "Go to many different stores."],
                ["Keep no distance. Make no space.", "Remember you must touch your face."],
                ["Don\'t be good, Do be bad.", "Don\'t be happy. Do be sad."],
                ["Don\'t be early. Do be late.", "Never eat what\'s on your plate."]])

contradictato = Potato([["Wash your hands and stay indoors.", "Leave your hands, Don\'t stay indoors."],
                ["Only go to grocery stores.", "Go to many different stores."],
                ["Keep some distance, Make some space.", "Keep no distance. Make no space"],
                ["Remember not to touch your face.", "Remember you must touch your face."],
                ["Do be good. Don\'t be bad.", "Don\'t be good, Do be bad."],
                ["Do be happy. Don\'t be sad.", "Don\'t be happy. Do be sad."],
                ["Do be early. Don\'t be late.", "Don\'t be early. Do be late."],
                ["Allways eat what\'s on your plate.", "Never eat what\'s on your plate."]])

serioustato = Potato([["Wash your hands and stay indoors.", "**I mean it, Wash your hands and stay indoors!**"],
                ["Only go to grocery stores.", "**I mean it, Only go to grocery stores!**"],
                ["Keep some distance, Make some space.", "Or else I'll  punch you in the face"],
                ["Remember not to touch your face.", "Or else I'll launch you into space"],
                ["Do be good. Don\'t be bad.", "**I swear, you don't want to know what happens if you are bad!**"],
                ["Do be happy. Don\'t be sad.", "you don't want to know what happens if you don't cheer up"],
                ["Do be early. Don\'t be late.", "Or you may reach a terrible fate"],
                ["Allways eat what\'s on your plate.", "**Or I'll force feed you that food you hate!**"]]   )

@client.event # note to self: this is called a decorator
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
        response += "!misspell - Reminds you how to spell something vaguely simmilar to \"baked potato \"\n"
        response += "!link - Sends the link to the video\n"
        response += "!serioustato - Gives a very serious response"
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
        await letter_by_letter(message.channel, ["**B**", "**A**", "**K**", "**E**", "**D**", "**P**", "**O**", "**T**", "**A**", "**T**", "**O**"])
        await message.channel.send("Baked Potato")
    elif message.content == "!misspell":
        print(str(message.author) + ": !misspell")
        alphabet = [f"**{letter}**" for letter in string.ascii_uppercase]
        potato_letters = ["**B**", "**A**", "**K**", "**E**", "**D**", "**P**", "**O**", "**T**", "**A**", "**T**", "**O**"]
        count = 0
        response = []
        while count < len(potato_letters) :
            rand = random.randint(0,10)
            if (rand == 4): # add a random letter before the one pointed to by count
                response += [random.choice(alphabet)]
            elif rand == 3: # skip the letter pointed to by count
                count += 1
            else: # add the correct letter to the word
                response += [potato_letters[count]]
                count += 1
        await letter_by_letter(message.channel, response)
        await message.channel.send("".join(response).replace("*", "").title())
    elif message.content == "!link":
        print(str(message.author) + ": !link")
        await message.channel.send("https://www.youtube.com/watch?v=yYOkgCkxj9I")
    elif message.content == "!serioustato":
        print(str(message.author) + ": !serioustato")
        await message.channel.send(serioustato.getResponse())


async def letter_by_letter(channel, content): # spells out the string in content by editing a sent message
    message = await channel.send(content[0]) # send a message containing the first letter
    for letter in content[1:]:
        await asyncio.sleep(0.8)
        message = await message.edit(content=message.content + " " + letter) # edit the message to include the next letter
    return message
    


        
# print("Your token is: ", TOKEN)
client.run(TOKEN) # start the bot