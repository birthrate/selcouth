import discord
from discord.ext import commands
# import time
import asyncio

class Admin(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount=10):
        await ctx.channel.purge(limit=amount+1)

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *,reason=None):
        await ctx.channel.purge(limit=1)
        embed=discord.Embed(
            title='User Punished',
            description= f'✅ {member.mention} ({member.id}) has been succesfully kicked',
            colour=0x008000
        )

        embed.set_footer(text='Selcouth Development')
        await ctx.channel.purge(limit=1)
        await ctx.send(embed=embed)

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *,reason=None):
        await ctx.channel.purge(limit=1)
        embed=discord.Embed(
            title='User Punished',
            description= f'✅ {member.mention} ({member.id}) has been succesfully banned',
            colour=0x008000
        )

        embed.set_footer(text='Selcouth Development')
        await member.ban(reason=reason)
        await ctx.send(embed=embed)

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def mute(self, ctx, member: discord.Member):
        await ctx.channel.purge(limit=1)
        embed=discord.Embed(
            title='User Punished',
            description= f'✅ {member.mention} ({member.id}) has been succesfully muted',
            colour=0x008000
        )

        embed.set_footer(text='Selcouth Development')
        mutedRole = discord.utils.get(ctx.guild.roles, name='Muted')
        
        
        role = discord.utils.find(lambda r: r.name =='Muted', ctx.message.guild.roles)

        if role in member.roles:
            await ctx.send('{} is already muted'.format(member))
        else:
            await ctx.send(embed=embed)
            await member.add_roles(mutedRole)

    @commands.command(aliases=['tmute'])
    @commands.has_permissions(administrator=True)
    async def tempmute(self, ctx, member: discord.Member, time=None):
        await ctx.channel.purge(limit=1)
        temp=discord.Embed(
            title='User Punished',
            description= f'✅ {member.mention} ({member.id}) has been temporarily muted',
            colour=0x008000
        )

        time_convert = {"s":1, "m":60, "h":3600,"d":86400}
        tempmute = int(time[0]) * time_convert[time[-1]]

        mutedRole = discord.utils.get(ctx.guild.roles, name='Muted')
        
        
        role = discord.utils.find(lambda r: r.name =='Muted', ctx.message.guild.roles)

        if role in member.roles:
            await ctx.send('{} is already muted'.format(member))
        elif time != None:
            await ctx.send(embed=temp)
            await member.add_roles(mutedRole)
            await asyncio.sleep(tempmute)
            await member.remove_roles(mutedRole)



    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def unmute(self, ctx, member: discord.Member):
        await ctx.channel.purge(limit=1)
        embed=discord.Embed(
            title='-',
            description= f'✅ {member.mention} ({member.id}) has been succesfully unmuted',
            colour=0x008000
        )

        embed.set_footer(text='Selcouth Development')

        mutedRole = discord.utils.get(ctx.guild.roles, name='Muted')


        role = discord.utils.find(lambda r: r.name =='Muted', ctx.message.guild.roles)

        if role not in member.roles:
            await ctx.send('{} is not muted'.format(member))
        else:
            await ctx.send(embed=embed)
            await member.remove_roles(mutedRole)
            
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def mvc(self, ctx):
        await ctx.channel.purge(limit=1)
        embed=discord.Embed(
            title='-',
            description= f'✅ Voice Channel has been succesfully muted',
            colour=0x008000
        )

        embed.set_footer(text='Selcouth Development')

        role = discord.utils.find(lambda r: r.name =='bypass', ctx.message.guild.roles)
        vc = ctx.author.voice.channel
        for member in vc.members:
            if role in member.roles:
                pass
            else:
                await member.edit(mute=True)
        await ctx.send(embed=embed)

    @commands.command(aliases=['nigga'])
    @commands.has_permissions(administrator=True)
    async def stfu(self, ctx):
        await ctx.channel.purge(limit=1)
        embed=discord.Embed(
            title='-',
            description= f'✅ please stop fucking talking',
            colour=0x008000
        )

        embed.set_footer(text='Selcouth Development')

        role = discord.utils.find(lambda r: r.name =='stfu', ctx.message.guild.roles)
        vc = ctx.author.voice.channel
        for member in vc.members:
            if role not in member.roles:
                pass
            else:
                await member.edit(mute=True)
        await ctx.send(embed=embed)

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def silence(self, ctx):
        await ctx.channel.purge(limit=1)
        embed=discord.Embed(
            title='-',
            description= f'✅ shh........',
            colour=0x008000
        )

        embed.set_footer(text='Selcouth Development')

        role = discord.utils.find(lambda r: r.name =='silence', ctx.message.guild.roles)
        vc = ctx.author.voice.channel
        for member in vc.members:
            if role in member.roles:
                pass
            else:
                await member.edit(mute=True)
        await ctx.send(embed=embed)

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def umvc(self, ctx):
        await ctx.channel.purge(limit=1)
        embed=discord.Embed(
            title='-',
            description= f'✅ Voice Channel has been succesfully unmuted',
            colour=0x008000
        )

        embed.set_footer(text='Selcouth Development')
        vc = ctx.author.voice.channel
        for member in vc.members:
            await member.edit(mute=False)
        await ctx.send(embed=embed)

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def bypass(self, ctx, member: discord.Member):
        await ctx.channel.purge(limit=1)
        bypass=discord.Embed(
            title='-',
            description= f':white_check_mark: {member.mention} ({member.id}) can now bypass VC mutes',
            colour=0x008000
        )

        no_bypass=discord.Embed(
            title='-',
            description= f':white_check_mark: {member.mention} ({member.id}) can no longer bypass VC mutes',
            colour=0x008000
        )

        bypass.set_footer(text='Selcouth Development')
        no_bypass.set_footer(text='Selcouth Development')

        bypassRole = discord.utils.get(ctx.guild.roles, name='bypass')


        role = discord.utils.find(lambda r: r.name =='bypass', ctx.message.guild.roles)

        if role in member.roles:
            await ctx.send(embed=no_bypass)
            await member.remove_roles(bypassRole)
        else:
            await ctx.send(embed=bypass)
            await member.add_roles(bypassRole)

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def sm(self, ctx, member: discord.Member):
        await ctx.channel.purge(limit=1)
        await member.edit(mute=True)

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def sum(self, ctx, member: discord.Member):
        await ctx.channel.purge(limit=1)
        await member.edit(mute=False)

    @commands.command()
    @commands.has_permissions(manage_channels=True)
    async def delay(self, ctx, seconds: int):
        await ctx.channel.purge(limit=1)
        await ctx.channel.edit(slowmode_delay=seconds)
        await ctx.send(f'Delay in this channel set to {seconds} seconds.')

    @commands.command()
    @commands.has_permissions(manage_channels=True)
    async def lock(self, ctx, channel: discord.TextChannel=None):
        await ctx.channel.purge(limit=1)
        embed=discord.Embed(
            title='🔒 Channel Locked 🔒',
            description='This channel has been locked until further notice.',
            colour=0x851a14
        )

        embed.set_footer(text='Selcouth Development')

        channel = channel or ctx.channel
        overwrite = channel.overwrites_for(ctx.guild.default_role)
        overwrite.send_messages=False
        await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
        await ctx.send(embed=embed)
        

    @commands.command()
    @commands.has_permissions(manage_channels=True)
    async def unlock(self, ctx, channel: discord.TextChannel=None):
        await ctx.channel.purge(limit=1)
        embed=discord.Embed(
            title='🔓 Channel Unlocked 🔓',
            colour=0x851a14
        )

        embed.set_footer(text='Selcouth Development')

        channel = channel or ctx.channel
        overwrite = channel.overwrites_for(ctx.guild.default_role)
        overwrite.send_messages=True
        await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
        await ctx.send(embed=embed)

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def freeze(self, ctx, member: discord.Member):
        embed=discord.Embed(
            title='User Punished',
            description= f'✅ {member.mention} ({member.id}) has been succesfully frozen',
            colour=0x008000
        )

        embed.set_footer(text='Selcouth Development')

        frozenRole = discord.utils.get(ctx.guild.roles, name='Frozen')


        role = discord.utils.find(lambda r: r.name =='Frozen', ctx.message.guild.roles)

        if role in member.roles:
            await ctx.send('{} is already frozen'.format(member))
        else:
            await ctx.send(embed=embed)
            await member.add_roles(frozenRole)
        

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def unfreeze(self, ctx, member: discord.Member):
        embed=discord.Embed(
            title='-',
            description= f'✅ {member.mention} ({member.id}) has been succesfully unfrozen',
            colour=0x008000
        )

        embed.set_footer(text='Selcouth Development')

        frozenRole = discord.utils.get(ctx.guild.roles, name='Frozen')


        role = discord.utils.find(lambda r: r.name =='Frozen', ctx.message.guild.roles)

        if role not in member.roles:
            await ctx.send('{} is not frozen'.format(member))
        else:
            await ctx.send(embed=embed)
            await member.remove_roles(frozenRole)
            
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def ss(self, ctx, member: discord.Member):
        frozen=discord.Embed(
            title='User Punished',
            description= f':white_check_mark: {member.mention} ({member.id}) has been succesfully frozen',
            colour=0x008000
        )

        not_frozen=discord.Embed(
            title='User Punished',
            description= f':white_check_mark: {member.mention} ({member.id}) has been succesfully unfrozen',
            colour=0x008000
        )

        frozen.set_footer(text='Selcouth Development')
        not_frozen.set_footer(text='Selcouth Development')

        frozenRole = discord.utils.get(ctx.guild.roles, name='Frozen')


        role = discord.utils.find(lambda r: r.name =='Frozen', ctx.message.guild.roles)

        if role in member.roles:
            await ctx.send(embed=not_frozen)
            await member.remove_roles(frozenRole)
        else:
            await ctx.send(embed=frozen)
            await member.add_roles(frozenRole)


    #############################################################
    @commands.has_permissions(administrator=True)
    async def sslist(self, ctx):
        role = ctx.message.guild.get_role(836657435460632606)
        for member in ctx.message.guild.members:
            if role in member.roles:
                await ctx.send(f'{member.name}({member.id}) is currently {role.name}')

    @commands.command(aliases=['development'])
    async def maintanence(self, ctx):
        yes = discord.Embed(
            title='🚧 Currently Under Maintanence 🚧',
            description='[tempmute, .list, .sslist]',
            colour = 0xeed202
        )

        yes.set_footer(text='Selcouth Development')

        no = discord.Embed(
            title='🚧 Currently Under Maintanence 🚧',
            description='N/A',
            colour = 0x008000
        )

        no.set_footer(text='Selcouth Development')

        ######################
        MAINTANENCE = True
        ######################

        if MAINTANENCE == True:
            await ctx.send(embed=yes)
        else:
            await ctx.send(embed=no)

def setup(client):
    client.add_cog(Admin(client))