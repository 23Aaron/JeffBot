from discord.ext import commands
import discord, asyncio, logging, json
bot = commands.Bot(command_prefix="!")

# Role ID Dictionary
platformDict = {"ios":291627102627823617, "macos":291627249768202240, "tvos":291627141982978059, "watchos":291627182365605890}

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

    transformDict = {"db":"Developer Beta", "pb":"Public Beta"}

    if platform.lower() in platformDict:
        role = platformDict[platform.lower()]

    roles = discord.utils.get(ctx.message.author.server.roles, id=str(role))

    if beta.lower() in transformDict:
        betas = transformDict[beta.lower()]
        
    platform = capitaliseOS(platform)

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
async def update(ctx):

    updateString = ""

    for platform in platformDict:
        role = discord.utils.get(ctx.message.author.server.roles, id= str(platformDict[platform]))

        await bot.edit_role(ctx.message.author.server, role, mentionable = True)

        updateString = updateString + " " + role.mention

    updateString = updateString + ", a new update has been released!"
    await bot.send_message(discord.Object(id="538268186198409227"), updateString)

    for platform in platformDict:
        role = discord.utils.get(ctx.message.author.server.roles, id= str(platformDict[platform]))

        await bot.edit_role(ctx.message.author.server, role, mentionable = False)

async def deleteWait(msg):
    await asyncio.sleep(6)
    await bot.delete_message(msg) 

async def getRoleID(platform):
    platformDict = {"ios":291627102627823617, "macos":291627249768202240, "tvos":291627141982978059, "watchos":291627182365605890}
    
    if platform.lower() in platformDict:
        return platformDict[platform.lower()]

async def capitaliseOS(msg):
    msg = msg.replace("o", "O")
    msg = msg.replace("s", "S")

    return msg

bot.run("YOUR_TOKEN_HERE")    
