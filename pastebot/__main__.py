import configparser
import inspect
import logging
import os
import urllib.parse
import urllib.request

from discord.ext import commands

logging.basicConfig(format="%(asctime)s %(levelname)s:%(message)s", datefmt="%m/%d/%Y %H:%M:%S",
                     filename="pastebot.log", level=logging.INFO)
path = os.path.dirname(os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))))
config = configparser.SafeConfigParser()
config.read(os.path.join(path, "config.txt"))
desc = 'A simple bot that creates pastebin pastes of long messages (e.g. code snippets and errors)'
bot = commands.Bot(command_prefix='thereAreNoCommands', description=desc)


@bot.event
async def on_ready():
    logging.info("The bot has been initialized.")


@bot.listen()
async def on_message(message):
    content = message.content
    channel = message.channel
    author = message.author
    if not author.bot and len(content) > config.getint("SETTINGS", "max_message_length"):
        codeBlock = "```"
        if content.startswith(codeBlock) and content.endswith(codeBlock):
            content = content[len(codeBlock):-len(codeBlock)]
        min_length = config.getint("SETTINGS", "preview_min_length")
        first = content[:min_length]
        result = pastebin.paste(paste_code=content, paste_name=author.display_name + "'s message").decode("utf-8")
        if "https://" in result:
            logging.info("Created a new paste of " + author.display_name + "'s message: " + result)
            await bot.send_message(channel, "[Long message] " + first + "... \nBy: " + author.display_name + "\n " + result)
            await bot.delete_message(message)
        else:
            logging.warning("Failed to create a new paste: " + result)


class Pastebin:

    def __init__(self, api_dev_key):
        self.api_dev_key = api_dev_key

    def paste(self, paste_code, paste_name):
        params = dict(
            api_option='paste',
            api_dev_key=self.api_dev_key,
            api_paste_code=paste_code,
            api_paste_name=paste_name,
            api_paste_expire_date=config.get("SETTINGS", "paste_expire"),
            api_paste_private=config.getint("SETTINGS", "private_paste")
            )
        with urllib.request.urlopen('https://pastebin.com/api/api_post.php', urllib.parse.urlencode(params).encode('utf-8')) as response:
            return response.read()


pastebin = Pastebin(api_dev_key=config.get("SETTINGS", "api_dev_key"))
bot.run(config.get("SETTINGS", "bot_token"))
