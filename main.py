import json

import disnake
from disnake.ext import commands

file = open("config.json", "r")
config = json.load(file)

bot = commands.Bot(command_prefix=".", help_command=None, intents=disnake.Intents.all())

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


@bot.command()
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

bot.run(config["token"])
