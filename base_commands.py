import random
from discord.ext import commands
import discord
from menu_view import MenuView
from emojis import EMOJI_UNICODE_ENGLISH
from re import search, IGNORECASE


def setup(bot):
    bot.add_cog(Base_commands(bot))


class Base_commands(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.last_5_deleted_msg = []
        self.menu_message_id = 0

    @commands.command(name="hello")
    async def hello(self, ctx: commands.Context):
        """Greets the user!"""
        author = ctx.message.author
        await ctx.send(f'hello, {author.mention}!')

    @commands.command(name="roll")
    async def roll_the_dice(self, ctx: commands.Context, *, max_value=None):
        """Roll number between 1 and by default 6 or number that you type after command"""
        if max_value:
            if max_value.isdigit():
                await ctx.reply(f"You rolled {random.randint(1, int(max_value))}")
            else:
                raise commands.UserInputError
        else:
            await ctx.reply(f"You rolled {random.randint(1, 6)}")

    @commands.command(name="menu")
    async def menu(self, ctx: commands.Context):
        """Show learning menu"""
        embed = discord.Embed(title='Menu', description='Choose what you want to do.', colour=65535)
        await ctx.send(embed=embed, view=MenuView(self.bot))

    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        try:
            if search('COCK', message.content, flags=IGNORECASE) and message.author.id != 766005466136313877:
                await message.channel.send('https://tenor.com/view/didsomeonesaycock-didsomeonesay-yep-pepe-yeppers-gif-19924664')
            await message.add_reaction(random.choice(list(EMOJI_UNICODE_ENGLISH.values())))
        except Exception:
            pass

    @commands.Cog.listener()
    async def on_ready(self):
        print('All is ready!')
