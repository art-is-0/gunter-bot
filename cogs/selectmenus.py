from typing import Any, Coroutine
import discord
from discord.ext import commands
from discord import app_commands
from discord.interactions import Interaction

class ClassesMenu(discord.ui.Select):
    def __init__(self):
        options = [discord.SelectOption(label='MAT1100', description='Tar du MAT100', emoji='♾️'),
                   discord.SelectOption(label='FYS1100', description='Tar du FYS1100', emoji='🥏'),
                   discord.SelectOption(label='IN1900', description='Tar du IN1900', emoji='💻')]
        super().__init__(placeholder="Hvilken emner tar du?", options=options, min_values=1, max_values=3)

    async def callback(self, interaction:discord.Interaction):
        values = self.values
        for i in range(len(values)):
            match values[i]:
                case 'MAT1100':
                    role = interaction.guild.get_role(1146516169797419132)
                    await interaction.user.add_roles(role)
                    # await interaction.channel.send(content="MAT1100")
                    
                case 'FYS1100':
                    await interaction.channel.send(content="FYS1100")
                case 'IN1900':
                    await interaction.channel.send(content="IN1900")


class Classes(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.add_item(ClassesMenu())

class StudyMenu(discord.ui.Select):
    def __init__(self):
        options = [discord.SelectOption(label='FA', description='Om du studerer "Fysikk og Astronomi"', emoji='🌠'),
                   discord.SelectOption(label='ELITE', description='Om du studerer "Elektronikk, Infomatikk og Teknologi"', emoji='⚡'),
                   discord.SelectOption(label='NUKETECH', description='Om du studerer "Kjernefysikk og nukleærteknologi"', emoji='💥')]
        super().__init__(placeholder="Hvilken studie tar du?", options=options, min_values=1, max_values=1)

class Study(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.add_item(StudyMenu())

class selectmenus(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

    @app_commands.command(name='selectmenus', description='test')
    async def selectmenus(self, interaction:discord.Interaction):
        await interaction.response.send_message(view=Classes())

async def setup(client:commands.Bot) -> None:
    await client.add_cog(selectmenus(client))