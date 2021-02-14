from discord import Member, Member
from discord.ext.commands import Context
from discord.utils import get

from protobot.roles.utils import get_role

async def can_give_friend(ctx: Context):
    return any(get_role(ctx, name=role) in ctx.author.roles for role in ("Admin", "Member"))

def can_grant_friend(ctx: Context, user: Member):
    return any(get_role(ctx, name=role) in user.roles for role in ("Admin", "Discord Mod"))

def can_have_friend(ctx: Context, member: Member):
    return not get_role(ctx, name="Friends") in member.roles