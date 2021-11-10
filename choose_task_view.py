import json
from discord import ButtonStyle, PartialEmoji
from discord.ui import button, View, Button, select, Select
from discord.interactions import Interaction
from discord.ext import commands
from discord import SelectOption
import discord
import socket
from task_view import TasksView


class ChooseTasksView(View):
    def __init__(self, bot: discord.ext.commands.Bot, options_list: list[str, ...]):
        super().__init__(timeout=None)
        self.bot = bot
        self.selector = Select(custom_id='task_selector', placeholder='Choose task',
                               options=[SelectOption(label=option) for option in options_list])
        self.selector_difficulty = Select(custom_id='difficulty_selector', placeholder='Choose difficulty',
                                          options=[SelectOption(label=option) for option in ['easy', 'medium', 'hard']])
        self.add_item(self.selector)
        self.add_item(self.selector_difficulty)

    @button(label='Choose', custom_id='choose_task', style=ButtonStyle.green)
    async def choose_style(self, button_: Button, interaction: Interaction):
        request_json = json.dumps({
            "Theme": self.selector.values,
            "Flags": [],
            "Type": "task",
            "Difficulty": self.selector_difficulty.values
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
            "Type": "Task",
            "Name": "loops",
            "Task": "tell me why",
            "Difficulty": 0.1,
            "AnswerType": "few answer",
            "Answers": [
                "sadfsf",
                "sdkfsdlsdl",
                "dsik"
            ],
            "RightAnswers": [
                "dsik",
                "sadfsf"
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
            "DirectArticles": [
                "article"
            ]
        }
        main_embed = discord.Embed(title=json_data["Name"],
                                   description=f"Answer type: {json_data['AnswerType']}\n"
                                               f"Difficulty: {json_data['Difficulty']}\n"
                                               f"Task: {json_data['Task']}")
        await interaction.message.edit(embed=main_embed,
                                       view=TasksView(self.bot, json_data))
