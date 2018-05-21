import discord
from discord.ext import commands
import logging
import asyncio
import random
import time
import os

client = commands.Bot(command_prefix="i!")
footer_text = "Limited Infinity™"

@client.event
async def on_ready():
    print("Logged in as:")
    print(client.user.name)
    print(client.user.id)
    print("---------------")
    await client.change_presence(game=discord.Game(name='on Limited Infinity™'))

# serverinfo
@client.command(pass_context=True)
async def mc(ctx):
    author = ctx.message.author
    msg = discord.Embed(colour=0xe3e550, description= "")
    msg.title = ":closed_book: Member Count :closed_book: "
    msg.add_field(name="MEMBERS", value=(len(ctx.message.server.members)), inline=True)
    await client.say(embed=msg)

# }userinfo <user>
@client.command(pass_context=True)
async def userinfo(ctx, userName: discord.Member = None):
    member_role = discord.utils.get(ctx.message.server.roles, name='Member')
    staff_role = discord.utils.get(ctx.message.server.roles, name='Staff')
    author = ctx.message.author
    msg = discord.Embed(colour=0xe3e550, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if member_role in author.roles or staff_role in author.roles:
        if userName == None:
            msg.title = ""
            msg.add_field(name="       :warning: ", value="`i!userinfo <user>`")
        else:
            imageurl = userName.avatar_url
            msg.title = ":closed_book: USER INFORMATION"
            msg.set_thumbnail(url=imageurl)
            msg.add_field(name="NAME:", value=(userName), inline=True)
            msg.add_field(name="ID:", value=(userName.id), inline=True)
            msg.add_field(name="CREATED AT:", value=(userName.created_at), inline=True)
            msg.add_field(name="JOINED AT:", value=(userName.joined_at), inline=True)
            msg.add_field(name="STATUS:", value=(userName.status), inline=True)
            msg.add_field(name="IS BOT:", value=(userName.bot), inline=True)
            msg.add_field(name="GAME:", value="Playing {}".format(userName.game), inline=True)
            msg.add_field(name="NICKNAME:", value=(userName.nick), inline=True)
            msg.add_field(name="TOP ROLE:", value=(userName.top_role), inline=True)
            msg.add_field(name="VOICE CHANNEL:", value=(userName.voice_channel), inline=True)
    await client.say(embed=msg)
    print("============================================================")
    print("<userinfo <user>")
    print("{} ### {}".format(author, author.id))
    print("============================================================")
    client.run(os.environ['BOT_TOKEN'])
