import disnake
from disnake.ext import commands

"""
I'm going to create such functions:
- I need to come up with some ideas 
- Instruction
-
"""


class SlashCommands(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(description="Калькулятор")
    async def calc(self, inter: disnake.ApplicationCommandInteraction, a: int, oper: str, b: int):
        if oper == "+":
            result = a + b
        elif oper == "-":
            result = a - b
        elif oper == "*":
            result = a * b
        elif oper == "/":
            if b == 0:
                b = 1
                await inter.send(str("Ошибка деления на ноль!"))
            result = a / b
        else:
            result = "Неверный оператор"

        await inter.send(str(result))


def setup(bot):
    bot.add_cog(SlashCommands(bot))
