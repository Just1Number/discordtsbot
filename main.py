# Work with Python 3.6
import discord
from os import environ
import time


TOKEN = environ['TOKEN']
REPORT = None

client = discord.Client()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await message.channel.send(msg)

    if message.content.startswith('!refresh'):
        global REPORT
        if REPORT == None:
            report = await message.channel.send(time.asctime(time.localtime(time.time())))
            REPORT = report
        else:
            await REPORT.edit(content=time.asctime(time.localtime(time.time())))


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)