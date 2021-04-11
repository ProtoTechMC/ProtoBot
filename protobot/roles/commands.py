from discord import Member, Message, TextChannel, Guild, Reaction
from discord.ext import commands
from discord.ext.commands import Context, Bot
from discord.utils import get

from protobot.roles.checks import can_give_friend, can_grant_friend, can_have_friend
from protobot.roles.messages import friend_request
from protobot.roles.utils import request_channel, bot, get_role

from random import randint


@commands.command()
@commands.check(can_give_friend)
async def friend(ctx: Context, member: Member):
    message: Message = ctx.message

    if not can_have_friend(ctx, member):
        await message.add_reaction('👎')
        return
        
    await message.add_reaction('👍')

    requests: TextChannel = request_channel(ctx)
    request = await requests.send(embed=friend_request(ctx, member))
    await request.add_reaction('✅')
    await request.add_reaction('❎')
    await add_troll_face(ctx, request)

    def check(reaction: Reaction, user: Member):
        emoji = str(reaction.emoji)
        return (reaction.message == request
                and user != request.author
                and can_grant_friend(ctx, user)
                and emoji in ('✅', '❎'))

    reaction, _ = await bot(ctx).wait_for('reaction_add', check=check)
    emoji = str(reaction.emoji)
    if(emoji == '✅'):
        await member.add_roles(get_role(ctx, name="Friends"))
        await message.add_reaction('✅')
    else:
        await message.add_reaction('❎')
    
    await request.add_reaction('👍')
    

@commands.command()
@commands.check(can_give_friend)
async def friend(ctx: Context, member: Member):
    message: Message = ctx.message

    if not can_have_friend(ctx, member):
        await message.add_reaction('👎')
        return
        
    await message.add_reaction('👍')

    requests: TextChannel = request_channel(ctx)
    request = await requests.send(embed=friend_request(ctx, member))
    await request.add_reaction('✅')
    await request.add_reaction('❎')
    await add_troll_face(ctx, request)

    def check(reaction: Reaction, user: Member):
        emoji = str(reaction.emoji)
        return (reaction.message == request
                and user != request.author
                and can_grant_friend(ctx, user)
                and emoji in ('✅', '❎'))

    reaction, _ = await bot(ctx).wait_for('reaction_add', check=check)
    emoji = str(reaction.emoji)
    if(emoji == '✅'):
        await member.add_roles(get_role(ctx, name="Friends"))
        await message.add_reaction('✅')
    else:
        await message.add_reaction('❎')
    
    await request.add_reaction('👍')

async def add_troll_face(ctx, request):
    emoji = bot(ctx).get_emoji(324039959873060875)
    if emoji is not None:
        await request.add_reaction(emoji)
