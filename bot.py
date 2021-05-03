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

@bot.command(name='ping')
async def ping(ctx):
    await ctx.channel.send('pong!')

@bot.command(name='salutation')
async def salutation(ctx):
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

@bot.command(name='yahtzee')
async def yahtzee(ctx):
    valeurJoueur = random.randrange(5, 30, 2)
    valeurBot = random.randrange(5, 30, 2)
    if valeurJoueur > valeurBot:
        resultat = 'Vous avez gagné!'
    elif valeurJoueur < valeurBot:
        resultat = 'Désolé, vous avez perdu!'
    elif valeurJoueur == valeurBot:
        resultat = 'Hum, match nul!'

    await ctx.channel.send('Votre valeur: '+ str(valeurJoueur) + ' Ma valeur: '+ str(valeurBot) + ' Résultat: ' + resultat)

@bot.command(name='meteoMontreal')
async def meteoMontreal(ctx):
    reponseMeteo = requests.get('https://www.metaweather.com/api/location/3534/').json()
    for item in reponseMeteo['consolidated_weather']:
        await ctx.channel.send('Date: '+ str(item['applicable_date']) + '   Humidité: ' + str(round(item['humidity'],2)) +
        ' %   Temperature: ' + str(round(item['the_temp'],2)) + ' °C')

@bot.command(name='searchmeteo')
async def seachmeteo(ctx, arg):
    reponseMeteo = requests.get(f'https://www.metaweather.com/api/location/search/?query={arg}').json()
    print(reponseMeteo)
    for item in reponseMeteo:
        await ctx.channel.send('Ville: '+ str(item['title']) +'  id: ' + str(item['woeid']))

@bot.command(name='meteo')
async def meteo(ctx, arg):
    reponseMeteo = requests.get(f'https://www.metaweather.com/api/location/{arg}/').json()
    print(reponseMeteo)
    for item in reponseMeteo['consolidated_weather']:
        await ctx.channel.send('Date: '+ str(item['applicable_date']) + ' Humidité: ' + str(round(item['humidity'],2)) +
        ' % Temperature: ' + str(round(item['the_temp'],2)) + ' °C')


# Affiche des meme
@bot.command(name='meme')
async def meme(ctx):
    reponsejson = requests.get(f'http://alpha-meme-maker.herokuapp.com/memes/{random.randrange(0 , 150)}').json()
    await ctx.send(reponsejson['data']['image'])
    
# Roche Papier Ciseau
@bot.command(name='rpc')
async def rpc(ctx, arg):
    result = ""
    answers = ["roche", "papier", "ciseaux"]
    answerReturned = random.choice(answers)
    results = ["égalité!",  "IVT Bot wins, FATALITY!",  "Pfff... tu as gagné, c\'était de la chance"]
    
    if arg.lower() == answerReturned:
        result = results[0]
        
    elif arg.lower() == answers[0]:
        if answerReturned == answers[1]:
            result = results[1]
        elif answerReturned == answers[2]:
            result = results[2]
            
    elif arg.lower() == answers[1]:
        if answerReturned == answers[2]:
            result = results[1]
        elif answerReturned == answers[0]:
            result = results[2]
    
    elif arg.lower() == answers[2]:
        if answerReturned == answers[0]:
            result = results[1]
        elif answerReturned == answers[1]:
            result = results[2]

    else:
        result = "sais tu au moins jouer à roche/papier/ciseaux?"
        answerReturned = "Meh"
    
    message = answerReturned + ", " + result
    await ctx.send(f'{message}')
bot.run(TOKEN)

# python -m pip install -U youtube_dl
# https://www.ffmpeg.org/