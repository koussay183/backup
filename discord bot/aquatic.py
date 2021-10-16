from discord.ext import commands
import discord

bot = commands.Bot(command_prefix='!')

# truth or dare game =====
@commands.command()
async def games(ctx ,*gamename):
    await ctx.send("tod : Truth Or Dare Tunisian Version\n==========\nTo Play Use\n====================\n!games tod (+18 or -18) players name\n====================\nexemple : !games tod +18 ali oussema")
    

bot.add_command(games)
# =======================
bot.run('ODIxMzI0Mjg4NzMyNTYxNDA5.YFCD2Q.SXx6-G7kaaIlb4S17tejWsXhbsg')
