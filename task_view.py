import json
from discord import ButtonStyle
from discord.ui import button, View, Button, Select
from discord.interactions import Interaction
from discord.ext import commands
from discord import SelectOption
import discord


class TasksView(View):
    def __init__(self, bot: discord.ext.commands.Bot, task_json: dict):
        super().__init__(timeout=None)
        self.bot = bot
        self.answers_list = task_json["Answers"]
        self.right_answers = task_json["RightAnswer"]
        self.name = task_json["Name"]
        self.direct_themes = task_json["Theme"]
        self.selector = Select(custom_id='answer_selector', placeholder='Choose answer',
                               options=[SelectOption(label=option) for option in self.answers_list])
        if task_json["AnswerType"] != 'one answer':
            self.selector.max_values = len(self.answers_list)
        self.add_item(self.selector)

    @button(label='Answer', custom_id='answer', style=ButtonStyle.green)
    async def answer_clicked(self, button_: Button, interaction: Interaction):
        embed = discord.Embed(title='Result')
        if sorted(self.selector.values) == sorted(self.right_answers):
            result = True
            embed.description = 'The answer was correct!'
        else:
            embed.description = 'The answer was incorrect!'
            if self.direct_themes:
                embed.add_field(name='Check those theme(s) before try again',
                                value='\n'.join([theme['Name'] for theme in self.direct_themes]))
            result = False
        request_json = json.dumps({
            "Type": "Answer",
            "Name": self.name,
            "Result": result,
            "UserID": interaction.message.author.id
        })
        await interaction.message.edit(embed=embed, view=None)

