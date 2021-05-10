import os
import requests
import discord
import youtube_dl
import random
import time
from dotenv import load_dotenv
from discord.ext import commands
from discord import FFmpegPCMAudio

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

# Salutations multilingues
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

# Partie de Yahtzee
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

# Requete Lyrics API
@bot.command(name='lyrics')
async def lyrics(ctx, arg1, arg2):
    reponsejson = requests.get(f'https://api.lyrics.ovh/v1/{arg1}/{arg2}').json()
    await ctx.send(reponsejson['lyrics'])

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

#Youtube bot
@bot.command(name='play')
async def play(ctx, url : str):
    songExists = os.path.isfile('song.mp3')

    try:
        if songExists:
            voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
            if not voice is None:
                voice.stop()       
                time.sleep(1) 
            os.remove('song.mp3')
    except PermissionError:
        await ctx.send('Arrêtez la musique avant d\'en lancer une autre')
        return

    voice_state = ctx.author.voice
    if voice_state is None:
        return await ctx.send('Vous devez être dans un salon vocal pour utiliser cette commande.')
    else:
        voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
        if voice is None:
            voiceChannel = ctx.author.voice.channel
            await voiceChannel.connect()
        
        
        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192'
            }]
        }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        for file in os.listdir('./'):
            if file.endswith('.mp3'):
                os.rename(file, 'song.mp3')
        voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
        voice.play(discord.FFmpegPCMAudio('song.mp3'))   
@bot.command(name='leave')
async def leave(ctx):
    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    if voice.is_connected():
        await voice.disconnect()
    else:
        await ctx.send('Je ne suis dans aucun salon vocal.')
@bot.command(name='pause')
async def pause(ctx):
    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    if voice.is_playing():
        voice.pause()
    else:
        await ctx.send('Je ne joue pas d\'audio présentement')
@bot.command(name='resume')
async def resume(ctx):
    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    if voice.is_paused():
        voice.resume()
    else:
        await ctx.send('L\'audio n\'est pas en pause.')
@bot.command(name='stop')
async def stop(ctx):
    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    voice.stop()
    
bot.run(TOKEN)

# python -m pip install -U youtube_dl
# https://www.ffmpeg.org/
