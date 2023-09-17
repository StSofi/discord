import discord, random
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

orlreshk = ['ОРЁЛ', 'РЕШКА']

def gen_pass(pass_length):
    elements = "+-/*!&$#?=@<>1234567890qwertyuiopasdfghjklzxcvbnm"
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
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def rnd(ctx, left: int, right: int):
    await ctx.send(random.randint(left, right))

@bot.command()
async def orlre(ctx):
    await ctx.send(random.choice(orlreshk))

@bot.command()
async def pas(ctx):
    await ctx.channel.send(gen_pass(10))

@bot.command()
async def add(ctx, left: int, right: int):
    await ctx.send(left + right)


   

bot.run("////////////////////////////")
