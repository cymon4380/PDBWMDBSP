import discord
from discord.ext import commands
import json
import os
import cache
import pymongo

with open("json/config.json", "r", encoding="utf-8") as f:
    config = json.load(f)

client = commands.AutoShardedBot(command_prefix=config["default_prefixes"], shard_count=config["shard_count"])
client.remove_command(help)

cpath = "release"
if config["debug_mode"]:
    cpath = "debug"

# Loading cogs
for file in os.listdir("./cogs"):
    if file.endswith(".py"):
        client.load_extension(f"cogs.{file[:-3]}")
        print("Cog loaded:", file[:-3])

@client.event
async def on_ready():
    print("The bot is ready.")

# Error handler
@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        return
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Too few arguments.")
    else:
        raise error

# Run
client.run(config[cpath]["bot_token"])