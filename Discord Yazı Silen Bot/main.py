import discord
from replit import db
from keep_alive import keep_alive

client = discord.Client()

@client.event
async def on_ready():
  print("Merhabalar {0.user}".format(client))

@client.event
async def on_message(message):
  if str(message.channel) == "konus" and message.content.startswith('-play'):
    await message.delete()

  if str(message.channel) == "konus" and message.content.startswith('-reset'):
    await message.delete()

  if str(message.channel) == "konus" and message.content.startswith('-stop'):
    await message.delete()  
  
  if str(message.channel) == "konus" and message.content.startswith('-shuffle'):
    await message.delete()
  
  if str(message.channel) == "konus" and message.content.startswith('-fastforward'):
    await message.delete()
  
  if str(message.channel) == "konus" and message.content.startswith('-start'):
    await message.delete()

  if str(message.channel) == "konus" and message.content.startswith('-next'):
    await message.delete()

  if str(message.channel) == "konus" and message.content.startswith('-loop'):
    await message.delete()

  if str(message.channel) == "konus" and message.content.startswith('-pause'):
    await message.delete()

  if str(message.channel) == "konus" and message.content.startswith('-resume'):
    await message.delete()

  if str(message.channel) == "konus" and message.author.bot:
    await message.delete()

  if message.author == client.user:
    return


#Your Discord Server Token has to be in client.run command
keep_alive()
client.run("")

