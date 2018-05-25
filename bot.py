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

@client.event
async def on_member_join(member):
    serverchannel = member.server.default_channel
    msg = "Willkommen {0} auf {1}".format(member.mention, member.server.name)
    await client.send_message(serverchannel, msg)

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
    
# serverinfo
@client.command(pass_context=True)
async def serverinfo(ctx):
    author = ctx.message.author
    msg = discord.Embed(colour=0xe3e550, description= "")
    msg.title = ":closed_book: Server Information :closed_book:"
    msg.add_field(name="MEMBERS", value=(len(ctx.message.server.members)), inline=True)
    msg.add_field(name="CHANNELS", value=(len(ctx.message.server.channels)), inline=True)
    msg.add_field(name="EMOJIS", value=(len(ctx.message.server.emojis)), inline=True)
    msg.add_field(name="ID", value=(ctx.message.server.id), inline=True)
    msg.add_field(name="REGION", value=(ctx.message.server.region), inline=True)
    msg.add_field(name="ROLES", value=(len(ctx.message.server.roles)), inline=True)
    msg.add_field(name="OWNER", value=(ctx.message.server.owner), inline=True)
    msg.add_field(name="RELEASE DATE:", value="23th of March 2018", inline=True)
    await client.say(embed=msg)
    print("============================================================")
    print("<serverinfo")
    print("{} ### {}".format(author, author.id))
    print("============================================================")
    
# <echo <text>
@client.command(pass_context=True)
async def say(ctx, *, args=None): 
    staff_role = discord.utils.get(ctx.message.server.roles, name='Staff')
    author = ctx.message.author
    msg = discord.Embed(colour=0xe3e550, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if staff_role in author.roles or staff_role in author.roles:
        if args == None:
            msg.add_field(name=":warning: ", value="i!say <text>")
            await client.say(embed=msg)
        else:
            await client.say("{}".format(args))
            await client.delete_message(ctx.message)
    else:
        msg.add_field(name=":warning: ", value="`This command can only be used by Staff!`")
        await client.say(embed=msg)
        
# <lick <user>
@client.command(pass_context=True)
async def lick(ctx, userName: discord.Member = None):
    author = ctx.message.author
    msg = discord.Embed(colour=0xe3e550, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if userName == None:
        msg.add_field(name=":bulb: Emotes :bulb: ", value="`i!lick <user>`")
    else:
        msg.set_image(url="{}".format(random.choice(licklinks)))
        msg.add_field(name=":tongue: Emotes :tongue:", value="`{} licked {}!`".format(author.display_name, userName.display_name), inline=True)
    await client.say(embed=msg)
    print("============================================================")
    print("}lick <user>")
    print("{} ### {}".format(author, author.id))
    print("============================================================")

licklinks = ["https://i.imgur.com/QkRz1GJ.gif",
             "https://i.imgur.com/ObCPKYV.gif",
             "https://i.imgur.com/7fWrYqd.gif",
             "https://i.imgur.com/O8CNVUL.gif",
             "https://i.imgur.com/4QIlJtC.gif",
             "https://i.imgur.com/LptJIi1.gif",
             "https://i.imgur.com/THGgRJz.gif"]

# <hug <user>
@client.command(pass_context=True)
async def hug(ctx, userName: discord.Member = None):
    author = ctx.message.author
    msg = discord.Embed(colour=0xe3e550, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if userName == None:
        msg.add_field(name=":warning: ", value="`i!hug <user>`")
    else:
        msg.set_image(url="{}".format(random.choice(huglinks)))
        msg.add_field(name=":bulb: Emotes :bulb: ", value="`{}, you got a hug from {}!`".format(userName.display_name, author.display_name), inline=True)
    await client.say(embed=msg)
    print("============================================================")
    print("}hug <user>")
    print("{} ### {}".format(author, author.id))
    print("============================================================")

huglinks = ["https://i.imgur.com/yE2RnXK.gif",
            "https://i.imgur.com/R9sYxk8.gif",
            "https://i.imgur.com/iLBEoKv.gif",
            "https://i.imgur.com/cc554e8.gif",
            "https://i.imgur.com/1dqkjHe.gif",
            "https://i.imgur.com/Ph8GTqg.gif",
            "https://i.imgur.com/G6EnOxd.gif",
            "https://i.imgur.com/ZxwHn5Y.gif",
            "https://i.imgur.com/movPIsP.gif",
            "https://i.imgur.com/tKlfSgo.gif",
            "https://i.imgur.com/ICg9nCr.gif",
            "https://i.imgur.com/yC95DC2.gif",
            "https://i.imgur.com/hRYXNKX.gif",
            "https://i.imgur.com/br3bGQc.gif",
            "https://i.imgur.com/IcNGAQD.gif"]

# <cuddle <user>
@client.command(pass_context=True)
async def cuddle(ctx, userName: discord.Member = None):
    author = ctx.message.author
    msg = discord.Embed(colour=0xe3e550, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if userName == None:
        msg.add_field(name=":warning: ", value="`i!cuddle (user)`")
    else:
        msg.set_image(url="{}".format(random.choice(cuddlelinks)))
        msg.add_field(name=":bulb: Emotes :bulb: ", value="`{}, you got a cuddle from {}!`".format(userName.display_name, author.display_name), inline=True)
    await client.say(embed=msg)
    print("============================================================")
    print("}cuddle <user>")
    print("{} ### {}".format(author, author.id))
    print("============================================================")

cuddlelinks = ["https://i.imgur.com/GWNWcLH.gif",
               "https://i.imgur.com/i3Eqqgz.gif",
               "https://i.imgur.com/GpFk6fE.gif",
               "https://i.imgur.com/mc3Z7wf.gif",
               "https://i.imgur.com/N5JYB5r.gif",
               "https://i.imgur.com/PGp8JYq.gif"]

# <pat <user>
@client.command(pass_context=True)
async def pat(ctx, userName: discord.Member = None):
    author = ctx.message.author
    msg = discord.Embed(colour=0xe3e550, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if userName == None:
        msg.add_field(name=":warning: ", value="`i!pat <user>`")
    else:
        msg.set_image(url="{}".format(random.choice(patlinks)))
        msg.add_field(name=":bulb: Emotes :bulb: ", value="`{}, you got a pat from {}!`".format(userName.display_name, author.display_name), inline=True)
    await client.say(embed=msg)
    print("============================================================")
    print("}pat <user>")
    print("{} ### {}".format(author, author.id))
    print("============================================================")

patlinks = ["https://i.imgur.com/8eApUKG.gif",
            "https://i.imgur.com/qVcP9Pt.gif",
            "https://i.imgur.com/X9hKO2p.gif",
            "https://i.imgur.com/v8cRPH9.gif",
            "https://i.imgur.com/N6C7C30.gif",
            "https://i.imgur.com/M9QPcY6.gif",
            "https://i.imgur.com/oUSdjX6.gif",
            "https://i.imgur.com/mFFr4e0.gif",
            "https://i.imgur.com/3F7kmCd.gif",
            "https://i.imgur.com/7yFvJ6m.gif",
            "https://i.imgur.com/y3La9yP.gif",
           "https://i.imgur.com/u7kxk2Y.mp4"]

# <kiss <user>
@client.command(pass_context=True)
async def kiss(ctx, userName: discord.Member = None):
    author = ctx.message.author
    msg = discord.Embed(colour=0xe3e550, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if userName == None:
        msg.add_field(name=":warning: ", value="`i!kiss (user)`")
    else:
        msg.set_image(url="{}".format(random.choice(kisslinks)))
        msg.add_field(name=":bulb: Emotes :bulb: ", value="`{}, you got kissed by {}!`".format(userName.display_name, author.display_name), inline=True)
    await client.say(embed=msg)
    print("============================================================")
    print("}kiss <user>")
    print("{} ### {}".format(author, author.id))
    print("============================================================")

kisslinks = ["https://i.imgur.com/0Ri9sfq.gif",
             "https://i.imgur.com/EMdpmXW.gif",
             "https://i.imgur.com/Y9iLoiv.gif",
             "https://i.imgur.com/ZlqZy8S.gif",
             "https://i.imgur.com/ySav1IQ.gif",
             "https://i.imgur.com/ZGfrn2d.gif",
             "https://i.imgur.com/glwWeUl.gif",
             "https://i.imgur.com/j5hDl7V.gif",
             "https://i.imgur.com/w7mVYty.gif",
             "https://i.imgur.com/FJ5bckO.gif",
             "https://i.imgur.com/KqVmVU7.gif",
             "https://i.imgur.com/EM1C9a6.gif",
             "https://i.imgur.com/TACVpH9.gif",
             "https://i.imgur.com/opiHLtc.gif",
             "https://i.imgur.com/LylJAea.gif"]

# <poke <user>
@client.command(pass_context=True)
async def poke(ctx, userName: discord.Member = None):
    author = ctx.message.author
    msg = discord.Embed(colour=0xe3e550, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if userName == None:
        msg.add_field(name=":warning: ", value="`i!poke (user)`")
    else:
        msg.set_image(url="{}".format(random.choice(pokelinks)))
        msg.add_field(name=":bulb: Emotes :bulb: ", value="`{}, you got poked by {}!`".format(userName.display_name, author.display_name), inline=True)
    await client.say(embed=msg)
    print("============================================================")
    print("}poke <user>")
    print("{} ### {}".format(author, author.id))
    print("============================================================")

pokelinks = ["https://i.imgur.com/HAAktbl.gif",
             "https://i.imgur.com/Fmd0Rsu.gif",
             "https://i.imgur.com/1rObSM3.gif",
             "https://i.imgur.com/Wo2fc94.gif",
             "https://i.imgur.com/rtTucBW.gif",
             "https://i.imgur.com/4c2mC5d.gif",
             "https://i.imgur.com/1DVD84G.gif"]

# <spank <user>
@client.command(pass_context=True)
async def spank(ctx, userName: discord.Member = None):
    author = ctx.message.author
    msg = discord.Embed(colour=0xe3e550, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if userName == None:
        msg.add_field(name=":warning: ", value="`i!spank (user)`")
    else:
        msg.set_image(url="{}".format(random.choice(spanklinks)))
        msg.add_field(name=":bulb: Emotes :bulb: ", value="`{} spanked {}!`".format(author.display_name, userName.display_name), inline=True)
    await client.say(embed=msg)
    print("============================================================")
    print("}spank <user>")
    print("{} ### {}".format(author, author.id))
    print("============================================================")

spanklinks = ["https://i.imgur.com/dt1TTQu.gif",
              "https://i.imgur.com/ZsTbDvh.gif",
              "https://i.imgur.com/4LHwG60.gif",
              "https://i.imgur.com/xLOoHKP.gif",
              "https://i.imgur.com/UShywVv.gif",
              "https://i.imgur.com/RE3mnrA.gif"]

# <sorry <user>
@client.command(pass_context=True)
async def sorry(ctx, userName: discord.Member = None):
    author = ctx.message.author
    msg = discord.Embed(colour=0xe3e550, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if userName == None:
        msg.add_field(name=":warning: ", value="`i!sorry (user)`")
    else:
        msg.set_image(url="{}".format(random.choice(sorrylinks)))
        msg.add_field(name=":bulb: Emotes :bulb: ", value="`{}, {} is saying sorry!`".format(userName.display_name, author.display_name), inline=True)
    await client.say(embed=msg)
    print("============================================================")
    print("}hug <user>")
    print("{} ### {}".format(author, author.id))
    print("============================================================")

sorrylinks = ["https://i.imgur.com/9f2FsAQ.gif",
            "https://i.imgur.com/9f2FsAQ.gif",
            "https://tenor.com/search/sorry-gifs",
            "https://giphy.com/explore/im-sorry",
            "https://tenor.com/search/im-sorry-gifs",
            "https://i.imgur.com/9f2FsAQ.gif"]

# }cry
@client.command(pass_context=True)
async def cry(ctx):
    author = ctx.message.author
    msg = discord.Embed(colour=0xe3e550, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    msg.set_image(url="{}".format(random.choice(crylinks)))
    msg.add_field(name=":bulb: Emotes :bulb: ", value="`{} is crying!` *Pat pat pat*".format(author.display_name), inline=True)
    await client.say(embed=msg)
    print("============================================================")
    print("}cry")
    print("{} ### {}".format(author, author.id))
    print("============================================================")
    
crylinks = ["https://media1.giphy.com/media/ROF8OQvDmxytW/giphy-downsized.gif",
            "https://media1.tenor.com/images/06ae6bbe852471939cf61a81e5a9eb23/tenor.gif?itemid=5370823",
            "https://78.media.tumblr.com/e9fb46144efc579746e57bcaebd3350a/tumblr_olrmy4djBG1tydz8to1_500.gif",
            "http://i.imgur.com/k5B1CBd.jpg",
            "https://media.giphy.com/media/hyU0RHvlS3iQU/giphy.gif",
            "https://media1.tenor.com/images/5912cbe4bc0dec511b5e0996a2ad9b6f/tenor.gif?itemid=8620704",
            "https://s9.favim.com/orig/131225/an-anime-anime-gif-anime-guy-Favim.com-1182388.gif",
            "https://media1.tenor.com/images/06ae6bbe852471939cf61a81e5a9eb23/tenor.gif?itemid=5370823",
            "https://media.tenor.com/images/d571f86a5adcb4545444e9d1dc4638f9/tenor.gif",
            "https://i.pinimg.com/originals/73/3d/59/733d5948098702b0d6f156819143b581.gif",
            "https://67.media.tumblr.com/aa7766807df523677bb9c73da94ee049/tumblr_npwxeb2dPp1u7ltf6o1_500.gif",
            "https://static2.fjcdn.com/thumbnails/comments/I+actually+dont+remember+i+think+because+of+the+horns+_78025db895d293c2765eaace345742f0.gif"]

# }slap <user>
@client.command(pass_context=True)
async def slap(ctx, userName: discord.Member = None):
    author = ctx.message.author
    msg = discord.Embed(colour=0xe3e550, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if userName == None:
        msg.add_field(name=":warning: ", value="`i!slap (user)`")
    else:
        msg.set_image(url="{}".format(random.choice(slaplinks)))
        msg.add_field(name=":bulb: Emotes :bulb: ", value="`{}, you got slapped by {}! Ouch...`".format(userName.display_name, author.display_name), inline=True)
    await client.say(embed=msg)
    print("============================================================")
    print("}slap <user>")
    print("{} ### {}".format(author, author.id))
    print("============================================================")
    
slaplinks = ["https://i.imgur.com/EAF42MG.gif",
             "https://i.imgur.com/tLTT9Q4.gif",
             "https://i.imgur.com/tEWjg7v.gif",
             "https://i.imgur.com/MlkLTjv.gif",
             "https://i.imgur.com/hoTYJZP.gif",
             "https://i.imgur.com/Pthhs3Y.gif"]

# }report <user> <reason>
@client.command(pass_context=True)
async def report(ctx, userName: discord.Member = None, *, args = None):
    author = ctx.message.author
    msg = discord.Embed(colour=0xe3e550, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    msg2 = discord.Embed(colour=0xe3e550, description= "")
    msg2.title = ""
    msg2.set_footer(text=footer_text)
    if userName == None or args == None:
        msg.add_field(name=":warning: ", value="`i!report <user> <reason>`")
    else:
        msg.add_field(name=":clipboard: **REPORT**", value="`{} has reported {}!`".format(author.display_name, userName.display_name))
        msg2.add_field(name=":clipboard: **REPORT**", value="**Reporter:**\n`{}` ### `{}`\n **Reported:**\n`{}` ### `{}`\n **Reason:**\n`{}`".format(author, author.id, userName, userName.id, args))
        channel = client.get_channel('447801494855745547')
        await client.send_message(channel, embed=msg2)
    await client.say(embed=msg)
    print("============================================================")
    print("}report <user> <reason>")
    print("{} ### {}".format(author, author.id))
    print("============================================================")
    
# }idban <user id> [reason]
@client.command(pass_context=True)
async def idban(ctx, userID: int = None, *, args = None):
    helper_role = discord.utils.get(ctx.message.server.roles, name='Administrator')
    mod_role = discord.utils.get(ctx.message.server.roles, name='Administrator')
    admin_role = discord.utils.get(ctx.message.server.roles, name='Administrator')
    manager_role = discord.utils.get(ctx.message.server.roles, name='Co Owner')
    owner_role = discord.utils.get(ctx.message.server.roles, name='Owner')
    author = ctx.message.author
    msg = discord.Embed(colour=0xe3e550, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if mod_role in author.roles or admin_role in author.roles or manager_role in author.roles or owner_role in author.roles:
        if userID == None:
            msg.add_field(name=":warning: ", value="`i!idban <userID> <reason>`")
        elif user == None and args is not None:
            msg.add_field(name=":tools: ", value="`{} ID-Banned the following ID: {}!`\n`Reason: {}`".format(author.display_name, userID, args))
            await client.http.ban(userID, guild.id, 0)
        elif user == None and args == None:
            msg.add_field(name=":tools: ", value="`{} ID-Banned the following ID: {}!`\n`Reason: ?`".format(author.display_name, userID))
            await client.http.ban(userID, guild.id, 0)
        else:
            msg.add_field(name=":warning: ", value="`Unknown error!`")
    else:
        msg.add_field(name=":warning: ", value="`This command can only be used by Admin+!`")
    await client.say(embed=msg)
    print("============================================================")
    print("}idban <user id> [reason]")
    print("{} ### {}".format(author, author.id))
    print("============================================================")
    
# }purge <number>
@client.command(pass_context=True)
async def purge(ctx, number: int = None):
    helper_role = discord.utils.get(ctx.message.server.roles, name='Moderator')
    mod_role = discord.utils.get(ctx.message.server.roles, name='Moderator')
    admin_role = discord.utils.get(ctx.message.server.roles, name='Administrator')
    manager_role = discord.utils.get(ctx.message.server.roles, name='Co Owner')
    owner_role = discord.utils.get(ctx.message.server.roles, name='Owner')
    author = ctx.message.author
    msg = discord.Embed(colour=0xe3e550, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if helper_role in author.roles or mod_role in author.roles or admin_role in author.roles or manager_role in author.roles or owner_role in author.roles:
        if number == None:
            msg.add_field(name=":warning: ", value="`i!purge <number>`")
        else:
            deleted = await client.purge_from(ctx.message.channel, limit=number)
            if len(deleted) < number:
                msg.add_field(name=":wastebasket: ", value="`{} tried to delete {} messages!`\n`Deleted {} message(s)!`".format(author.display_name, number, len(deleted)))
            else:
                msg.add_field(name=":wastebasket: ", value="`{} deleted {} message(s)!`".format(author.display_name, len(deleted)))
    else:
        msg.add_field(name=":warning: ", value="`This command can only be used by staff!`")
    await client.say(embed=msg)
    print("============================================================")
    print("}purge <number>")
    print("{} ### {}".format(author, author.id))
    print("============================================================")
    
# }punish <user> <time> [reason]
@client.command(pass_context=True)
async def tempmute(ctx, userName: discord.Member = None, time: int = None, *, args = None):
    member_role = discord.utils.get(ctx.message.server.roles, name ='Members')
    punished_role = discord.utils.get(ctx.message.server.roles, name='Muted')
    helper_role = discord.utils.get(ctx.message.server.roles, name='Helper')
    mod_role = discord.utils.get(ctx.message.server.roles, name='Moderator')
    admin_role = discord.utils.get(ctx.message.server.roles, name='Administrator')
    manager_role = discord.utils.get(ctx.message.server.roles, name='Co Owner')
    owner_role = discord.utils.get(ctx.message.server.roles, name='Owner')
    author = ctx.message.author
    msg = discord.Embed(colour=0xe3e550, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if helper_role in author.roles or mod_role in author.roles or admin_role in author.roles or manager_role in author.roles or owner_role in author.roles:
        if userName == None or time == None:
            msg.add_field(name=":warning: ", value="`i!tempmute <user> <time> (reason)`")
            await client.say(embed=msg)
        elif helper_role in userName.roles or mod_role in userName.roles or admin_role in userName.roles or manager_role in userName.roles or owner_role in userName.roles:
            msg.add_field(name=":warning: ", value="`You can't punish other staff!`")
            await client.say(embed=msg)
        elif punished_role in userName.roles:
            msg.add_field(name=":warning: ", value="`That user is already muted!`")
            await client.say(embed=msg)
        else:
            time2 = time * 60
            if args == None:
                await client.add_roles(userName, punished_role)
                await client.remove_roles(userName, member_role)
                msg.add_field(name=":speak_no_evil: ", value="`{} has been temporarily muted by {}! for {} minute(s)!`\n`Reason: ?`".format(userName.display_name, author.display_name, time))
                await client.say(embed=msg)
                await asyncio.sleep(float(time2))
                await client.remove_roles(userName, punished_role)
                await client.say("```diff\n- Removed {}'s mute! ({} minute(s) are up.)\n```".format(userName.display_name, time))
            else:
                await client.add_roles(userName, punished_role)
                msg.add_field(name=":speak_no_evil: ", value="`{} has been muted by {} for {} minute(s)!`\n`Reason: {}`".format(userName.display_name, author.display_name, time, args))
                await client.say(embed=msg)
                await asyncio.sleep(float(time2))
                await client.remove_roles(userName, punished_role)
                await client.say("```diff\n- Removed {}'s mute! ({} minute(s) are up.)\n```".format(userName.display_name, time))
    else:
        msg.add_field(name=":warning: ", value="`This command can only be used by staff!`")
        await client.say(embed=msg)
        
# <kick <user> [reason]
@client.command(pass_context=True)
async def kick(ctx, userName: discord.Member = None, *, args = None):
    helper_role = discord.utils.get(ctx.message.server.roles, name='Helper')
    mod_role = discord.utils.get(ctx.message.server.roles, name='Moderator')
    admin_role = discord.utils.get(ctx.message.server.roles, name='Administrator')
    manager_role = discord.utils.get(ctx.message.server.roles, name='Co Owner')
    owner_role = discord.utils.get(ctx.message.server.roles, name='Owner')
    author = ctx.message.author
    msg = discord.Embed(colour=0xe3e550, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if mod_role in author.roles or admin_role in author.roles or manager_role in author.roles or owner_role in author.roles:
        if userName == None:
            msg.add_field(name=":warning: ", value="`i!kick <user> (reason)`")
        elif helper_role in userName.roles or mod_role in userName.roles or admin_role in userName.roles or manager_role in userName.roles or owner_role in userName.roles:
            msg.add_field(name=":warning: ", value="`You can't kick other staff!`")
        elif args == None:
            msg.add_field(name=":boot: Kicker", value="`{} kicked {}!`\n`Reason: ?`".format(author.display_name, userName.display_name))
            await client.kick(userName)
        else:
            msg.add_field(name=":boot: Kicker", value="`{} kicked {}!`\n`Reason: {}`".format(author.display_name, userName.display_name, args))
            await client.kick(userName)
    else:
        msg.add_field(name=":warning: ", value="`This command can only be used by Moderators, Administrators, Co Owners and Owners!`")
    await client.say(embed=msg)
    
@client.command(pass_context=True)
async def warn(ctx, userName: discord.Member = None, *, args = None):
    helper_role = discord.utils.get(ctx.message.server.roles, name='Helper')
    mod_role = discord.utils.get(ctx.message.server.roles, name='Moderator')
    admin_role = discord.utils.get(ctx.message.server.roles, name='Administrator')
    manager_role = discord.utils.get(ctx.message.server.roles, name='Co Owner')
    owner_role = discord.utils.get(ctx.message.server.roles, name='Owner')
    author = ctx.message.author
    msg = discord.Embed(colour=0xe3e550, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    msg2 = discord.Embed(colour=0xe3e550, description= "")
    msg2.title = ""
    msg2.set_footer(text=footer_text)
    if helper_role in author.roles or mod_role in author.roles or admin_role in author.roles or manager_role in author.roles or owner_role in author.roles:
        if userName == None or args == None:
            msg.add_field(name=":warning: ", value="`i!warn <user> <reason>`")
            await client.say(embed=msg)
        else:
            if helper_role in userName.roles or mod_role in userName.roles or admin_role in userName.roles or manager_role in userName.roles or owner_role in userName.roles:
                msg.add_field(name=":warning: ", value="`You cannot warn other staff!`")
                await client.say(embed=msg)
            else:
                msg2.add_field(name=":pencil: ", value="`You have been warned by {} in Limited Infinity™!`\n`Reason: {}`".format(author.display_name, args))
                msg.add_field(name=":pencil: ", value="`{} warned {}!`\n`Reason: {}`".format(author.display_name, userName.display_name, args))
                await client.say(embed=msg)
                await client.send_message(userName, embed=msg2)
    else:
        msg.add_field(name=":warning: ", value="`This command can only be used by staff!`")
        await client.say(embed=msg)
        
# }unban <user id>
@client.command(pass_context=True)
async def unban(ctx, userID = None):
    mod_role = discord.utils.get(ctx.message.server.roles, name='Moderator')
    admin_role = discord.utils.get(ctx.message.server.roles, name='Administrator')
    manager_role = discord.utils.get(ctx.message.server.roles, name='Co Owner')
    owner_role = discord.utils.get(ctx.message.server.roles, name='Owner')
    author = ctx.message.author
    msg = discord.Embed(colour=0xe3e550, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if mod_role in author.roles or admin_role in author.roles or manager_role in author.roles or owner_role in author.roles:
        if userID == None:
            msg.add_field(name=":warning: ", value="`i!unban <user id>`")
        else:
            banned_users = await client.get_bans(ctx.message.server)
            user = discord.utils.get(banned_users,id=userID)
            if user is not None:
                await client.unban(ctx.message.server, user)
                msg.add_field(name=":tools: ", value="`{} unbanned the user with the following ID: {}!`".format(author.display_name, userID))
            else:
                msg.add_field(name=":warning: ", value="`The ID you specified is not banned! ID: {}`".format(userID))
    else:
        msg.add_field(name=":warning: ", value="`This command can only be used by Moderators, Administrators, Co Owners and Owners!`")
    await client.say(embed=msg)
    print("============================================================")
    print("}unban <user>")
    print("{} ### {}".format(author, author.id))
    print("============================================================")
    
# }tempban <user> <time> [reason]
@client.command(pass_context=True)
async def tempban(ctx, userName: discord.Member = None, time: int = None, *, args = None):
    helper_role = discord.utils.get(ctx.message.server.roles, name='Moderator')
    mod_role = discord.utils.get(ctx.message.server.roles, name='Moderator')
    admin_role = discord.utils.get(ctx.message.server.roles, name='Administrator')
    manager_role = discord.utils.get(ctx.message.server.roles, name='Co Owner')
    owner_role = discord.utils.get(ctx.message.server.roles, name='Owner')
    author = ctx.message.author
    msg = discord.Embed(colour=0xe3e550, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if mod_role in author.roles or admin_role in author.roles or manager_role in author.roles or owner_role in author.roles:
        if userName == None or time == None:
            msg.add_field(name=":warning: ", value="`i!tempban <user> <time> (reason)`")
            await client.say(embed=msg)
        else:
            if helper_role in userName.roles or mod_role in userName.roles or admin_role in userName.roles or manager_role in userName.roles or owner_role in userName.roles:
                msg.add_field(name=":warning: ", value="`You can't ban other staff!`")
                await client.say(embed=msg)
            else:
                time2 = time * 60
                user_id = userName.id
                if args == None:
                    msg.add_field(name=":hammer: Ban Hammer", value="`{} banned {} for {} minute(s)!`\n`Reason: ?`".format(author.display_name, userName.display_name, time))
                    await client.say(embed=msg)
                    await client.ban(userName)
                    await asyncio.sleep(float(time2))
                    banned_users = await client.get_bans(ctx.message.server)
                    user = discord.utils.get(banned_users,id=user_id)
                    await client.unban(ctx.message.server, user)
                    await client.say("```diff\n- The user with the following ID has been unbanned: {} ({} minute(s) are up!)\n```".format(user_id, time))
                else:
                    msg.add_field(name=":hammer: Ban Hammer", value="`{} banned {} for {} minute(s)!`\n`Reason: {}`".format(author.display_name, userName.display_name, time, args))
                    await client.say(embed=msg)
                    await client.ban(userName)
                    await asyncio.sleep(float(time2))
                    banned_users = await client.get_bans(ctx.message.server)
                    user = discord.utils.get(banned_users,id=user_id)
                    await client.unban(ctx.message.server, user)
                    await client.say("```diff\n- The user with the following ID has been unbanned: {} ({} minute(s) are up!)\n```".format(user_id, time))
    else:
        msg.add_field(name=":warning: ", value="`This command can only be used by Moderators, Administrators, Co Owners and Owners!`")
        await client.say(embed=msg)
    print("============================================================")
    print("}tempban <user> <time> [reason]")
    print("{} ### {}".format(author, author.id))
    print("============================================================")
    
# }ban <user> [reason]
@client.command(pass_context=True)
async def ban(ctx, userName: discord.Member = None, *, args = None):
    helper_role = discord.utils.get(ctx.message.server.roles, name='Moderator')
    mod_role = discord.utils.get(ctx.message.server.roles, name='Moderator')
    admin_role = discord.utils.get(ctx.message.server.roles, name='Administrator')
    manager_role = discord.utils.get(ctx.message.server.roles, name='Co Owner')
    owner_role = discord.utils.get(ctx.message.server.roles, name='Owner')
    author = ctx.message.author
    msg = discord.Embed(colour=0xe3e550, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if mod_role in author.roles or admin_role in author.roles or manager_role in author.roles or owner_role in author.roles:
        if userName == None:
            msg.add_field(name=":warning: ", value="`i!ban <user> (reason)`")
        elif helper_role in userName.roles or mod_role in userName.roles or admin_role in userName.roles or manager_role in userName.roles or owner_role in userName.roles:
            msg.add_field(name=":warning: ", value="`You can't ban other staff!`")
        elif args == None:
            msg.add_field(name=":hammer: Ban Hammer", value="`{} banned {}!`\n`Reason: ?`".format(author.display_name, userName.display_name))
            await client.ban(userName)
        else:
            msg.add_field(name=":hammer: Ban Hammer", value="`{} banned {}!`\n`Reason: {}`".format(author.display_name, userName.display_name, args))
            await client.ban(userName)
    else:
        msg.add_field(name=":warning: ", value="`This command can only be used by Moderators, Administrators, Co Owners and Owners!`")
    await client.say(embed=msg)
    print("============================================================")
    print("}ban <user> [reason]")
    print("{} ### {}".format(author, author.id))
    print("============================================================")
    
# }rps <rock/paper/scissors>
@client.command(pass_context=True)
async def rps(ctx, args=None):
    choice = random.choice(choices)
    author = ctx.message.author
    msg = discord.Embed(colour=0xe3e550, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if args == None:
        msg.add_field(name=":warning: ", value="`i!rps <rock/paper/scissors>`")
    elif args == "rock" or args == "paper" or args == "scissors":
        msg.add_field(name=":fist: :raised_hand: :v: ROCK PAPER SCISSORS :v: :raised_hand: :fist: ", value="**~~=================================~~**\n:arrow_forward: `{}`: {}\n:arrow_forward: `BOT`: {}\n**~~=================================~~**".format(author.display_name, args, choice), inline=True)
        if args == "rock" and choice == "scissors":
            msg.add_field(name=":diamonds: W I N N E R :diamonds: ", value="`{}`\n**~~=================================~~**".format(author.display_name), inline=True)
        elif args == "paper" and choice == "rock":
            msg.add_field(name=":diamonds: W I N N E R :diamonds: ", value="`{}`\n**~~=================================~~**".format(author.display_name), inline=True)
        elif args == "scissors" and choice == "paper":
            msg.add_field(name=":diamonds: W I N N E R :diamonds: ", value="`{}`\n**~~=================================~~**".format(author.display_name), inline=True)
        elif args == "rock" and choice == "paper":
            msg.add_field(name=":diamonds: W I N N E R :diamonds: ", value="`BOT`\n**~~=================================~~**", inline=True)
        elif args == "paper" and choice == "scissors":
            msg.add_field(name=":diamonds: W I N N E R :diamonds: ", value="`BOT`\n**~~=================================~~**", inline=True)
        elif args == "scissors" and choice == "rock":
            msg.add_field(name=":diamonds: W I N N E R :diamonds: ", value="`BOT`\n**~~=================================~~**", inline=True)
        elif args == "rock" and choice == "rock":
            msg.add_field(name=":diamonds: W I N N E R :diamonds: ", value="It's a tie!\n**~~=================================~~**", inline=True)
        elif args == "paper" and choice == "paper":
            msg.add_field(name=":diamonds: W I N N E R :diamonds: ", value="It's a tie!\n**~~=================================~~**", inline=True)
        else:
            msg.add_field(name=":diamonds: W I N N E R :diamonds: ", value="It's a tie!\n**~~=================================~~**", inline=True)
    else:
        msg.add_field(name=":warning: ", value="`i!rps <rock/paper/scissors>`")
    await client.say(embed=msg)
    print("============================================================")
    print("}rps <rock/paper/scissors>")
    print("{} ### {}".format(author, author.id))
    print("============================================================")
    
choices = ["rock", "paper", "scissors"]

# <battle <user>
@client.command(pass_context=True)
async def battle(ctx, userName: discord.Member = None):
    attacker = random.randint(0, 301)
    attacked = random.randint(0, 301)
    attackerhealth = 300 - attacked
    attackedhealth = 300 - attacker
    author = ctx.message.author
    msg = discord.Embed(colour=0xe3e550, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if userName == None:
        msg.add_field(name=":warning: ", value="`i!battle <user>`")
    else:
        msg.add_field(name= ":crossed_swords: B A T T LE :crossed_swords: ", value= "**~~=================================~~**\n`{}` :vs: `{}`\n**~~=================================~~**\n:small_orange_diamond: `{}`\n \n:arrow_forward: {}\n \n:fast_forward: {} DMG\n**~~=================================~~**\n:small_orange_diamond: `{}`\n \n:arrow_forward: {}\n \n:fast_forward: {} DMG\n**~~=================================~~**\n:small_orange_diamond: `{}`\n:hearts: {} HP\n \n:small_orange_diamond: `{}`\n:hearts: {} HP\n**~~=================================~~**".format(author.display_name, userName.display_name, author.display_name, random.choice(attacks), attacker, userName.display_name, random.choice(attacks), attacked, author.display_name, attackerhealth, userName.display_name, attackedhealth), inline=True)
        if attacker == attacked:
            msg.add_field(name= ":diamonds: N O  W I N N E R :diamonds:", value= "**~~=================================~~**\n`{}`\n`{}`\n**~~=================================~~**".format(author.display_name, userName), inline=True)
        elif attacker > attacked:
            msg.add_field(name= ":diamonds: W I N N E R :diamonds:", value= "**~~=================================~~**\n`{}`\n**~~=================================~~**".format(author.display_name), inline=True)
        else:
            msg.add_field(name= ":diamonds: W I N N E R :diamonds:", value= "**~~=================================~~**\n`{}`\n**~~=================================~~**".format(userName.display_name), inline=True)
    await client.say(embed=msg)
    print("============================================================")
    print("}battle <user>")
    print("{} ### {}".format(author, author.id))
    print("============================================================")

attacks = ["Punches the opponent :punch: ", "Kicks the opponent :boot: ", "Throws the opponent :raised_hands: ", "Stabs the opponent :dagger: ", "Shoots the opponent :gun: ",
           "Sets the opponent on fire :fire: ", "Poisons the opponent :syringe: ", "Throws a bomb at the opponent :bomb: ", "Uses a shield to deal damage with the same attack as the opponent's :shield: ", "Chokes the opponent using chains :chains: ",
           "Cuts the opponent :knife: ", "Hits the opponent's head with a hammer :hammer: ", "Uses dark magic to attack the opponent :skull_crossbones: ", "Casts a spell on the opponent :sparkles: ", "Pukes at the opponent :nauseated_face: ",
           "Scares the opponent :ghost: ", "Summons a demon to attack the opponent :smiling_imp: ", "Transforms into a robot to attack the opponent :robot: ", "Farts at the opponent :dash: ", "Summons a tornado near the opponent :cloud_tornado: ",
           "Summons a meteor and hits the opponent with it :comet: ", "Hits the opponent with lightning :zap: ", "Freezes the opponent :snowflake: ", "Cripples the opponent :boom: ", "Shoots the opponent using a bow and arrow :bow_and_arrow: ",
           "Drives over the opponent :red_car: ", "Chops off the opponent's leg :crossed_swords: ", "Drains some of the opponent's life :broken_heart: ", "Steals the opponent's soul :black_heart: ", "Stuns the opponent :octagonal_sign: ",
           "Uses nuclear energy to attack the opponent :radioactive: ", "Blinds the opponent :eye: ", "Deafens the opponent :ear: ", "Uses mind control on the opponent :alien: ", "Summons minions to attack the opponent :busts_in_silhouette: ",
           "Traps the opponent :spider_web: "] 

# }embed <title> <description> <field name> <field value> <footer>
@client.command(pass_context=True)
async def embed(ctx, title = None, desc = None, name = None, value = None, footer = None):
    admin_role = discord.utils.get(ctx.message.server.roles, name='Administrator')
    manager_role = discord.utils.get(ctx.message.server.roles, name='Co Owner')
    owner_role = discord.utils.get(ctx.message.server.roles, name='Owner')
    author = ctx.message.author
    if admin_role in author.roles or manager_role in author.roles or owner_role in author.roles:
        if title == None or desc == None or name == None or value == None or footer == None:
            msg = discord.Embed(colour=0xe3e550, description= "")
            msg.title = ""
            msg.set_footer(text=footer_text)
            msg.add_field(name=":warning: ", value="`i!embed <title> <description> <field name> <field value> <footer>`")
        else:
            msg = discord.Embed(colour=0xe3e550, description= "{}".format(desc))
            msg.title = "{}".format(title)
            msg.set_footer(text="{}".format(footer))
            msg.add_field(name="{}".format(name), value="{}".format(value))
    else:
        msg = discord.Embed(colour=0x210150, description= "")
        msg.title = ""
        msg.set_footer(text=footer_text)
        msg.add_field(name=":warning: ", value="`This command can only be used by Administrators, Co Owners and Owners!`")
    await client.say(embed=msg)
    print("============================================================")
    print("}embed <title> <description> <field name> <field value> <footer>")
    print("{} ### {}".format(author, author.id))
    print("============================================================")
    
# EVENT - JOIN / LEAVE
@client.async_event
async def on_member_join(member):
    msg = "Welcome to {1}! 🎉 {0}. Make sure to read <#446594082731720705> and get some roles in <#448456540597256192> feel free to DM the owner for queries and enjoy your stay here 😉 ".format(member.mention, member.server.name)
    channel = discord.utils.get(id="446349220149198859", client.get_all_channels())
    await client.send_message(channel, msg))
    print("============================================================")
    print("JOIN EVENT")
    print("{} ### {}".format(userName, userName.id))
    print("============================================================")
client.run(os.environ['BOT_TOKEN'])
