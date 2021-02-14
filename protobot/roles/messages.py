from discord import Embed, Member, Role
from discord.ext.commands import Context
from discord.utils import get


def get_friend_color(ctx: Context):
    role: Role = get(ctx.guild.roles, name='Friends')
    return role.color


def friend_request(ctx: Context, member: Member):
    author = ctx.author
    return Embed(title="Friend Request",
                 description=f"<@{author.id}> would like to give `friend` to <@{member.id}>",
                 color=get_friend_color(ctx))
