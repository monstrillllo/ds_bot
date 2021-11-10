from discord import ButtonStyle
from discord.ui import button, View, Button
from discord.interactions import Interaction
from discord.ext import commands
import discord
import socket
from choose_theme_view import ThemesView
from choose_task_view import ChooseTasksView


json_data = {
    "themes": [
        "one",
        "two"
    ]
}

json_data_tasks = {
    "tasks": [
        "taskone",
        "tasktwo"
    ]
}


class MenuView(View):
    def __init__(self, bot: discord.ext.commands.Bot):
        super().__init__(timeout=None)
        self.bot = bot
        self.selected_item = None

    @button(label='Articles', custom_id='articles', style=ButtonStyle.green)
    async def articles_clicked(self, button_: Button, interaction: Interaction):
        # channel = self.bot.get_channel(interaction.channel_id)
        # request_json = json.dumps({
        #                               "Theme": [],
        #                               "Flags": [],
        #                               "Type": "article",
        #                               "Difficulty": None
        #                             })
        # with socket.socket() as sock:
        #     sock.connect(('192.168.43.68', 8888))
        #     sock.send(len(request_json).to_bytes(4, 'little', signed=True))
        #     sock.send(request_json.encode())
        #     data = sock.recv(1024).decode()
        #     sock.send(len(request_json).to_bytes(4, 'little', signed=True))
        #     sock.send(request_json.encode())
        #     data = sock.recv(1024).decode()
        #     json_data = json.loads(data)
        themes = '\n'.join(json_data['themes'])
        embed = discord.Embed(title='Available themes', description=themes, colour=65535)
        await interaction.message.edit(embed=embed, view=ThemesView(self.bot, json_data['themes']))

    @button(label='Tasks', custom_id='tasks', style=ButtonStyle.green)
    async def tasks_clicked(self, button_: Button, interaction: Interaction):
        # channel = self.bot.get_channel(interaction.channel_id)
        # request_json = json.dumps({
        #                               "Theme": [],
        #                               "Flags": [],
        #                               "Type": "article",
        #                               "Difficulty": None
        #                             })
        # with socket.socket() as sock:
        #     sock.connect(('192.168.43.68', 8888))
        #     sock.send(len(request_json).to_bytes(4, 'little', signed=True))
        #     sock.send(request_json.encode())
        #     data = sock.recv(1024).decode()
        #     sock.send(len(request_json).to_bytes(4, 'little', signed=True))
        #     sock.send(request_json.encode())
        #     data = sock.recv(1024).decode()
        #     json_data = json.loads(data)
        tasks = '\n'.join(json_data_tasks['tasks'])
        embed = discord.Embed(title='Available tasks', description=tasks, colour=65535)
        await interaction.message.edit(embed=embed, view=ChooseTasksView(self.bot, json_data['themes']))

