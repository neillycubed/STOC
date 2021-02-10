import os
import discord
import logging
from discord.ext import commands
import config

conf = config.load_config()

client = commands.Bot(command_prefix = conf["prefix"])

@client.command()
async def reload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')
    print(f'{extension} reloaded successfully!')

@client.event
async def on_ready():
    print(f'STOC v{conf["version"]} loaded successfully!')

client.run(conf["token"])