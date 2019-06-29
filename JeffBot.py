from discord.ext import commands
import discord, asyncio, logging, json
bot = commands.Bot(command_prefix="!")

# Role ID Dictionary
platformDict = {"ios":291627102627823617, "macos":291627249768202240, "tvos":291627141982978059, "watchos":291627182365605890, "ipados":585506894240546817, "xcode":590944120252661770}

@bot.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def setgame(ctx):
    mygame = discord.Game(name="Firing Jony Ive...")
    await bot.change_presence(activity=mygame)

@bot.event
async def on_ready():
    print("Ready to go!")

@bot.command(pass_context=True)
async def hello(ctx):
    await ctx.send("Hello!")

@bot.command(pass_context=True)
async def moo(ctx):
    await ctx.send("Moo big gey.")  

@bot.command(pass_context=True)
async def announcements(ctx):
    member = ctx.message.author
    role = discord.utils.get(member.guild.roles, name="Announcements")
    await member.add_roles(role)      
     
    embed = discord.Embed(
        title = "**Role Given!**",
        description = "You're now subscribed to server updates and other announcements!",
        colour = 0xffffff
    )

    msg = await ctx.send(embed=embed)
    await deleteWait(msg)

@bot.command(pass_context=True)
@commands.has_permissions(manage_messages=True)
async def beta(ctx, platform, version, beta, betaversion):

    transformDict = {"db":"Developer Beta", "pb":"Public Beta"}

    if platform.lower() in platformDict:
        role = platformDict[platform.lower()]

    if beta.lower() in transformDict:
        betas = transformDict[beta.lower()]

    platform = capitaliseOS(platform)

    guild = ctx.guild

    roleObj = guild.get_role(role)

    channel = guild.get_channel(538268186198409227)

    await roleObj.edit(mentionable = True)
    await channel.send("{} {} {} {} {} has been released!".format(roleObj.mention, platform, str(version), betas, str(betaversion)))
    await roleObj.edit(mentionable = False)

@bot.command(pass_context=True)
@commands.has_permissions(manage_messages=True)
async def update(ctx, platform, version):

    guild = ctx.guild

    platform = platform.lower()

    role = getRoleID(platform)
    
    platform = capitaliseOS(platform)

    roleObj = guild.get_role(role)

    channel = guild.get_channel(538268186198409227)

    await roleObj.edit(mentionable = True)
    await channel.send("{} {} {} has been released!".format(roleObj.mention, platform, str(version)))
    await roleObj.edit(mentionable = False)

async def deleteWait(msg):
    await asyncio.sleep(6)
    await msg.delete 

def getRoleID(platform):
    platformDict = {"ios":291627102627823617, "macos":291627249768202240, "tvos":291627141982978059, "watchos":291627182365605890, "ipados":585506894240546817, "xcode":590944120252661770}
    
    if platform.lower() in platformDict:
        return platformDict[platform.lower()]

def capitaliseOS(msg):
    msg = msg.replace("os", "OS")
    msg = msg.replace("ipad", "iPad")
    msg = msg.replace("xcode", "Xcode")

    return msg

bot.run("YOUR_TOKEN_HERE")    
