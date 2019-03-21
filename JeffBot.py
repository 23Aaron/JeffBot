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

    platformDict = {"ios":291627102627823617, "macos":291627249768202240, "tvos":291627141982978059, "watchos":291627182365605890}
    transformDict = {"db":"Developer Beta", "pb":"Public Beta"}

    if platform.lower() in platformDict:
        role = platformDict[platform.lower()]

    roles = discord.utils.get(ctx.message.author.server.roles, id=str(role))

    if beta.lower() in transformDict:
        betas = transformDict[beta.lower()]

    # Capitalise "OS"

    platform = platform.replace("o", "O")
    platform = platform.replace("s", "S")

    await bot.edit_role(ctx.message.author.server, roles, mentionable = True)
    await bot.send_message(discord.Object(id="538268186198409227"), "{} {} {} {} {} has been released!".format(roles.mention, platform, str(version), betas, str(betaversion)))
    await bot.edit_role(ctx.message.author.server, roles, mentionable = False)

@@bot.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def full(ctx, platform, version: float):


    platform = platform.lower()
    role = getRoleID(platform)

    roles = discord.utils.get(ctx.message.author.server.roles, id=str(role))
    
    platform = capitaliseOS(platform)

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
