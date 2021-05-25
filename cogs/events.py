import discord
from discord.ext import commands
import datetime

class Events(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        await self.client.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.playing, name='MINECRAFT'))
        print("""\033[91m
    
 $$$$$$\            $$\                                 $$\     $$\       
$$  __$$\           $$ |                                $$ |    $$ |      
$$ /  \__| $$$$$$\  $$ | $$$$$$$\  $$$$$$\  $$\   $$\ $$$$$$\   $$$$$$$\  
\$$$$$$\  $$  __$$\ $$ |$$  _____|$$  __$$\ $$ |  $$ |\_$$  _|  $$  __$$\ 
 \____$$\ $$$$$$$$ |$$ |$$ /      $$ /  $$ |$$ |  $$ |  $$ |    $$ |  $$ |
$$\   $$ |$$   ____|$$ |$$ |      $$ |  $$ |$$ |  $$ |  $$ |$$\ $$ |  $$ |
\$$$$$$  |\$$$$$$$\ $$ |\$$$$$$$\ \$$$$$$  |\$$$$$$  |  \$$$$  |$$ |  $$ |
 \______/  \_______|\__| \_______| \______/  \______/    \____/ \__|  \__|
                                                                          
                                                                          
                                                                          
    
    \033[1m""")
        # channel=self.client.get_channel(id=830651285115109426)
        # await channel.send("```If you were frozen, please create a ticket.```")

    @commands.Cog.listener()
    async def on_member_join(self, member):
        embed = discord.Embed(
            title = 'Welcome',
            description = f'Welcome to Selcouth, {member.mention}! \nMake sure to read our #rules',
            colour = 0x851a14,
        )

        embed.set_thumbnail(url=f'{member.avatar_url}')
        embed.timestamp = datetime.datetime.utcnow()
        embed.set_footer(text='Selcouth Development')

        channel = self.client.get_channel(id=689280222842978385)

        em = discord.Embed(
            title = 'Welcome',
            description= """Welcome to **~ ＳＥＬ☾ＯＵＴＨ ~**

            We hope you enjoy your stay!
            - Tyler & Kenny

           """,
            colour = 0x851a14,
        )
        
        em.set_footer(text='Selcouth Development')

        await member.send(embed=em)
        # await channel.send(embed=embed)
        

        


    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('missing arguments.')
        if isinstance(error, commands.MissingPermissions):
            await ctx.send('no permission.')

    @commands.Cog.listener()
    async def on_message(self, ctx, message):

        if ctx.channel.id == 828040521283928064:
            if ctx.author.guild_permissions.administrator:
                pass
            elif message.content.startswith('.new '):
                pass
            else:
                ctx.channel.purge(limit=1)
        else:
            pass
    


    

    # Backup event for MEE6 ---

    # @commands.Cog.listener
    # async def on_member_join(self, member):
    #     role = discord.utils.get(member.server.roles, name='𝑾𝒂𝒏𝒅𝒆𝒓𝒆𝒓')
    #     await self.client.add_roles(member, role)


def setup(client):
    client.add_cog(Events(client))