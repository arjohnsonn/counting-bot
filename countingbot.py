import discord
from discord.ext.commands import Bot
from discord.ext import commands
import time

client = discord.Client()
bot = commands.Bot(command_prefix="")


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.channel.id != 622998981915574283:
        return

    if message.content.startswith("~start"):
        await counter(10000000000000000, message)

    if message.content == "~stop":
        await message.channel.send("Stopped!")
        await client.logout()

async def counter(max, message):
    count = 303005
    while count != 10000000000000000:
        await message.channel.send(str(count))
        time.sleep(1)
        count = count+1

client.run('NjIyOTgxNTg1NTI4MDI5MTg3.XX7y4g.wJGLZWuaZvCNrMyF2YPaO5gdWVw')
