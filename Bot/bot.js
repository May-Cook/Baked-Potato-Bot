const Discord = require('discord.js');
 const client = new Discord.Client();

client.on('ready', () => {
 console.log(`Logged in as ${client.user.tag}!`);
 });

client.on('message', msg => {
 if (msg.content === '!potato') {
 msg.reply('Wash you hands, don\'t touch your face');
 }
 });

client.login('Njk3MTI3NDE3NjMzOTY0MjIz.Xoy0Tw.LrU7ulHXSbx70rGL17CuFN8NOic');