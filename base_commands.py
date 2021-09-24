import random

from discord.ext import commands
import discord
from discord_components import DiscordComponents, Button, ButtonStyle, InteractionEventType, ComponentsBot


from oath_data import settings


def setup(bot):
    bot.add_cog(Base_commands(bot))


class Base_commands(commands.Cog):
    def __init__(self, bot: ComponentsBot):
        self.bot = bot
        self.menu_message_id = 0

    @commands.command(name="hello")
    async def hello(self, ctx: commands.Context):
        """Greets the user!"""
        author = ctx.message.author
        await ctx.send(f'hello, {author.mention}!')

    @commands.command(name="setstatus")
    async def setstatus(self, ctx: commands.Context, *, text: str):
        """Sets the bot status to *text*"""
        await self.bot.change_presence(activity=discord.Game(name=text))
        await ctx.send('The status was set!')

    @commands.command(name="roll")
    async def roll_the_dice(self, ctx: commands.Context, *, max_value=None):
        """Roll number between 1 and by default 6 or number that you type after command"""
        try:
            if max_value:
                await ctx.send(f"You rolled {random.randint(1, int(max_value))}")
            else:
                await ctx.send(f"You rolled {random.randint(1, 6)}")
        except:
            await ctx.send("Wrong argument!")

    @commands.command(name="menu")
    async def menu(self, ctx):
        await ctx.send("Say hi!", components=[Button(label="Button", custom_id="hi", id='123')])
        interaction = await self.bot.wait_for(
            "button_click", check=lambda i: i.custom_id == "hi" and i.id == '123'
        )
        print(interaction)
        await interaction.send(content="Button Clicked")

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
        for em in ["🖤", "💔", "💚", "💜"]:
            await message.add_reaction(em)

    @commands.Cog.listener()
    async def on_ready(self):
        # DiscordComponents(self.bot)
        print('All is ready!')
