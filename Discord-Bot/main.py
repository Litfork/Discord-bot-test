import discord
from discord.ext import commands
from config import settings

bot = commands.Bot(command_prefix = settings['prefix'], Intents=discord.Intents.all())
bot.remove_command("help")

@bot.event
async def on_ready():
    print('Бот включен')
    await bot.change_presence(activity=discord.Game(name=".help | .invite"))


bot.run(settings['token'])