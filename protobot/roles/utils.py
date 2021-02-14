from discord import Role, Member, Guild
from discord.ext.commands import Context, Bot
from discord.utils import get

def get_role(ctx: Context, **kwargs) -> Role:
    return get(ctx.guild.roles, **kwargs)

def get_member(ctx: Context, **kwargs) -> Member:
    return get(ctx.guild.members, **kwargs)

def request_channel(ctx: Context):
    return get(ctx.guild.text_channels, name="role-requests")

def bot(ctx: Context) -> Bot:
    return ctx.bot