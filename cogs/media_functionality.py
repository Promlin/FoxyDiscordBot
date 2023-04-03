import disnake
from disnake.ext import commands
from typing import Optional
from cogs.commands import CMDUsers


"""
Media functionality should include:
- playing the music
- playing the music from YouTube
- playing video from YouTube
"""

def setup():
    bot = commands.Bot(command_prefix=commands.when_mentioned, help_command=None, intents=disnake.Intents.all(),
                       test_guilds=[1067903829040955432])

    bot.add_cog(CMDUsers(bot))