import discord
from discord.ext import commands
from cache import * # Required
import helper

class Example(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def hello(self, ctx):
        await ctx.send("Hello, {}!".format(ctx.author.mention))

    @commands.command()
    @commands.check(helper.is_owner)
    async def secret(self, ctx):
        await ctx.send("Hello, my owner!")

    @commands.command()
    async def points(self, ctx):
        if not ctx.author.id in testdata:
            amount = 0
        else:
            amount = testdata[ctx.author.id]["amount"]
        await ctx.send(f"You have {amount} points.")

    @commands.command()
    @commands.check(helper.is_owner)
    async def setpoints(self, ctx, user: discord.User, amount: int):
        if amount == 0:
            test.remove(user.id)
        else:
            test.add(user.id, {"amount": amount})
        await ctx.message.add_reaction("✅")

def setup(bot):
    bot.add_cog(Example(bot))