import json
from choose_task_view import ChooseTasksView
from discord import ButtonStyle, PartialEmoji
from discord.ui import button, View, Button, select, Select
from discord.interactions import Interaction
from discord.ext import commands
from discord import SelectOption
import discord
import socket


class ThemesView(View):
    def __init__(self, bot: discord.ext.commands.Bot, options_list: list[str, ...]):
        super().__init__(timeout=None)
        self.bot = bot
        self.selector = Select(custom_id='themes_selector', placeholder='Choose theme',
                               options=[SelectOption(label=option) for option in options_list])
        self.add_item(self.selector)

    @button(label='Choose', custom_id='choose', style=ButtonStyle.green)
    async def choose_clicked(self, button_: Button, interaction: Interaction):
        request_json = json.dumps({
            "Theme": self.selector.values,
            "Flags": [],
            "Type": "article",
            "Difficulty": None
        })
        # with socket.socket() as sock:
        #     sock.connect(('192.168.43.68', 8888))
        #     sock.send(len(request_json).to_bytes(4, 'little', signed=True))
        #     sock.send(request_json.encode())
        #     data = sock.recv(1024).decode()
        #     sock.send(len(request_json).to_bytes(4, 'little', signed=True))
        #     sock.send(request_json.encode())
        #     data = sock.recv(1024).decode()
        #     json_data = json.loads(data)
        json_data = {
            "Type": "Article",
            "Name": "art",
            "Information": "This is article",
            "Difficulty": 0.1,
            "RelatedThemes": [
                "mytheme"
            ],
            "Links": [
                "url",
                "anotherurl"
            ],
            "Theme": [
                {
                    "Name": "Basic",
                    "Weight": 0.1
                },
                {
                    "Name": "something",
                    "Weight": 0.2
                }
            ],
            "DirectTasks": [
                "ifAny"
            ]
        }
        main_embed = discord.Embed(title=f'{json_data["Type"]}: {json_data["Name"]}',
                                   description=f"Information: {json_data['Information']}\n"
                                               f"Difficulty: {json_data['Difficulty']}")
        secondary_embed = discord.Embed(title='RelatedThemes',
                                        description='\n'.join(json_data['RelatedThemes']) if json_data[
                                            'RelatedThemes'] else 'No related themes available')
        secondary_embed2 = discord.Embed(title='Links',
                                         description='\n'.join(json_data['Links']) if json_data[
                                             'Links'] else 'No links available')
        await interaction.message.edit(embeds=[main_embed, secondary_embed, secondary_embed2],
                                       view=None)
