import disnake
from disnake.ext import commands
from typing import Optional

class Commands(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

# class Confirm(disnake.ui.View):
#     def __init__(self):
#         super().__init__(timeout=10.0)
#         self.value = Optional[bool]
#
#     @disnake.ui.button(label="Confirm", style=disnake.ButtonStyle.green, emoji="🎈", row=0)  # win + точка запятая
#     async def confirm(self, button: disnake.ui.Button, inter: disnake.CommandInteraction):
#         await inter.response.send_message("Кнопка нажата")
#         self.value = True
#         self.stop()
#
#     @disnake.ui.button(label="Cancel", style=disnake.ButtonStyle.red, emoji="🤞", row=0)
#     async def cancel(self, button: disnake.ui.Button, inter: disnake.CommandInteraction):
#         await inter.response.send_message("okey")
#         self.value = False
#         self.stop()
#
#
# class LinkToParty(disnake.ui.View):
#
#     def __init__(self):
#         super().__init__()
#         self.add_item(disnake.ui.Button(label="Join", url="https://habr.com/ru/post/649363/"))
#
#
#     @commands.command(name="party")
#     async def ask_party(ctx):
#         view = Confirm()
#
#         await ctx.send("Accept ar deny?", view=view)
#         await view.wait()
#
#         if view.value is None:
#             await ctx.send("Time run away")
#         elif view.value:
#             await ctx.send("Good", view=LinkToParty())
#         else:
#             await ctx.send("Bad")
#
#
#     # TODO подключить словарь
#     CENSORED_WORDS = ["one", "two"]  # слова для цензуры - можно подключить тектовый файл
#
#
#     @commands.event
#     async def on_ready(self):
#         print(f"Bot {commands.user} is ready to work!")
#         # here we could make status for bot - online - offline - sleeping
#
#
#     @commands.event  # задание роли при входе на канал
#     async def on_member_joint(member):
#         role = await disnake.utils.get(guild_id=member.guild.roles, id=1069708205145460807)
#         channel = member.guild.system_channel
#         # channel = bot.get_channel(id_from_discord) #Если нужен какой-то определенный канал
#
#         embed = disnake.Embed(  # Сообщение в красивой рамочке
#             title="Новый участник!",
#             description=f"{member.name}#{member.discriminator}",
#             color=0xfffff
#         )
#
#         await member.add_roles(role)
#         await channel.send(embed=embed)
#
#
#     @commands.event  # цензура
#     async def on_message(message):
#         await commands.process_commands(message)
#
#         for content in message.content.split():  # по умолчанию делит через пробелы
#             for cendored_words in CENSORED_WORDS:
#                 if content.lower() == cendored_words:
#                     await message.delete()
#                     await message.channel.send(f"{message.author.mention} такие слова запрещены!")
#
#
#     # Обработка ошибок
#     # TODO добавить примеры ошибок
#     @commands.event
#     async def on_command_error(ctx, error):
#         print(error)
#
#         if isinstance(error, commands.MissingPermissions):
#             await ctx.send(f"{ctx.author}, у вас недостаточно прав для выполнения данной команды")
#         elif isinstance(error, commands.UserInputError):
#             await ctx.send(embed=disnake.Embed(
#                 description=f"Правильное использование команды: '{ctx.prefix}{ctx.command.name}'({ctx.command.brief})\n"
#                             f"Пример: {ctx.prefix}{ctx.command.usage}"
#             ))
#
#
#     @commands.command(brief="Описание команды")
#     @commands.has_permissions(kick_members=True, administrator=True)
#     async def kick(ctx, member: disnake.Member, *, reason="Нарушение правил"):
#         await ctx.send(f"Администратор {ctx.author.mention} исключил пользователя {member.mention}")
#         await member.kick(reason=reason)
#         await ctx.message.delete()
#
#
#     @commands.command(name="бан", aliases=["слово для бана"])
#     @commands.has_permissions(ban_members=True, administrator=True)
#     async def ban(ctx, member: disnake.Member, *, reason="Нарушение правил"):
#         await ctx.send(f"Администратор {ctx.author.mention} забанил пользователя {member.mention}")
#         await member.ban(reason=reason)
#         await ctx.message.delete()
#
#
#     # TODO mute of the member
#     # Создаем роль - отнимаем у нее право говорить - создаем функию и выдаем роль



def setup(bot):
    bot.add_cog(Commands(bot))
