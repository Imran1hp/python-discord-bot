import discord 
from discord.ext import commands
import logging
from dotenv import load_dotenv
import os
import random
import webserver

load_dotenv()
token =os.getenv('DISCORD_TOKEN')


handler =logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
intents = discord.Intents.default()
intents.message_content =True
intents.members = True

bot = commands.Bot(command_prefix='!',intents=intents)
secret_role ="Tousif ar bou"
@bot.event
async def on_ready():
    print(f" {bot.user.name} is runing")
@bot.event
async def on_member_join(member):
    await member.send(f'Welcome to the server {member.name}!')
@bot.event
async def on_member_remove(member):
    print(f"{member.name}has left the server")
    

@bot.event
async def on_message(message):
    if message.author ==bot.user:
        return
    if "hannan" in message.content.lower():
        await message.delete()
        await message.channel.send(f"{message.author.mention} Respect who give you birth!")

    await bot.process_commands(message)     


@bot.command()
async def hello(ctx):
    await ctx.send(f"Hello bsdk {ctx.author.name}")

@bot.command()    
async def ping(ctx):
    await ctx.send(f"Pong! {round(bot.latency*1000)}ms")

@bot.command()
async def about(ctx):
    await ctx.send("I am a discord bot make by Imran....\nAnd he said i am a dog from usthi.... ")

@bot.command()
async def userinfo(ctx,member:discord.Member):
    await ctx.send(f"Name:{member.name}\nID:{member.id}\nJoined at:{member.joined_at}")

@bot.command()
async def avatar(ctx,member:discord.Member):
    await ctx.send(member.display_avatar.url)

@bot.command()
async def roll(ctx):
    await ctx.send(f"You got {random.randint(1,6)}")    

@bot.command()
async def bark(ctx):
    await ctx.send("gheu gheu gheu .......")   


@bot.command()
async def tousif_ar_bou(ctx):
    role = discord.utils.get(ctx.guild.roles,name=secret_role)
    if role:
        await ctx.author.add_roles(role)
        await ctx.send(f"Role {secret_role} has been assigned to {ctx.author.name}")

    else:
        await ctx.send(f"Role {secret_role} does not exist")

@bot.command()
async def tousif_talak(ctx):
    role =discord.utils.get(ctx.guild.roles,name=secret_role)
    if role:
        await ctx.author.remove_roles(role)
        await ctx.send(f"Touif ar {ctx.author.name} somporko ses ")
    else:
        await ctx.send(f"Role {secret_role} does not exist")    

webserver.keep_alive()

bot.run(token,log_handler=handler,log_level=logging.DEBUG)




