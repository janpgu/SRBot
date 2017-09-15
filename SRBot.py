"""Simple Discord bot, which returns a list of skill rating values for a given list of Overwatch accounts."""

import time  # Sleep timer to avoid rate limit of API
from discord.ext import commands
import requests  # Access the API

# The OW API requires a custom user agent
headers = {
    'User-Agent': 'SRBot',
    'From': 'SRBot@gmail.com'
}

preLink = 'https://owapi.net/api/v3/u/'
postLink = '/stats'
srList = []
# List of all OW account battletags where '#' has been replaced with '-' for easier API use
userList = ['BATTLETAG-123',
            'BATTLETAG-123',
            'BATTLETAG-123']

# Instantiation of bot with '!s' as a prefix --> !sNAME_OF_COMMAND will trigger NAME_OF_COMMAND
bot = commands.Bot(command_prefix='!s', description='Returns a list of all SR values for all chosen accounts')


@bot.event
async def on_ready():
    """Simple little message to notify you in the console once a connection to discord has been made"""
    print('Logged in as')
    print(bot.user.name)


@bot.command()
async def r():
    """This is the 'r'-command, which will be executed if preceded by the above prefix, so it triggers if we type !sr"""
    for eachUser in userList:  # Iterate over all battletags
        userLink = preLink + eachUser + postLink  # Create a custom url for every battletag
        req = requests.get(userLink, headers=headers)  # Access the API with custom url
        data = req.json()  # Decode the JSON response
        sr = data['eu']['stats']['competitive']['overall_stats']['comprank']  # Extract SR (EU servers) from all statistics
        srList.append(sr)
        time.sleep(1)  # Sleep for one second to respect the rate limits of API
    await bot.say('####################################')  # Cosmetic spacer to distinguish from normal messages
    # Separate loop so output is produced in quick succession and shows up as a single discord message block
    for idx, _ in enumerate(userList):
        outMsg = userList[idx] + ' --- ' + str(srList[idx])
        await bot.say(outMsg)
    await bot.say('####################################')  # Cosmetic spacer to distinguish from normal messages

bot.run('SECRET TOKEN')
