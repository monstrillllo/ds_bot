import discord
from discord.ext import commands
from oath_data import settings

intents = discord.Intents.default()
# intents.members = True
bot = commands.Bot(command_prefix=settings['prefix'], intents=intents, self_bot=False)
# bot = ComponentsBot(command_prefix=settings['prefix'], intents=intents)
bot.load_extension("base_commands")
bot.load_extension('error_handler')
bot.load_extension('admin_commands')


if __name__ == '__main__':
    bot.run(settings['token'])
