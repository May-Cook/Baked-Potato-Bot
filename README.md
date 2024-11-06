# Baked Potato Bot
 :potato:A discord bot based on the song "Thank You Baked Potato" by Matt Lucas:potato:
 




## Instructions

### Add this bot to your server
Just follow this link: https://discord.com/api/oauth2/authorize?client_id=697127417633964223&permissions=3072&scope=bot

### Hosting your own bot using this repo
1. Create an environment variable called `DISCORD_TOKEN`, equal to your bot's token
2. Run bakedPotatoBot.py

#### Setting environment variables

###### Windows
1. Search for 'environment' in the windows search bar and open `Edit the system environment variables`
2. Under the `Advnaced` tab, click the button labelled `Environment Variables...` in the bottom right of the `System Properties` window 
3. Click the button labelled `new...` in the middle of the `Environment Variables` window to add a new user variable
4. Enter `DISCORD_TOKEN` in the box labelled `Variable name: `  and enter your bot's token in the box labelled `Variable value: `
5. Click the button labelled `OK` at the bottom of the window

###### Linux
Type `DISCORD_TOKEN = "yourToken"` into the console *(replcacing `yourToken` with your bot's token)*

if this does not work, you can try:
1. Open .bashrc in your preferred editor *(if you don't know how to do this you can use `sudo nano ~/.bashrc` to open it using nano)*
2. Add the line ```export DISCORD_TOKEN="yourToken"``` *(replacing `yourToken` with whatever your bot's token is)*
3. Save and exit the file *(if you are using nano you do this by pressing `CTRL-S` followed by `CTRL-X`)*

## Commands
* `!help` - Gives a list of options
* `!potato` - Gives a conventional potato response
* `!antitato` - Gives a reverse potato response
* `!contradictato` - Gives a conventional potato response, followed by the corresponding reverse potato response
* `!spell` - Reminds you how to spell "baked potato" 
* `!misspell` - Reminds you how to spell something vaguely similar to "baked potato "
* `!link` - Sends the link to the video
* `!serioustato` - Gives a very serious potato response
* `!cookedtuber` - Chooses a cooking method and a tuber and reminds you how to spell it

## Requirements
* Python3
* The `Discord.py` python module


## Links to the song

Original: https://www.youtube.com/watch?v=bPsY_nhTtxg

NHS Edition: https://www.youtube.com/watch?v=yYOkgCkxj9I

 ![An image of a cartoon potato next to Matt Lucas. Above them are the words "Thank you baked potato"](https://celebmix.com/wp-content/uploads/2020/04/BakedPotato.jpg)
