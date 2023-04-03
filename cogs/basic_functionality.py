import disnake
from typing import Optional

from cogs.commands import CMDUsers
from disnake.ext import commands

"""
Basic functionality should include:
- greetings new members (embed)
- kick member
- ban member
- give the role
- mute member
- transfer member from one voice channel to another
- return message with the help (explaining the bot functionality)
"""

class CMDUsers(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

def setup(bot):
    bot.add_cog(CMDUsers(bot))
