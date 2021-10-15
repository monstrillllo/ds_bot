import json

from discord import ButtonStyle, PartialEmoji
from discord.ui import button, View, Button, select, Select
from discord.interactions import Interaction
from discord.ext import commands
from discord import SelectOption
import discord
import socket


class MenuView(View):
    def __init__(self, bot: discord.ext.commands.Bot):
        super().__init__(timeout=None)
        self.bot = bot
        self.selected_item = None

    @button(label='learn', custom_id='learn', style=ButtonStyle.green)
    async def button1_clicked(self, button_: Button, interaction: Interaction):
        channel = self.bot.get_channel(interaction.channel_id)
        request_json = json.dumps({
                          "Type": "Article",
                          "Name": "loops",
                          "Information": "",
                          "Theme": [
                            {
                              "Name": "Basic",
                              "Weight": 1
                            }
                          ],
                          "DirectsTasks": [
                            "loops_1"
                          ]
                        })
        try:
            with socket.socket() as sock:
                sock.connect(('192.168.43.68', 8888))
                sock.send(len(request_json).to_bytes(4, 'little', signed=True))
                sock.send(request_json.encode())
                data = sock.recv(1024).decode()
                sock.send(len(request_json).to_bytes(4, 'little', signed=True))
                sock.send(request_json.encode())
                data = sock.recv(1024).decode()
                json_data = json.loads(data)
                embed = discord.Embed(title=json_data['task']['name'], description=json_data['description'], colour=65535)
                await channel.send(embed=embed)
        except Exception as _ex:
            await channel.send(f'[+] Error: {_ex}')

    @button(label='testing', custom_id='testing', style=ButtonStyle.blurple)
    async def button2_clicked(self, button_: Button, interaction: Interaction):
        channel = self.bot.get_channel(interaction.channel_id)
        await channel.send(f'You press {button_.label}, but at this moment that do nothing!')

    @button(label='results', custom_id='results', style=ButtonStyle.red)
    async def button3_clicked(self, button_: Button, interaction: Interaction):
        channel = self.bot.get_channel(interaction.channel_id)
        await channel.send(f'You press {button_.label}, but at this moment that do nothing!')

    @button(label='select', custom_id='select', style=ButtonStyle.red)
    async def select_clicked(self, button_: Button, interaction: Interaction):
        if self.selected_item:
            channel = self.bot.get_channel(interaction.channel_id)
            await channel.send(f'You press {self.selected_item}, but at this moment that do nothing!')
        else:
            return

    @select(custom_id='test_select', options=[SelectOption(label='test1'), SelectOption(label='test3'), SelectOption(label='test2')])
    async def selector(self, select_: Select, interaction: Interaction):
        self.selected_item = select_.values[0]
