import discord
from discord.ext import commands
from oath_data import settings
from connection import Connection


class MyBot(commands.Bot):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.conn = Connection()


intents = discord.Intents.default()
bot = MyBot(command_prefix=settings['prefix'], intents=intents, self_bot=False)
bot.load_extension("base_commands")
bot.load_extension('error_handler')
bot.load_extension('admin_commands')

if __name__ == '__main__':
    bot.run(settings['token'])
