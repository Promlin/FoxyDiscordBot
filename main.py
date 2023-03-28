import os
import json
import disnake
from disnake.ext import commands

file = open("config.json", "r")
config = json.load(file)

bot = commands.Bot(command_prefix=commands.when_mentioned, help_command=None, intents=disnake.Intents.all(),
                   test_guilds=[1067903829040955432])

@bot.command()
@commands.is_owner()
async def load(ctx, extension):
    bot.load_extension(f"cogs.{extension}")

@bot.command()
@commands.is_owner()
async def unload(ctx, extension):
    bot.unload_extension(f"cogs.{extension}")

@bot.command()
@commands.is_owner()
async def reload(ctx, extension):
    bot.reload_extension(f"cogs.{extension}")

for filename in os.listdir("cogs"):
    if filename.endswith(".py"):
        bot.load_extension(f"cogs.{filename[:-3]}")

bot.run(config["token"])