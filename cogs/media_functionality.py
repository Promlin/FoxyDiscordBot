import disnake
from disnake.ext import commands
from typing import Optional


"""
Media functionality should include:
- playing the music
- playing the music from YouTube
- playing video from YouTube
"""

class MediaFunctionality(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

def setup(bot):
    bot.add_cog(MediaFunctionality(bot))