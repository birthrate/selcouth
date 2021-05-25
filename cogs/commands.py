import discord
from discord.ext import commands
import datetime

class Commands(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['?'])
    async def kenny(self, ctx):
        links="""https://bit.ly/3mjWh03 https://bit.ly/31Mo1Rm https://bit.ly/39G77s7 https://bit.ly/3wpYATX"""
        await ctx.send(links)

    @commands.command()
    async def selcouth(self, ctx):
        em = discord.Embed(
            title="🚧 Under Maintanence 🚧",
#             description="""
# \n $$$$$$\            $$\                                 $$\     $$\       
# \n$$  __$$\           $$ |                                $$ |    $$ |      
# \n$$ /  \__| $$$$$$\  $$ | $$$$$$$\  $$$$$$\  $$\   $$\ $$$$$$\   $$$$$$$\  
# \n\$$$$$$\  $$  __$$\ $$ |$$  _____|$$  __$$\ $$ |  $$ |\_$$  _|  $$  __$$\ 
# \n \____$$\ $$$$$$$$ |$$ |$$ /      $$ /  $$ |$$ |  $$ |  $$ |    $$ |  $$ |
# \n$$\   $$ |$$   ____|$$ |$$ |      $$ |  $$ |$$ |  $$ |  $$ |$$\ $$ |  $$ |
# \n\$$$$$$  |\$$$$$$$\ $$ |\$$$$$$$\ \$$$$$$  |\$$$$$$  |  \$$$$  |$$ |  $$ |
# \n \______/  \_______|\__| \_______| \______/  \______/    \____/ \__|  \__|
#     """,
            colour = 0xeed202,
        )

        em.set_footer(text='Selcouth Development')

        await ctx.send(embed=em)

    @commands.command()
    async def help(self, ctx):
        em = discord.Embed(
            title = 'Selcouth Help',
            colour = 0x851a14,
        )

        developer = discord.utils.get(ctx.guild.roles, name="developer")

        if developer in ctx.author.roles:
            em.add_field(name="`.ping`", value='see the current ping of the bot.')
            em.add_field(name="`.users`", value='see the current number of members in the server.')
            em.add_field(name="`.clear`", value='clear a certain amount of chat messages. {default:10}')
            em.add_field(name="`.kick`", value='kick a member from the server.')
            em.add_field(name="`.ban`", value='ban a member from the server.')
            em.add_field(name="`mute/unmute`", value='mute/unmute a a user.')
            em.add_field(name="`tempmute/unmute`", value='temporarily mute/unmute a a user.')
            em.add_field(name="`sm/sum`", value="server mute/server unmute a member")
            em.add_field(name="`mvc/umvc`", value="mute/unmute every user inside your current vc.")
            em.add_field(name='`.delay`', value='slow down the chat by a set amount of time.')
            em.add_field(name='`lock/unlock`', value='lock/unlock a channel (only users with administrative permissions may type in chat.)')
            em.add_field(name="`ss(freeze/unfreeze)`", value="Completely restrict a member to only allow the creation of a ticket.")
            em.add_field(name="`.avatar(av)`", value="View your own, or other members' avatars.")
            em.add_field(name="`.profile(who)`", value="View your own, or other members' profiles.")
            em.add_field(name="`.ticket(s)`", value='run this command for help with tickets.')
            em.add_field(name="`load <file.py>`", value="load a python cogs file (excluding main.py)")
            em.add_field(name="`unload <file>`", value="unload a python cogs file (excluding main.py)")
            em.add_field(name="`reload <file>`", value="reload a python cogs file (excluding main.py)")
            em.add_field(name="`maintanence`", value="See what commands/features are currently under maintanence")
            em.add_field(name="`sslist (MAINTANENCE)`", value="null")
            em.add_field(name="`list(MAINTANENCE)`", value="null")
            em.add_field(name="**MAIN.PY**", value="If you edit the main.py file, you can't update by running ```.reload main```, you have to manually shut down and restart the bot!")
            em.add_field(name="**IMPORTANT**", value="When loading/unloading/reloading files, do **NOT** add .py at the end! (.reload admin)")
            em.set_footer(text='Developer Only Help Menu')

            await ctx.send(embed=em)
        elif ctx.author.guild_permissions.administrator:
            em.add_field(name="`.ping`", value='see the current ping of the bot.')
            em.add_field(name="`.users`", value='see the current number of members in the server.')
            em.add_field(name="`.clear`", value='clear a certain amount of chat messages. {default:10}')
            em.add_field(name="`.kick`", value='kick a member from the server.')
            em.add_field(name="`.ban`", value='ban a member from the server.')
            em.add_field(name="`mute/unmute`", value='mute/unmute a a user.')
            em.add_field(name="`tempmute/unmute`", value='temporarily mute/unmute a a user.')
            em.add_field(name="`mvc/umvc`", value="mute/unmute every user inside your current vc.")
            em.add_field(name='`.delay`', value='slow down the chat by a set amount of time.')
            em.add_field(name='`lock/unlock`', value='lock/unlock a channel (only users with administrative permissions may type in chat.)')
            em.add_field(name="`ss(freeze/unfreeze)`", value="Completely restrict a member to only allow the creation of a ticket.")
            em.add_field(name="`.avatar`", value="View your own, or other members' avatars.")
            em.add_field(name="`.profile`", value="View your own, or other members' profiles.")
            em.add_field(name="`.ticket`", value='run this command for help with tickets.')
            em.add_field(name="`???`", value='there are other commands, cba to add them to the list. If you want to know just them message kenny#1111.')
            em.set_footer(text='Selcouth Development')

            await ctx.send(embed=em)
        else:
            em.add_field(name="`.ping`", value='See the current ping of the bot.')
            em.add_field(name="`.users`", value='See the current number of members in the server.')
            em.add_field(name="`.avatar`", value="View your own, or other members' avatars.")
            em.add_field(name="`.profile`", value="View your own, or other members' profiles.")
            em.add_field(name="`.ticket`", value='run this command for help with tickets.')
            em.set_footer(text='Selcouth Development')

            await ctx.send(embed=em)

    @commands.command(aliases=['bot', 'developer'])
    async def dev(self, ctx):
        em = discord.Embed(
            description = '```Selcouth Bot developed by kenny#1111```',
            colour = 0x851a14,
        )
        
        em.set_author(name='developer')
        em.set_footer(text='Selcouth Development')
            
        await ctx.send(embed=em)


    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'{round(self.client.latency*1000)}ms')

    @commands.command()
    async def users(self, message):
        id = self.client.get_guild(511674643225247776)

        await message.channel.send(f'{id.member_count} members.')

    @commands.command(aliases=['av'])
    async def avatar(self, ctx, member: discord.Member=None):
        avatar = discord.Embed(
            colour = 0x851a14
        )

        if member is None:
            member = ctx.message.author
        avatar.set_image(url='{}'.format(member.avatar_url))
        await ctx.send(embed=avatar)

    @commands.command(aliases=['who'])
    async def profile(self, ctx,  member: discord.Member=None):
        if member is None:
            member = ctx.message.author
        profile = discord.Embed(
            title='Profile',
            colour = member.colour
        )

        
        fields = [("Name", str(member), True),
				  ("ID", member.id, True),
				  ("Top role", member.top_role.mention, True),
				  ("Status", str(member.status).title(), True),
				  ("Activity", f"{str(member.activity.type).split('.')[-1].title() if member.activity else 'N/A'} {member.activity.name if member.activity else ''}", True),
				  ("Created at", member.created_at.strftime("%d/%m/%Y %H:%M:%S"), True),
				  ("Joined at", member.joined_at.strftime("%d/%m/%Y %H:%M:%S"), True)]

        for name, value, inline in fields:
            profile.add_field(name=name, value=value, inline=inline)
        
        profile.set_thumbnail(url=f'{member.avatar_url}')
        profile.timestamp = datetime.datetime.utcnow()
        profile.set_footer(text='Selcouth Development')
        await ctx.send(embed=profile)

    @commands.command(aliases=['info'])
    async def server(self, ctx):
        embed = discord.Embed(title="Server information",
                    colour=0x851a14,
                    timestamp=datetime.datetime.utcnow())

        embed.set_thumbnail(url=ctx.guild.icon_url)

        fields = [("ID", ctx.guild.id, True),
                ("Owner", 'kenny#1111', True),
                ("Region", ctx.guild.region, True),
                ("Created at", ctx.guild.created_at.strftime("%d/%m/%Y %H:%M:%S"), True),
                ("Members", len(ctx.guild.members), True),
                ("Humans", len(list(filter(lambda m: not m.bot, ctx.guild.members))), True),
                ("Bots", len(list(filter(lambda m: m.bot, ctx.guild.members))), True),
                ("Banned members", len(await ctx.guild.bans()), True),
                ("Text channels", len(ctx.guild.text_channels), True),
                ("Voice channels", len(ctx.guild.voice_channels), True),
                ("Categories", len(ctx.guild.categories), True),
                ("Roles", len(ctx.guild.roles), True),
                ("\u200b", "\u200b", True)]

        for name, value, inline in fields:
            embed.add_field(name=name, value=value, inline=inline)

        embed.set_footer(text='Selcouth Development')

        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Commands(client))