import json
import disnake
from disnake.ext import commands

# TODO добавить проигрывание музыки из YouTube
# TODO добавить библиотеку некоторых фраз (мотивация/анекдоты/прочее) и показывать рандомную при вызове команды
# TODO устанавливать напоминания и делать оповещения

file = open("config.json", "r")
config = json.load(file)

bot = commands.Bot(command_prefix=".", help_command=None, intents=disnake.Intents.all(),
                   test_guilds=[1067903829040955432])

# TODO подключить словарь
CENSORED_WORDS = ["one", "two"]  # слова для цензуры - можно подключить тектовый файл


@bot.event
async def on_ready():
    print(f"Bot {bot.user} is ready to work!")
    # here we could make status for bot - online - offline - sleeping


@bot.event  # задание роли при входе на канал
async def on_member_joint(member):
    role = await disnake.utils.get(guild_id=member.guild.roles, id=1069708205145460807)
    channel = member.guild.system_channel
    # channel = bot.get_channel(id_from_discord) #Если нужен какой-то определенный канал

    embed = disnake.Embed(  # Сообщение в красивой рамочке
        title="Новый участник!",
        description=f"{member.name}#{member.discriminator}",
        color=0xfffff
    )

    await member.add_roles(role)
    await channel.send(embed=embed)


@bot.event  # цензура
async def on_message(message):
    await bot.process_commands(message)

    for content in message.content.split():  # по умолчанию делит через пробелы
        for cendored_words in CENSORED_WORDS:
            if content.lower() == cendored_words:
                await message.delete()
                await message.channel.send(f"{message.author.mention} такие слова запрещены!")


# Обработка ошибок
# TODO добавить примеры ошибок
@bot.event()
async def on_command_error(ctx, error):
    print(error)

    if isinstance(error, commands.MissingPermissions):
        await ctx.send(f"{ctx.author}, у вас недостаточно прав для выполнения данной команды")
    elif isinstance(error, commands.UserInputError):
        await ctx.send(embed=disnake.Embed(
            description=f"Правильное использование команды: '{ctx.prefix}{ctx.command.name}'({ctx.command.brief})\n"
                        f"Пример: {ctx.prefix}{ctx.command.usage}"
        ))

@bot.command(brief="Описание команды")
@commands.has_permissions(kick_members=True, administrator=True)
async def kick(ctx, member: disnake.Member, *, reason="Нарушение правил"):
    await ctx.send(f"Администратор {ctx.author.mention} исключил пользователя {member.mention}")
    await member.kick(reason=reason)
    await ctx.message.delete()


@bot.command(name="бан", aliases=["слово для бана"])
@commands.has_permissions(ban_members=True, administrator=True)
async def ban(ctx, member: disnake.Member, *, reason="Нарушение правил"):
    await ctx.send(f"Администратор {ctx.author.mention} забанил пользователя {member.mention}")
    await member.ban(reason=reason)
    await ctx.message.delete()

# TODO mute of the member
# Создаем роль - отнимаем у нее право говорить - создаем функию и выдаем роль


# slash - command
@bot.slash_command(description="Калькулятор")
async def calc(inter, a: int, oper: str, b: int):
    if oper == "+":
        result = a + b
    elif oper == "-":
        result = a - b
    else:
        result = "Неверный оператор"

    await inter.send(str(result))


bot.run(config["token"])
