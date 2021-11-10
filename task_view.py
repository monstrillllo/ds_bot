import json
from discord import ButtonStyle, PartialEmoji
from discord.ui import button, View, Button, select, Select
from discord.interactions import Interaction
from discord.ext import commands
from discord import SelectOption
import discord
import socket


class TasksView(View):
    def __init__(self, bot: discord.ext.commands.Bot, task_json: dict):
        super().__init__(timeout=None)
        self.bot = bot
        self.answers_list = task_json["Answers"]
        self.right_answers = task_json["RightAnswers"]
        self.name = task_json["Name"]
        self.direct_articles = task_json["DirectArticles"]
        self.selector = Select(custom_id='answer_selector', placeholder='Choose answer',
                               options=[SelectOption(label=option) for option in self.answers_list])
        if task_json["AnswerType"] != 'one answer':
            self.selector.max_values = len(self.answers_list)
        self.add_item(self.selector)

    @button(label='Answer', custom_id='answer', style=ButtonStyle.green)
    async def answer_clicked(self, button_: Button, interaction: Interaction):
        if sorted(self.selector.values) == sorted(self.right_answers):
            result = True
            description = 'The answer was correct!'
        else:
            description = 'The answer was incorrect!\n'
            if self.direct_articles:
                description += 'Check those articles before try again:\n' + '\n'.join(self.direct_articles)
            result = False
        request_json = json.dumps({
            "Type": "Answer",
            "Name": self.name,
            "Result": result,
            "UserID": interaction.message.author.id
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
        embed = discord.Embed(title='Result', description=description)
        await interaction.message.edit(embed=embed, view=None)

