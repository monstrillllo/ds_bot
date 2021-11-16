import json
from discord import ButtonStyle
from discord.ui import button, View, Button,Select
from discord.interactions import Interaction
from discord import SelectOption
import discord
from task_view import TasksView


class ThemesView(View):
    def __init__(self, bot, options_list: list[str, ...]):
        super().__init__(timeout=None)
        self.bot = bot
        self.selector = Select(custom_id='themes_selector', placeholder='Choose theme',
                               options=[SelectOption(label=option) for option in options_list],
                               max_values=len(options_list))
        self.selector_dif = Select(custom_id='dif_selector', placeholder='Choose dif',
                                   options=[SelectOption(label=str(option)) for option in range(1, 4)])
        self.add_item(self.selector)
        self.add_item(self.selector_dif)

    @button(label='Read', custom_id='read', style=ButtonStyle.green)
    async def choose_clicked(self, button_: Button, interaction: Interaction):
        request_json = json.dumps({
            "Theme": self.selector.values,
            "Flags": [],
            "Type": "Article",
            "Difficulty": int(self.selector_dif.values[0])
        })
        json_data = await self.bot.conn.send_request(request_json)

        embed = discord.Embed(title=json_data["Name"])
        embed.add_field(name="Information", value=json_data["Information"], inline=False)
        embed.add_field(name="Related Themes", value='\n'.join(json_data["RelatedThemes"]))
        embed.add_field(name="Difficulty", value=json_data["Difficulty"])
        embed.add_field(name="Links", value='\n'.join(json_data["Links"]), inline=False)
        await interaction.message.edit(embed=embed,
                                       view=None)

    @button(label='Do task', custom_id='task', style=ButtonStyle.green)
    async def tasks_clicked(self, button_: Button, interaction: Interaction):
        request_json = json.dumps({
            "Theme": self.selector.values,
            "Flags": [],
            "Type": "Task",
            "Difficulty": int(self.selector_dif.values[0])
        })
        json_data = await self.bot.conn.send_request(request_json)
        main_embed = discord.Embed(title=json_data["Name"])
        main_embed.add_field(name='Answer type', value=json_data['AnswerType'])
        main_embed.add_field(name='Difficulty', value=json_data['Difficulty'])
        main_embed.add_field(name='Task', value=json_data['Task'], inline=False)
        await interaction.message.edit(embed=main_embed,
                                       view=TasksView(self.bot, json_data))
