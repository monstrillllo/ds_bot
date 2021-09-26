import discord

from oath_data import settings
from discord.ext import commands


def setup(bot):
    bot.add_cog(Admin_commands(bot))


class Admin_commands(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name="setstatus")
    @commands.is_owner()
    async def setstatus(self, ctx: commands.Context, *, text: str):
        """Sets the bot status to *text*"""
        await self.bot.change_presence(activity=discord.Game(name=text))
        await ctx.send('The status was set!')

    @commands.command(name='quit')
    @commands.is_owner()
    async def quit(self, ctx):
        await ctx.send('See you later!')
        await self.bot.close()
