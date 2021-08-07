# **P**ython **D**iscord **B**ot **W**ith **M**ongo**DB** **S**tarter **P**ack
**Credits to EQUENOS**

Hello! If you've decided to create a Python 3 Discord Bot with MongoDB, this repository will save you time.
It provides for caching data from the database to reduce the use of RAM.

You can customize the configuration of your bot using the `config.json` file in the `json` folder.
You can also specify tokens and databases for the main bot and for the debug bot.
## Tutorial
First, you have to create a cluster and a database in [MongoDB](https://www.mongodb.com/) and paste the following things into the config file:
• Cluster URL (it can be found by clicking on the Connect button → Connect your application), example: `clustername.abcde.mongodb.net`;
• Username and password (it can be created on the Database Access tab);
• Database name (it can be created by clicking on the cluster name and choosing the Collections tab).

Next, in the `cache.py` file, you need to create cached collections that will be used in cogs. There is an example of usage in the file.
Paste your bot token into the config file. If you have a debugging bot, also paste its token. To enable debug mode, just change `debug_mode` to `true`.

### Cogs
Each cog must import all from `cache.py` (`from cache import *`) to work with cached data. There is also an example of use.

### Other from config file
`owner_ids` is an int array with a bot's owner ID. Only they can use special commands like `eval`.
`shard_count` determines how many shards a bot will have. If it is located on a small number of servers, you can leave 1. **It's not recommended to specify too many shards**.
`default_prefixes` – I think it's clear what it is.

### How to launch my bot?
In `requirements.txt`, you need to specify the third-party libraries that your bot uses. **Please do not delete the existing ones - they are needed for the bot to work correctly!**
#### Heroku
Create a **private** Github repository and put your bot files there. Then create a new app on Heroku, connect your Github and deploy branch on the Deploy tab. Turn on the switch on the Resources tab. Voila!
#### Your PC or other servers
Install all libraries from the `requirements.txt` file using the `pip install -r requirements.txt`. Then start the bot using the `python3 main.py` command.
