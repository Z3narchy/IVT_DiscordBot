import random
import os
import requests
import discord
from dotenv import load_dotenv
from discord.ext import commands

#Load .env
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

#Setup Bot
bot = commands.Bot(command_prefix='!')

@bot.command(name='99')
async def nine_nine(ctx):
    brooklyn_99_quotes = [
        'I\'m the human form of the 💯 emoji.',
        'Bingpot!',
        (
            'Cool. Cool cool cool cool cool cool cool, '
            'no doubt no doubt no doubt no doubt.'
        ),
    ]

    response = random.choice(brooklyn_99_quotes)
    await ctx.send(response)

@bot.command(name='meme')
async def meme(ctx):
    reponsejson = requests.get(f'http://alpha-meme-maker.herokuapp.com/memes/{random.randrange(0 , 150)}').json()
    await ctx.send(reponsejson['data']['image'])

@bot.command(name='actus')
async def actus(ctx):
    reponseActu = requests.get('https://api.rss2json.com/v1/api.json?rss_url=https%3A%2F%2Fnews.ycombinator.com%2Frss').json()
    for item in reponseActu['items']:
        await ctx.send(item['link'])
    

@bot.command(name='chien')
async def chien(ctx, arg):
    reponsejson = requests.get(f'https://api.funtranslations.com/translate/doge.json?text={arg}/').json()
    await ctx.send(reponsejson['contents']['translated'])

@bot.command(name='chuck')
async def chuck(ctx):
    reponsejson = requests.get('https://api.chucknorris.io/jokes/random').json()
    await ctx.send(reponsejson['value'])

@bot.command(name='troll')
async def troll(ctx):
    reponseTroll = "voici du troll"
    await ctx.send(reponseTroll)

@bot.command(name='patate')
async def patate(ctx, arg):
    reponsePatate = "DÉ PETATES!"
    await ctx.send(reponsePatate + ' ' + arg)

@bot.command(name='garall')
async def garall(ctx):
    garallOnline = "GARALL EST ENFIN EN LIGNE!!!"
    await ctx.send(garallOnline)

@bot.command(name='garall+')
async def garall(ctx, arg):
    garallPlus = "GARALL EST ENFIN EN LIGNE!!!"
    await ctx.send(garallPlus + arg)

@bot.command(name='multiply')
async def multiply(ctx, arg, arg2):
    paulKing = 'resultat ='
    await ctx.send(f'{paulKing} {(int(arg) * int(arg2))}')

bot.run(TOKEN)