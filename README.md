# SRBot
A simple Python 3 bot for [Discord](https://discordapp.com/), which returns a list of skill rating values for a given list of [Overwatch](https://playoverwatch.com/en-us/) accounts. The bot utilizes the unofficial Overwatch [API](https://github.com/SunDwarf/OWAPI/blob/master/api.md) maintained by SunDwarf.
## Example Usage
![Command and Response](https://i.imgur.com/mJG59kd.png)
## Getting Started
### Prerequisites
In order to use or build upon this bot, you'll need the following Python packages:
- requests
- discord

If you don't have those already install them through pip using the command
`pip3 install requests discord`. Additionally you will obviously need a Discord account.
### Deployment / Installation
1. Navigate to the following [link](https://discordapp.com/developers/applications/me)
2. Create a new app and set a name / title and a profile picture / app icon by hitting the "New App" button
3. After clicking on "Create App" hit the "Create a Bot User" button and confirm that you really want to add it
4. Edit the SRBot.py file and enter your own bot token where it says `bot.run('')`
