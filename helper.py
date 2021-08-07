import json

with open("json/config.json", "r", encoding="utf-8") as f:
    config = json.load(f)

async def is_owner(ctx):
    if not ctx.author.id in config["owner_ids"]:
        await ctx.send("This command is only available to bot owners!")
        return False
    return True