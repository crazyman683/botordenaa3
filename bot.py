import discord

from discord.ext import commands
import random
import asyncio
from discord import Activity, ActivityType



#vasno
intens = discord.Intents.all()

client = commands.Bot(command_prefix="†", intents=intens)

@client.event
async def on_ready():
                print("Bot is ready to work")
                await client.change_presence(status=discord.Status.idle,activity=Activity(name="Ave ordinu",type=ActivityType.watching))





@client.command()
@commands.has_permissions(view_audit_log=True)
async def kick(ctx,member:discord.Member,reason):
        emb = discord.Embed(title='Kick', color=0xff0000)
        emb.add_field(name='Moderator', value=ctx.message.author.mention)
        emb.add_field(name='Impostor', value=member.mention)
        emb.add_field(name='Reason', value=reason)
        await member.kick()



@client.command()
async def info(ctx,member:discord.Member):
    emb = discord.Embed(title= 'Информация пользователя' ,color=0xff0000)
    emb.add_field(name= 'Когда присоединился:',value=member.joined_at.strftime("%H:%M:%S"))

    emb.add_field(name= 'Имя:', value=member.display_name)
    emb.add_field(name= 'ID:', value=member.id)
    emb.add_field(name= 'Аккаунт был создан:',value=member.created_at.strftime("%a,%#d %B %Y, %I:%M %p UTC"))
    emb.set_thumbnail(url=member.avatar_url)
    emb.set_footer(text=f"Вызвано:{ctx.message.author}",icon_url=ctx.message.author.avatar_url)
    emb.set_author(name=ctx.message.author,icon_url=ctx.message.author.avatar_url)
    await ctx.send(embed = emb)


@client.command()
@commands.has_permissions(view_audit_log=True)
async def mute(ctx,member:discord.Member,time:int,reason):
    muterole = discord.utils.get(ctx.guild.roles,id=840181562297679912)
    emb = discord.Embed(title='Mute',color=0xff0000)
    emb.add_field(name='Moderator', value=ctx.message.author.mention)
    emb.add_field(name='Impostor', value=member.mention)
    emb.add_field(name='Reason', value=reason)
    emb.add_field(name='Time', value=time)
    await member.add_roles(muterole)
    await ctx.send(embed=emb)
    await asyncio.sleep(time * 60)
    await member.remove_roles(muterole)


@client.command()
@commands.has_permissions(view_audit_log=True)
async def ban(ctx,member:discord.Member, reason):
    emb = discord.Embed(title='Kick', color=0xff0000)
    emb.add_field(name='Moderator', value=ctx.message.author.mention)
    emb.add_field(name='Impostor', value=member.mention)
    emb.add_field(name='Reason', value=reason)
    await member.ban()

@client.command()
@commands.has_permissions(view_audit_log=True)
async def clear(ctx, amount=10):
    deleted = await ctx.message.channel.purge(limit=amount)

@client.event
async def on_member_join(member):
                print(f" {member} Добро пожаловать")
                async def on_member_remove(member):
                                print(f'{member} Пока')

@client.command()
async def help_me(ctx, *,  question):
                responses = ['Да', 'Нет', 'Возможно', 'Спросите потом']
                await ctx.send(f'Вопрос: {question}, Ответ: {random.choice(responses)}')





client.run('ODM5MTU1ODQxMTE0MzA4NzE4.YJFixw.3JJYlH7WjQr61XwkKbSsHKGoRLg')






