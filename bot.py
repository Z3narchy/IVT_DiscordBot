import random
import os
import requests
import discord
import random
from dotenv import load_dotenv
from discord.ext import commands
from random import Random

# Load .env
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

# Setup Bot
bot = commands.Bot(command_prefix='!')

# Commande du bot
# Affiche des meme
@bot.command(name='meme')
async def meme(ctx):
    reponsejson = requests.get(f'http://alpha-meme-maker.herokuapp.com/memes/{random.randrange(0 , 150)}').json()
    await ctx.send(reponsejson['data']['image'])

@bot.command(name='actu')
async def actu(ctx):
    reponseActu = requests.get('https://api.rss2json.com/v1/api.json?rss_url=https%3A%2F%2Fnews.ycombinator.com%2Frss').json()
    await ctx.send(random.choice(reponseActu['items'])['link'])

# Va chercher des nouvelles technologiques
@bot.command(name='actus')
async def actus(ctx):
    reponseActu = requests.get('https://api.rss2json.com/v1/api.json?rss_url=https%3A%2F%2Fnews.ycombinator.com%2Frss').json()
    for item in reponseActu['items']:
        await ctx.send(item['link'])  

# Traduction du texte en son de chien
@bot.command(name='chien')
async def chien(ctx, arg):
    reponsejson = requests.get(f'https://api.funtranslations.com/translate/doge.json?text={arg}/').json()
    await ctx.send(reponsejson['contents']['translated'])

# Va chercher des jokes sur Chuck Norris
@bot.command(name='chuck')
async def chuck(ctx):
    reponsejson = requests.get('https://api.chucknorris.io/jokes/random').json()
    await ctx.send(reponsejson['value'])
# Pour Étienne 
@bot.command(name='patate')
async def patate(ctx, arg):
    reponsePatate = "DÉ PETATES!"
    await ctx.send(reponsePatate + ' ' + arg)

# Fait la multipication de deux nombres
@bot.command(name='multiply')
async def multiply(ctx, arg, arg2):
    paulKing = 'resultat ='
    await ctx.send(f'{paulKing} {(int(arg) * int(arg2))}')

@bot.command(name='Ping')
async def Ping(ctx):
    await ctx.channel.send('Pong!')

@bot.command(name='Salutation')
async def Salutation(ctx):
    salutation = [
        'Hello!',
        'Bonjour!',
        'Aloha!',
        'Buenos dias!',
        'こんにちは!',
        'Buongiorno!',
        'Salve!',
        'Buna ziua!',
    ]

    response = random.choice(salutation)
    await ctx.channel.send(response)

@bot.command(name='Yatzee')
async def Yatzee(ctx):
    valeurJoueur = random.randrange(5, 30, 2)
    valeurBot = random.randrange(5, 30, 2)
    if valeurJoueur > valeurBot:
        resultat = 'Vous avez gagné!'
    elif valeurJoueur < valeurBot:
        resultat = 'Désolé, vous avez perdu!'
    elif valeurJoueur == valeurBot:
        resultat = 'Hum, match nul!'

    await ctx.channel.send('Votre valeur: '+ str(valeurJoueur) + ' Ma valeur: '+ str(valeurBot) + ' Résultat: ' + resultat)




bot.run(TOKEN)