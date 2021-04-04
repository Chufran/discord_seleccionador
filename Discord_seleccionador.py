# bot.py
import os
import random

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()
def get_channel_by_name(name,server):
    for server in client.guilds:
        for text_channel in server.text_channels:
            if text_channel.name == "general":
                    channel = text_channel
    return channel
def custom_message():
    message_list=["chufran","didi","jesus","sarasa","papa noel"]
    return random.choice(message_list)
@client.event
async def on_ready():
	channel = get_channel_by_name("general",client)
	
	await channel.send('Prendio el bot')
@client.event
async def on_message(message):
    channel = message.channel
    message_to_send={
    'ZU': ["chufran","didi","jesus","sarasa","papa noel"],
    'QH': ["judas","aseda","teclado","razer","aguante el cs"]
    }.get(str(message.content))
    if message_to_send:
        await channel.send(random.choice(message_to_send))
        msg = await client.wait_for('message')
client.run(TOKEN)