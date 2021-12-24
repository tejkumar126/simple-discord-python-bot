import discord
from discord.ext import commands
from discord.ext import commands
import os

client = commands.Bot(command_prefix="")#Bot's Prefix


@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.dnd,
                                 activity=discord.Game("Watching Server"))#Put Any Kind Of Status
    print(" Online")


@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! In {round(client.latency * 1000)}ms')


@client.command(name="userinfo")
async def whoami(ctx):
    await ctx.send(f"You are {ctx.message.author.name}")


@client.command()
async def clear(ctx, amount=3):
    await ctx.channel.purge(limit=amount)
    

@client.command()
@has_permissions(manage_channels=True)
async def lockdown(ctx):
    await ctx.channel.set_permissions(ctx.guild.default_role,send_messages=False)
    await ctx.send( ctx.channel.mention + "is now in lockdown.")

@client.command()
@has_permissions(manage_channels=True)
async def unlock(ctx):
    await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=True)
    await ctx.send(ctx.channel.mention + "has been unlocked.")


@client.command()
async def slowmode(ctx, seconds: int):
    await ctx.channel.edit(slowmode_delay=seconds)
    await ctx.send(f"Set the slowmode delay in this channel to {seconds} seconds!")


@client.command(aliases=["mc"])

async def member_count(ctx):

    a=ctx.guild.member_count
    b=discord.Embed(title=f"Members in {ctx.guild.name}",description=a,color=discord.Color((0xffff00)))
    await ctx.send(embed=b)


client.run('')#Bot's Token


#Doing on replit Hide your token by doing this token = os.getenv("") and save your token in secret env bot.run(os.getenv('TOKEN'))
