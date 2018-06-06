import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='?', description='This is description')
	
@bot.event
async def on_ready():
	print('------')
	print("Logged in")
	print(bot.user.name)
	print('------')

@bot.command()
async def heart(ctx):
    await ctx.send('I heard you! {0} :heart_eyes: :heart_eyes: '.format(ctx.author))
	
@bot.command()
async def info(ctx):
    embed = discord.Embed(title="BlowMice Discord", description="XD", color=0xffffff)
    embed.add_field(name="Author", value="Adryan")
    embed.add_field(name="Invite", value="https://discordapp.com/oauth2/authorize?client_id=453621483923832836&scope=bot&permissions=52224")

    await ctx.send(embed=embed)

bot.run("NDUzNjIxNDgzOTIzODMyODM2.Dfhy_A.UbmwvvxsWDZAIftZcjnWL3g8wmc")


#color=0xffffff --> Color bar

#https://discordapp.com/oauth2/authorize?client_id=453621483923832836&scope=bot&permissions=52224