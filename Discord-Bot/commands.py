import discord
from discord.ext import commands
from config import settings

bot = commands.Bot(command_prefix = settings['prefix'], Intents=discord.Intents.all())

@bot.command() 
async def one(ctx): 
    author = ctx.message.author 
    await ctx.send(f'Тіла, які тривалий час зберігають магнітні властивості, називають постійними магнітами.')





