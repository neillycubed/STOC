import sys, os
import discord
import json
import asyncio
from discord.ext import commands
config_file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'config.json')

class Tty(commands.Cog):
    
    def __init__(self, client):
        self.client = client

    #Events
    @commands.Cog.listener()
    async def on_message(self, message):
        if (message.author != self.client.user):
            with open(config_file_path) as json_data_file:
                conf = json.load(json_data_file)
                json_data_file.close()
            if conf["channel"] and (message.channel.id == conf["channel"]):
                channel = message.guild.get_channel(conf["channel"])
                msgs = await channel.history(limit=100).flatten()
                await Tty.check_console(self=self, channel=channel)
                await Tty.input_console(self=self, channel=channel, input=message.content)
                for msg in msgs:
                    if len(msg.embeds) <= 0:
                        await msg.delete()

    #Commands
    @commands.command()
    async def tty(self, ctx):
        ttyEmbed = discord.Embed(color=0x00ff00)
        ttyEmbed.set_thumbnail(url='https://i.imgur.com/jP9BH6f.png')
        ttyEmbed.add_field(name="STOC CONSOLE", value="ㅤ", inline=False)
        ttyEmbed.add_field(name="INPUT", value="```                             ```", inline=False)
        ttyEmbed.add_field(name="ㅤ", value="**ㅤ                                     **", inline=False)
        ttyEmbed.add_field(name="OUTPUT", value="```                                ```", inline=False)
        ttyEmbed.set_footer(text="STOC v0.1.0", icon_url='https://i.imgur.com/jP9BH6f.png')
        await ctx.send(embed=ttyEmbed)

    @commands.command()
    async def set_tty(self, ctx):
        Tty.spawn_tty(self=self, channel=ctx.channel)
        
    #Methods
    async def check_console(self, channel):
        msgs = await channel.history().flatten()
        for msg in msgs:
            if len(msg.embeds) <=0:
                pass

    async def input_console(self, channel, input):
        msgs = await channel.history().flatten()
        for msg in msgs:
            if len(msg.embeds) <= 0:
                pass
            else:
                pass
                
    

    async def spawn_tty(self, channel):
        msgs = await channel.history().flatten()
        for msg in msgs:
            if len(msg.embeds) <= 0:
                print(msg.embeds)
            else:
                return 0
            ttyEmbed = discord.Embed(color=0x00ff00)
            ttyEmbed.set_thumbnail(url='https://i.imgur.com/jP9BH6f.png')
            ttyEmbed.add_field(name="ㅤ", value=f"Tty Console set successfully in \{channel.name}", inline=False)
            ttyEmbed.set_footer(text="STOC v0.1.0", icon_url='https://i.imgur.com/jP9BH6f.png')
            await channel.send(embed=ttyEmbed)
            with open(config_file_path) as json_data_file:
                conf = json.load(json_data_file)
                json_data_file.close()
            conf["channel"] = channel.id
            with open(config_file_path, "w") as json_data_file:
                json.dump(conf, json_data_file)
                json_data_file.close()
            return 1
        

def setup(client):
    client.add_cog(Tty(client))