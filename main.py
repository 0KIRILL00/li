import random
import discord

from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True


bot = commands.Bot(command_prefix='$', intents=intents)

def gen_pass(pass_length):
    elements = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    password = ""
    for i in range(pass_length):
        password += random.choice(elements)
    return password

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Привет! Я бот {bot.user}!')

@bot.command()
async def bye(ctx):
    await ctx.send(f'Пока!')


@bot.command()
async def pasw(ctx, count=8):
    await ctx.send(f'Ваш пароль - {gen_pass(count)}')

@bot.command()
async def add(ctx, left: int, right: int):
    await ctx.send(left + right)

@bot.command()
async def repeat(ctx, times: int, content='повторение...'):
    for i in range(times):
        await ctx.send(content)
bot.run('')
