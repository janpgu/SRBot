# SRBot
A simple Python 3 bot for [Discord](https://discordapp.com/), which returns a list of skill rating values for a given list of [Overwatch](https://playoverwatch.com/en-us/) accounts. The bot utilizes the unofficial Overwatch [API](https://github.com/SunDwarf/OWAPI/blob/master/api.md) maintained by Laura F.D. aka SunDwarf.
## Example Usage
![Command and Response](https://i.imgur.com/mJG59kd.png)
## Getting Started
### Prerequisites
In order to use or build upon this bot, you'll need the following Python packages:
- requests
- discord

If you don't have those two packages already installed, get them through pip using the command
`pip3 install requests discord`. Additionally you will obviously need a Discord account and server.
### Deployment / Installation
1. Navigate to the following [link](https://discordapp.com/developers/applications/me)
2. Create a new app and set a name / title and a profile picture / app icon by hitting the "New App" button
3. After clicking on "Create App" hit the "Create a Bot User" button and confirm that you really want to add it
4. Ensure you remember the bot token and client ID you are given at this stage
5. Edit the SRBot.py file and enter your own bot token where it says `bot.run('SECRET TOKEN')`
6. Add your bot to a Discord server by inserting your client ID into the following link `https://discordapp.com/api/oauth2/authorize?client_id=CLIENT_ID_GOES_HERE&scope=bot&permissions=0` and open it in your browser.
## Acknowledgments
- How to code a discord bot with Python by [Coding with Python](https://writinginpython.wordpress.com/2017/04/01/how-to-code-a-discord-bot-with-python-part-1/)
- [Laura F.D](https://github.com/SunDwarf/OWAPI) aka SunDwarf
