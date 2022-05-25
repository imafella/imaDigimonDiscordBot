import asyncio
import discord
import logging
import os
from discord.ext import commands
from discord.ext.commands import Bot
from dotenv import load_dotenv
from ThingyDo.DieRoll import *
from ThingyDo.Shout import shout
from ThingyDo.Info import *
from ThingyDo.Ascii import *
from ThingyDo.GetGreeting import *
from ThingyDo.DigimonKeywords import *
from ThingyDo.DigimonIOAPI import *
from ThingyDo.TimeingDefinitions import *

intents = discord.Intents.all()
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
GUILD_ID = os.getenv("DISCORD_GUILD")
api_url = os.getenv("digimonAPI_search")

client = commands.Bot(command_prefix="!", intents=intents)
logging.basicConfig(filename=".\output.log", filemode="w", level=logging.INFO, format="%(asctime)s:%(levelname)s:%(message)s")

#
#Events
#

@client.event
async def on_error(event, *args, **kwargs):
	print("Here is the log \n ")
	print(traceback.format_exc())

@client.event
async def on_member_join(member):
	username = str(member.name)[:-5]
	channel = get_channel(os.getenv("DISCORD_GENERAL"))
	await channel.send(pickGreeting(username))

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name='with nukes'))
    
    print('Connected to bot: {}'.format(client.user.name))
    print('Bot ID: {}'.format(client.user.id))


#
#Commands
#

@client.command(pass_context=True)
async def roll(ctx):
	username = str(ctx.author)[:-5]
	message = ctx.message.content
	channel = ctx.channel
	await channel.send(dieRoll(username, message))
	await ctx.message.delete()

@client.command(pass_context=True)
async def yell(ctx):
	username = str(ctx.author)[:-5]
	channel = ctx.channel
	await channel.send(shout(username))
	await ctx.message.delete()

@client.command(pass_context=True)
async def test(ctx):
	username = str(ctx.author)[:-5]
	channel = ctx.channel
	await channel.send("Hello "+username)
	await ctx.message.delete()

@client.command(pass_context=True)
async def info(ctx):
	channel = ctx.channel
	await channel.send(giveInfo())	
	await ctx.message.delete()

@client.command(pass_context=True)
async def flip(ctx):
    channel = ctx.channel
    await channel.send(tblFlip())
    await ctx.message.delete()

@client.command(pass_context=True,name="search", aliases=["s", "lookup", "find", "f"])
async def search(ctx, arg):
	channel = ctx.channel
	await channel.send(searchInput(arg, api_url))

@client.command(pass_context=True, name="timing")
async def timing(ctx, message):
	channel=ctx.channel
	inTxt = ctx.message.content.split(" ")
	toSearch = str(' '.join(inTxt[1:]))
	await channel.send(pickTiming(toSearch))
	await ctx.message.delete()

#
#
#Commands
# Keywords
#
@client.command(pass_context=True, name="blocker" ,aliases=["Blocker","block","Block", "DefendyBoi"])
async def blocker(ctx):
	channel = ctx.channel
	await channel.send(getBlocker())
	await ctx.message.delete()

@client.command(pass_context=True, name = "secAttack", aliases=["secattack","securityattack", "SecurityAttack", "Securityattack", "Security"])
async def secAttack(ctx):
	channel = ctx.channel
	username = str(ctx.author)[:-5]
	await channel.send("Please let me know if it is 'plus' or 'minus' sec attack "+username+".")
	


@client.command(pass_context=True, name = "secAttackPlus", aliases=["SecAttackPlus", "secattackplus", "secattackPlus", "SecAttackplus", "SecurityAttackPlus", "SecurityAttackplus", "Securityattackplus", "securityattackplus", "secPlus", "SecPlus", "secplus", "SecurityPlus", "Securityplus", "securityplus", "securityPlus"])
async def secAttackPlus(ctx):
	channel = ctx.channel
	await channel.send(getSecAttackPlus())
	await ctx.message.delete()


@client.command(pass_context=True, name = "secAttackMinus", aliases=["SecAttackMinus", "secattackminus", "secattackMinus", "SecAttackminus", "SecurityAttackMinus", "SecurityAttackminus", "Securityattackminus", "securityattackminus", "secMinus", "SecMinus", "secminus", "SecurityMinus", "Securityminus", "securityminus", "securityMinus"])
async def SecAttackMinus(ctx):
	channel = ctx.channel
	await channel.send(getSecAttackMinus())
	await ctx.message.delete()


@client.command(pass_context=True, name="recovery", aliases=["Recovery", "GrowSecurity"])
async def recovery(ctx):
	channel = ctx.channel
	await channel.send(getRecovery())
	await ctx.message.delete()

@client.command(pass_context=True, name ="piercing", aliases=["Piercing"])
async def piercing(ctx):
	channel = ctx.channel
	await channel.send(getPiercing())
	await ctx.message.delete()

@client.command(pass_context=True, name="draw", aliases=["Draw"])
async def draw(ctx):
	channel = ctx.channel
	await channel.send(getDraw())
	await ctx.message.delete()

@client.command(pass_context=True, name="jamming", aliases=["Jamming"])
async def jamming(ctx):
	channel = ctx.channel
	await channel.send(getJamming())
	await ctx.message.delete()

@client.command(pass_context=True, name="digisorption", aliases=["Digisorption"])
async def digisorption(ctx):
	channel = ctx.channel
	await channel.send(getDigisorption())
	await ctx.message.delete()

@client.command(pass_context=True, name="reboot", aliases=["Reboot", "RestandyBoi"])
async def reboot(ctx):
	channel = ctx.channel
	await channel.send(getReboot())
	await ctx.message.delete()

@client.command(pass_context=True , name="deDigivolve", aliases=["DeDigivolve", "Dedigivolve"])
async def deDigivolve(ctx):
	channel = ctx.channel
	await channel.send(getDeDigivolve())
	await ctx.message.delete()

@client.command(pass_context=True, name = "retaliation", aliases=["Retaliation"])
async def retaliation(ctx):
	channel = ctx.channel
	await channel.send(getRetaliation())
	await ctx.message.delete()

@client.command(pass_context=True, name="digiBurst", aliases=["DigiBurst", "Digiburst", "digiburst"])
async def digiBurst(ctx):
	channel = ctx.channel
	await channel.send(getDigiburst())
	await ctx.message.delete()

@client.command(pass_context=True, name="rush", aliases=["Rush"])
async def rush(ctx):
	channel = ctx.channel
	await channel.send(getRush())
	await ctx.message.delete()

@client.command(pass_context=True, name="blitz", aliases=["Blitz"])
async def blitz(ctx):
	channel = ctx.channel
	await channel.send(getBlitz())
	await ctx.message.delete()


@client.command(pass_context=True, name="delay", aliases=["Delay"])
async def delay(ctx):
	channel = ctx.channel
	await channel.send(getDelay())
	await ctx.message.delete()

@client.command(pass_context=True, name="decoy", aliases=["Decoy"])
async def decoy(ctx):
	channel = ctx.channel
	await channel.send(getDecoy())
	await ctx.message.delete()

@client.command(pass_context=True, name="armorPurge", aliases=["ArmorPurge", "Armorpurge", "armorpurge"])
async def armorPurge(ctx):
	channel = ctx.channel
	await channel.send(getArmorPurge())
	await ctx.message.delete()


	
client.run(TOKEN)