import random
from discord.ui import button, View, Button
from discord.interactions import Interaction
from discord.ext import commands
import discord
from button_view import Menu_view
# from discord import Button
# from discord_components import DiscordComponents, Button, ButtonStyle, InteractionEventType, ComponentsBot


from oath_data import settings


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
            if type(max_value) == 'int':
                await ctx.send(f"You rolled {random.randint(1, int(max_value))}")
            else:
                raise commands.UserInputError
        else:
            await ctx.send(f"You rolled {random.randint(1, 6)}")

    @commands.command(name="menu")
    async def menu(self, ctx: commands.Context):
        embed = discord.Embed(title='Menu', description='Choose what you want to do.', colour=65535)
        await ctx.send(embed=embed, view=Menu_view(self.bot))

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        if payload.message_id == self.menu_message_id and payload.user_id != settings['id']:
            channel = self.bot.get_channel(payload.channel_id)
            if not channel:
                return
            await channel.send(f"You add {payload.emoji} to message!")

    @commands.Cog.listener()
    async def on_member_remove(self, member: discord.Member):
        channel = self.bot.get_channel(766010486969204748)
        if not channel:
            return
        await channel.send(f"Покеда, {member}!")

    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member):
        channel = self.bot.get_channel(766010486969204748)
        if not channel:
            return
        await channel.send(f"Welcome, {member}!")
        # print(member.guild.roles)
        role = None
        for r in member.guild.roles:
            if r.name == 'clown':
                role = r
                break
        await member.add_roles(role)

    @commands.Cog.listener()
    async def on_message(self, message):
        await message.add_reaction(random.choice(["🖤", "💔", "💚", "💜"]))

    @commands.Cog.listener()
    async def on_raw_bulk_message_delete(self, message):
        print(message)
        if len(self.last_5_deleted_msg) == 5:
            self.last_5_deleted_msg.pop(0)
        self.last_5_deleted_msg.append(message)

    @commands.Cog.listener()
    async def on_ready(self):
        print('All is ready!')
