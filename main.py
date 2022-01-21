import discord
from discord.ext import commands
from discord_webhook import DiscordWebhook, DiscordEmbed
import datetime
import time


t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)

client = commands.Bot(command_prefix='$')
datetime = datetime.datetime.now()


@client.event
async def on_ready():
    print(str(datetime) + ' - {0.user} is live!'.format(client))
    webhook = DiscordWebhook(
        "WEBHOOK")
    embed = DiscordEmbed(title='ESCP-helper is live!', color=0x3a0080)
    embed.set_footer(text='@ESCPnotes',
                     icon_url="IMAGE")
    embed.set_timestamp()
    webhook.add_embed(embed)
    response = webhook.execute()
    await client.change_presence(activity=discord.Game(name="Watching...",
                                                       icon="IMAGE"))


@client.command(pass_context=True)
async def sendembed(ctx, title, description):
    await ctx.message.delete()
    embed = discord.Embed(title=title, description=description, color=0x3a0080)
    embed.set_author(name='ESCP-helper',
                     icon_url="IMAGE")
    embed.set_footer(text='Powered by @ESCPnotes',
                     icon_url="IMAGE")
    await ctx.message.channel.send(embed=embed)


@client.command()
async def purge(ctx, limit):
    if ctx.author.guild_permissions.administrator:
        await ctx.channel.purge(limit=int(limit))
        await ctx.message.delete()


client.run('KEY')
