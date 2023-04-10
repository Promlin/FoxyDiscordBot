import disnake
from typing import Optional

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

class BasicFunctionality(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(brief="Kick someone")
    @commands.has_permissions(kick_members=True, administrator=True)
    async def kick(self, ctx, member: disnake.Member, *, reason="Нарушение правил"):
        await ctx.send(f"Администратор {ctx.author.mention} исключил пользователя {member.mention}")
        await member.kick(reason=reason)
        await ctx.message.delete()

    @commands.command(name="Ban", aliases=["Word for ban"])
    @commands.has_permissions(ban_members=True, administrator=True)
    async def ban(self, ctx, member: disnake.Member, *, reason="Нарушение правил"):
        await ctx.send(f"Администратор {ctx.author.mention} забанил пользователя {member.mention}")
        await member.ban(reason=reason)
        await ctx.message.delete()

    @commands.command(name="Unban", aliases=["Word for unban"])
    @commands.has_permissions(ban_members=True, administrator=True)
    async def unban(self, ctx, member: disnake.Member):
        await ctx.send(f"Администратор {ctx.author.mention} забанил пользователя {member.mention}")
        await member.unban()
        await ctx.message.delete()

def setup(bot):
    bot.add_cog(BasicFunctionality(bot))
