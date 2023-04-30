import os 
import discord 
import openai
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
OPENAI_KEY = os.getenv('OPENAI_KEY')

openai.api_key = OPENAI_KEY



intents = discord.Intents.all()
client = discord.Client(command_prefix='!', intents=intents)


@client.event
async def on_ready():
    print('We logged in as {0.user}'.format(client))

 #test sending a message and receiving a message from the bot 
"""@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!hello bot'):
        await message.channel.send('Hii!')
 """



client.run(TOKEN)

