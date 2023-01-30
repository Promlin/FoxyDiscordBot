import disnake
from disnake.ext import commands

bot = commands.Bot(command_prefix=".", help_command=None, intents=disnake.Intents.all())

CENSORED_WORDS = ["one", "two"] #слова для цензуры - можно подключить тектовый файл

@bot.event
async def on_ready():
    print(f"Bot {bot.user} is ready to work!")
    # here we could make status for bot - online - offline - sleeping


@bot.event #задание роли при входе на канал
async def on_member_joint(member):
        role = await disnake.utils.get(guild_id=member.guild.id, role_id=1069708205145460807)
        channel = member.guild.system_channel
        #channel = bot.get_channel(id_from_discord) #Если нужен какой-то определенный канал

        embed = disnake.Embed( #Сообщение в красивой рамочке
            title="Новый участник!",
            description=f"{member.name}#{member.discriminator}",
            color=0xfffff
        )

        await member.add_roles(role)
        await channel.send(embed=embed)


@bot.event #цензура
async def on_message(message):
    for content in message.content.split(): #по умолчанию делит через пробелы
        for cendored_words in CENSORED_WORDS:
            if content == cendored_words:
                await message.delete()
                await message.channel.send(f"{message.author.mention} такие слова запрещены!")


bot.run("MTA2Nzg5OTEyMjEwMDc0ODMxOA.Ga3No2.iw5krY7bKIlQVCKlGPt_bc1ZjzudV0dEPvA5hg")
