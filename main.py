import discord
from discord.ext import commands
from discord_components import ComponentsBot

from oath_data import settings

intents = discord.Intents.default()
intents.members = True
# bot = commands.Bot(command_prefix=settings['prefix'], intents=intents)
bot = ComponentsBot(command_prefix=settings['prefix'], intents=intents)
bot.load_extension("base_commands")
bot.load_extension('error_handler')


if __name__ == '__main__':
    bot.run(settings['token'])
