from discord.ext import commands
from os import environ
from protobot.roles.commands import friend

bot = commands.Bot(command_prefix='pt!')

bot.add_command(friend)

def start():
    token = environ.get('TOKEN')
    bot.run(token)

if __name__ == '__main__':
    start()