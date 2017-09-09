import discord
from discord.ext import commands
import requests # access the API
import time # sleep timer to avoid rate limit of API

# The OW API requires a custom user agent
headers = {
	'User-Agent': 'SRBot',
	'From': 'SRBot@gmail.com'
}

preLink = 'https://owapi.net/api/v3/u/'
postLink = '/stats'
srList = []
userList = [] # create empty list for easier adding of new accounts (see lines below)

# List of all OW account battletags where '#' has been replaced with '-' for easier API use
userList.append('Bronzo-11898')
userList.append('Zylbad-2592')
userList.append('Meow-22747')
userList.append('Thinking-21442')
userList.append('Bruh-11392')
userList.append('IronFist-12981')

# Instantiation of bot with '!s' as a prefix --> !sNAME_OF_COMMAND will trigger NAME_OF_COMMAND
bot = commands.Bot(command_prefix='!s', description='Returns a list of all SR values for all chosen accounts')

@bot.event # simple little message to notify you in the console once a connection to discord has been made
async def on_ready():
	print('Logged in as')
	print(bot.user.name)

# This is the 'r'-command, which will be executed if preceeded by the above prefix, so it triggers if we type !sr
@bot.command()
async def r():
	for eachUser in userList: # iterate over all battletags
		userLink = preLink + eachUser + postLink # create a custom url for every battletag
		r = requests.get(userLink, headers=headers) # access the API with custom url
		data = r.json() # decode the JSON response
		sr = data['eu']['stats']['competitive']['overall_stats']['comprank'] # extract SR (EU servers) from all statistics
		srList.append(sr)
		time.sleep(1) # sleep for one second to respect the rate limits of API
	await bot.say('####################################') # cosmetic spacer to distinguish from normal messages
	# Seperate loop so output is produced in quick succession and shows up as a single discord message block
	for i in range(len(userList)):
		outMsg = userList[i] + ' --- ' + str(srList[i])
		await bot.say(outMsg)
	await bot.say('####################################') # cosmetic spacer to distinguish from normal messages

bot.run('SECRET TOKEN')
