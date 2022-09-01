import os
import discord
from discord import FFmpegPCMAudio
from discord.ext.commands import Bot
from dotenv import load_dotenv
import datetime
import asyncio




load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
PREFIX = os.getenv('DISCORD_PREFIX') #its '&' and '+'

intents = discord.Intents.all()
bot = Bot(command_prefix=list(PREFIX), intents=intents)
bot.remove_command('help')

@bot.event
async def on_ready():
    print('Bot Ready cuy')
    await daily_msg()



#   RADIO AWIKWOK
@bot.command(aliases=['radio', 'r'])
async def play(ctx, url: str = 'https://23743.live.streamtheworld.com/PRAMBORS_FM_SC?dist=pramborsweb&pname=tdwidgets'):
    if (ctx.author.voice):
        channel = ctx.author.voice.channel
        global player
        player = await channel.connect()
        await ctx.send("Sy Join Banh - PRAMBORS FM")
    else:
        await ctx.send("join channel dulu atuh banh")
        return

    player.play(FFmpegPCMAudio('https://23743.live.streamtheworld.com/PRAMBORS_FM_SC?dist=pramborsweb&pname=tdwidgets', executable='./ffmpeg-2022-08-29-git-f99d15cca0-full_build/bin/ffmpeg.exe'))



@bot.command(aliases=['leave', 'stopradio'])
async def stop(ctx):
    player.stop()
    if (ctx.voice_client):
        ctx.send("Ok aq keluar banh")
        await ctx.guild.voice_client.disconnect()
    else:
        ctx.send("g lg di channel banh")


#   commands

@bot.command(name='hitam')
async def hitam(ctx):
    if ctx.author == bot.user:
        return
    await ctx.send("https://i.ytimg.com/vi/E20T_7CxcKU/maxresdefault.jpg")

@bot.command(name='help')
async def help_msg(ctx):
    if ctx.author == bot.user:
        return
    elif ctx.author != bot.user:
        await ctx.send("""Prefix = '&'
        &radio alias &r         = For Radio (Prambors)
        &leave alias &stopradio = Stop Radio
        &hitam                  = Bundah :weary:
        &help                   = Opens this message
        """)

@bot.event
async def on_member_join(member):
    #When a member joins the discord, they will get mentioned with this welcome message
    channel = bot.get_channel(799961113714360350)
    await channel.send(f'Cok. @{member.name} siapa anjing')
    
async def daily_msg():
    while True:
        now = datetime.datetime.now()
        then = now+datetime.timedelta(hours=5)
        # then= now.replace(hour=4, minute=0)
        wait_time = (then-now).total_seconds()
        await asyncio.sleep(wait_time)

        channel = bot.get_channel(799961113714360350)

        await channel.send("""niguer
        https://c.tenor.com/lt09oyt0gEkAAAAC/shap-siap.gif""")
    



















bot.run(TOKEN)