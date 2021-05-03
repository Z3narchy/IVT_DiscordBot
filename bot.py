import random
import os
import requests
import discord
import random
from dotenv import load_dotenv
from discord.ext import commands
import time

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
    
#Jouer à roche papier ciseau
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


@bot.command(name = 'rickroll')
async def rickroll(ctx):
    content = [
        ":notes:",
        "Never gonna give you up",
        "Never gonna let you down",
        "Never gonna run around and desert you",
        "Never gonna make you cry",
        "Never gonna say goodbye",
        "Never gonna tell a lie and hurt you",
        ":notes:",
        "https://cdn.vox-cdn.com/thumbor/HWPOwK-35K4Zkh3_t5Djz8od-jE=/0x86:1192x710/fit-in/1200x630/cdn.vox-cdn.com/uploads/chorus_asset/file/22312759/rickroll_4k.jpg"
    ]
     
    for line in content:
     await ctx.send(f'{line}')
     time.sleep(2)
    

               


bot.run(TOKEN)