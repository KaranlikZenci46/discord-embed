import discord
from discord.ext import commands
from discord.ui import Button, View

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

TOKEN = 'your_discord_token'
CHANNEL_ID = 1258067234236923955

@bot.event
async def on_ready():
    print('Bot is online')

    embed = discord.Embed(title="TITLE", description="Description", color=0x000000)

    embed.set_image(url="img url")
 
    button = Button(style=discord.ButtonStyle.link, label="Button", url="in button url")

    view = View()
    view.add_item(button)

    channel = bot.get_channel(CHANNEL_ID)
    if channel:
        await channel.send(embed=embed, view=view)
        print(f'Message sended {channel.name} named channel.')
    else:
        print("Channel is not exist")
        

bot.run(TOKEN)
