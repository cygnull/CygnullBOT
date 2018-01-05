# These are the dependecies. The bot depends on these to function, hence the name. Please do not change these unless your adding to them, because they can break the bot.
import discord
import asyncio
from discord.ext.commands import Bot
from discord.ext import commands
import platform

# Here you can modify the bot's prefix and description and wether it sends help in direct messages or not.
client = Bot(description="Cygnull A.I. Discord Bot ver. 0.1a", command_prefix=">", pm_help = True)

# This is what happens everytime the bot launches. In this case, it prints information like server count, user count the bot is connected to, and the bot id in the console.
# Do not mess with it because the bot can break, if you wish to do so, please consult me or someone trusted.
@client.event
async def on_ready():
	print('Logged in as '+client.user.name+' (ID:'+client.user.id+') | Connected to '+str(len(client.servers))+' servers | Connected to '+str(len(set(client.get_all_members())))+' users')
	print('-=-=-=-=-')
	print('Current Discord.py Version: {} | Current Python Version: {}'.format(discord.__version__, platform.python_version()))
	print('-=-=-=-=-')
	print('Use this link to invite {}:'.format(client.user.name))
	print('https://discordapp.com/oauth2/authorize?client_id={}&scope=bot&permissions=8'.format(client.user.id))
	print('-=-=-=-=-')
	print('Support Discord Server: https://discord.gg/hyGa7J2')
	print('Github Link: https://github.com/cygnull/CygnullBOT')
	print('-=-=-=-=-')
	print('Created by Cygnull')

# This is a basic example of a call and response command. You tell it do "this" and it does it.
@client.command()
async def testing(*args):

	await client.say(":test_me: Test is working!")
	await asyncio.sleep(3)
	await client.say(":warning: This bot was created by **Cygnull#1348**, Updates pushed to GitHub regularly!")
# After you have modified the code, feel free to delete the line above (line 33) so it does not keep popping up everytime you initiate the ping commmand.
	
client.run('Mzk2MDM0NTYwNDc2ODM5OTM4.DSbjpw.XP-NWs5z5WC0BnPySt2Zuc_XTEA')

# Cygnull A.I. Discord Bot was created by Cygnull#1348 
# Please join this Discord server if you have any suggestions, comments, need help, or want to help out and become a Developer: https://discord.gg/hyGa7J2
# Comments will be added as much as possible to help discern and explain code.
#
# # The help command is currently set to be Direct Messaged.
# If you would like to change that, change "pm_help = True" to "pm_help = False" on line 9.