import json
from discord import ButtonStyle
from discord.ui import button, View, Button
from discord.interactions import Interaction
import discord
from choose_theme_view import ThemesView


class MenuView(View):
    def __init__(self, bot):
        super().__init__(timeout=None)
        self.bot = bot
        self.selected_item = None

    @button(label='Themes', custom_id='themes', style=ButtonStyle.green)
    async def articles_clicked(self, button_: Button, interaction: Interaction):
        request_json = json.dumps({
                                      "Theme": [],
                                      "Flags": [],
                                      "Type": "Article",
                                      "Difficulty": None
                                    })
        json_data = await self.bot.conn.send_request(request_json)
        themes = '\n'.join(json_data)
        embed = discord.Embed(title='Available themes', description=themes, colour=65535)
        await interaction.message.edit(embed=embed, view=ThemesView(self.bot, json_data))
