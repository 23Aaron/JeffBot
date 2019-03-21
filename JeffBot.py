from discord.ext import commands
import discord, asyncio, logging, json
bot = commands.Bot(command_prefix="!")

@bot.event
async def on_ready():
    print("Ready to go!")

@bot.command(pass_context=True)
async def hello(ctx):
    await bot.say("Hello!")

@bot.command(pass_context=True)
async def moo(ctx):
    await bot.say("Moo big gey.")  

@bot.command(pass_context=True)
async def announcements(ctx):
    user = ctx.message.author
    role = discord.utils.get(user.server.roles, name="Announcements")
    await bot.add_roles(user, role)      
     
    embed = discord.Embed(
        title = "**Role Given!**",
        description = "You're now subscribed to server updates and other announcements!",
        colour = 0xffffff
    )

    msg = await bot.say(embed=embed)
    await deleteWait(msg)

@bot.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def post(ctx, platform, version: float, beta, betaversion):
    if (platform.lower() == "ios"):  
        role = 291627102627823617
    elif (platform.lower() == "macos"):
        role =  291627249768202240
    elif (platform.lower() == "tvos"):
        role = 291627141982978059
    elif (platform.lower() == "watchos"):
        role = 291627182365605890
    roles = discord.utils.get(ctx.message.author.server.roles, id=str(role))
    if(beta.lower() == "db"):
        betas = "Developer Beta"
    if(beta.lower() == "pb"):
        betas = "Public Beta"
    if(platform == "ios"):
        platform = "iOS"
    if(platform == "tvos"):
        platform = "tvOS"
    if(platform == "macos"):
        platform = "macOS"
    if(platform == "watchos"):
        platform = "watchOS"
    await bot.edit_role(ctx.message.author.server, roles, mentionable = True)
    await bot.send_message(discord.Object(id="538268186198409227"), "{} {} {} {} {} has been released!".format(roles.mention, platform, str(version), betas, str(betaversion)))
    await bot.edit_role(ctx.message.author.server, roles, mentionable = False)

@bot.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def full(ctx, platform, version: float):
    if (platform.lower() == "ios"):  
        role = 291627102627823617
    elif (platform.lower() == "macos"):
        role = 291627249768202240
    elif (platform.lower() == "tvos"):
        role = 291627141982978059
    elif (platform.lower() == "watchos"):
        role = 291627182365605890
    roles = discord.utils.get(ctx.message.author.server.roles, id=str(role))
    if(platform == "ios"):
        platform = "iOS"
    if(platform == "tvos"):
        platform = "tvOS"
    if(platform == "macos"):
        platform = "macOS"
    if(platform == "watchos"):
        platform = "watchOS"
    await bot.edit_role(ctx.message.author.server, roles, mentionable = True)
    await bot.send_message(discord.Object(id="538268186198409227"), "{} {} {} has been released!".format(roles.mention, platform, str(version)))
    await bot.edit_role(ctx.message.author.server, roles, mentionable = False)

@bot.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def update(ctx, version: float):
    ios = discord.utils.get(ctx.message.author.server.roles, id=str(291627102627823617))
    macos = discord.utils.get(ctx.message.author.server.roles, id=str(291627249768202240))
    tvos = discord.utils.get(ctx.message.author.server.roles, id=str(291627141982978059))
    watchos = discord.utils.get(ctx.message.author.server.roles, id=str(291627182365605890))
    await bot.edit_role(ctx.message.author.server, ios, mentionable = True)
    await bot.edit_role(ctx.message.author.server, macos, mentionable = True)
    await bot.edit_role(ctx.message.author.server, tvos, mentionable = True)
    await bot.edit_role(ctx.message.author.server, watchos, mentionable = True)
    await bot.send_message(discord.Object(id="538268186198409227"), "{} {} {} {}, a new update has been released!".format(ios.mention, macos.mention, tvos.mention, watchos.mention))
    await bot.edit_role(ctx.message.author.server, ios, mentionable = False)
    await bot.edit_role(ctx.message.author.server, macos, mentionable = False)
    await bot.edit_role(ctx.message.author.server, tvos, mentionable = False)
    await bot.edit_role(ctx.message.author.server, watchos, mentionable = False)

async def deleteWait(msg):
    await asyncio.sleep(6)
    await bot.delete_message(msg) 

bot.run("YOUR_TOKEN_HERE")    
