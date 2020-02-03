import discord
from discord.ext import commands
import discord.utils
import asyncio
bot = commands.Bot(command_prefix='$')
blacklist_array = []
@bot.event
async def on_ready():
    """Start of bot"""
    print('Bot is starting up!!')
    print(f'Logged in as {bot.user.name}')
    game = discord.Game("Watching Akanate Build Me")
    await bot.change_presence(status=discord.Status.idle, activity=game)

@bot.event
async def on_message(message):
    try:
        ctx = message
        global blacklist_array
        if ctx.author.id in blacklist_array:
            await ctx.delete()
            embed=discord.Embed(title="Blacklisted", description="You have been Blacklisted", color=0xf91b0b)
            embed.set_thumbnail(url="")
            await ctx.channel.send(embed=embed,delete_after=2)
        if "blacklisted" in [y.name.lower() for y in message.author.roles]:
            await ctx.delete()
            embed=discord.Embed(title="Blacklisted", description="You have been Blacklisted", color=0xf91b0b)
            embed.set_thumbnail(url="https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/120/microsoft/209/warning-sign_26a0.png")
            await ctx.channel.send(embed=embed,delete_after=2)
        await bot.process_commands(message)
    except AttributeError:
        return



@bot.command(aliases=['fbl'])
@commands.has_permissions(manage_roles=True, ban_members=True)
async def forced_blacklist(ctx,user: discord.Member):
    """Blacklist command"""
    global blacklist_array
    if user.id == 673621718719529021:
        return
    if user.id in blacklist_array:
        embed=discord.Embed(title=f"{user.name} is already blacklisted", description="The user is already blacklisted", color=0xf9e90b)
        embed.set_thumbnail(url="https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/120/microsoft/209/warning-sign_26a0.png")
        await ctx.send(embed=embed)
        return
    blacklist_array.append(user.id)
    embed=discord.Embed(title="Added to Blacklist", description="The user has been added to the blacklist", color=0xf9e90b)
    embed.set_thumbnail(url="https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/60/whatsapp/238/thumbs-up-sign_1f44d.png")
    await ctx.send(embed=embed)
@commands.has_permissions(manage_roles=True, ban_members=True)
@bot.command(aliases=['fbl_remove'])
async def forcedblacklist_remove(ctx,user: discord.Member):
    global blacklist_array
    for e in range (len(blacklist_array)):
        for i in blacklist_array:
            if i == user.id:
                blacklist_array.pop(e)
                embed=discord.Embed(title="Removed from blacklist", description="The user has been removed from the blacklist", color=0xf9e90b)
                embed.set_thumbnail(url="https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/60/whatsapp/238/thumbs-up-sign_1f44d.png")
                await ctx.send(embed=embed)
            else:
                embed=discord.Embed(title="Error User not found", color=0xf9e90b)
                embed.set_thumbnail(url="https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/120/microsoft/209/warning-sign_26a0.png")
                await ctx.send(embed=embed)
@bot.command()
async def blacklist(ctx,user: discord.Member):
    role = discord.utils.find(lambda r: r.id == 673649755485634631,ctx.message.guild.roles)
    user.add_role(role)
    embed=discord.Embed(title="Blacklist role added", color=0xf9e90b)
    embed.set_thumbnail(url="https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/120/microsoft/209/warning-sign_26a0.png")
    await ctx.send(embed=embed)


@forced_blacklist.error
async def error_blacklist(ctx):
    embed=discord.Embed(title="Don't do that", description="You are not allowed to use that command", color=0xf91b0b)
    embed.set_thumbnail(url="https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/120/microsoft/209/warning-sign_26a0.png")
    await ctx.send(embed=embed)

bot.run(token)
