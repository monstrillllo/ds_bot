import discord
from discord.ext import commands
from oath_data import settings
import json
from base_commands import Base_commands

intents = discord.Intents.default()
intents.members = True


bot = commands.Bot(command_prefix=settings['prefix'], intents=intents)
bot.load_extension("base_commands")


# @bot.command(name="help")
# async def help_com(ctx):
#     await ctx.send('At this moment i cant do anything but say hello!')


if __name__ == '__main__':
    bot.run(settings['token'])
