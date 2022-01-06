import os
import discord
from discord import voice_client
import youtube_dl
from dotenv import load_dotenv
from discord.ext import commands, tasks

load_dotenv()

DISCORD_TOKEN = os.getenv('discord_token')

bot = commands.Bot(command_prefix="!")

youtube_dl.utils.bug_reports_message = lambda: ''

ytdl_format_options = {
  'format': 'bestaudio/best',
  'restrictfilenames': True,
  'noplaylist': True,
  'nocheckcertificate': True,
  'ignoreerrors': False,
  'logtostderr': False,
  'quiet': True,
  'no_warnings': True,
  'default_search': 'auto',
  'source_address': '0.0.0.0' # bind to ipv4 since ipv6 addresses cause issues sometimes
}

ffmpeg_options = {
  'options': '-vn'
}

ytdl = youtube_dl.YoutubeDL(ytdl_format_options)

class YTDLSource(discord.PCMVolumeTransformer):
  def __init__(self, source, *, data, volume=0.5):
    super().__init__(source, volume)
    self.data = data
    self.title = data.get('title')
    self.url = ""

  @classmethod
  async def from_url(cls, url, *, loop=None, stream=False):
    loop = loop or asyncio.get_event_loop()
    data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=not stream))
    if 'entries' in data:
      # take first item from a playlist
      data = data['entries'][0]
    filename = data['title'] if stream else ytdl.prepare_filename(data)
    return filename


@bot.event
async def on_ready():
    print("Olha o homi aí")

@bot.command(name="join", help="Diz ao bot para entrar no canal de voz")
async def join(ctx):
  if not ctx.message.author.voice:
    await ctx.send("{} não está conectado a um canal de voz".format(ctx.message.author.name))
    return
  else:
    channel = ctx.message.author.voice.channel
  await channel.connect()

@bot.command(name="leave", help="Para fazer o bot sair do canal de voz")
async def leave(ctx):
  voice_client = ctx.message.guild.voice_client
  if voice_client.is_connected():
    await voice_client.disconnect()
  else:
    await ctx.send("O bot não está conectado no canal de voz")

@bot.command(name="play", help="Toca o som dj")
async def play(ctx, url):
  try:
    server = ctx.message.guild
    voice_channel = server.voice_client

    async with ctx.typing():
      filename = await YTDLSource.from_url(url, loop=bot.loop)
      voice_channel.play(discord.FFmpegPCMAudio(executable="ffmpeg.exe", source=filename))
    await ctx.send("**Tocando agora:** {}".format(filename))
  except:
    await ctx.send("O bot não está conectado no canal de voz")

@bot.command(name="pause", help="Pausa essa porra aí, ooh!")
async def pause(ctx):
  voice_client = ctx.message.guild.voice_client
  if voice_client.is_playing():
    await voice_client.pause()
  else:
    await ctx.send("O bot não está conectado no canal de voz")

@bot.command(name="resume", help="Continuar música pausada, caralho!:")
async def resume(ctx):
  voice_client = ctx.message.guild.voice_client
  if voice_client.is_paused():
    await voice_client.resume()
  else:
    await ctx.send("O bot não tá tocando nada. Use o comando !play para ele tocar ( ͡° ͜ʖ ͡°)")

@bot.command(name="stop", help="Para essa mzr aí, porra!!!")
async def stop(ctx):
  voice_client = ctx.message.guild.voice_client
  if voice_client.is_playing():
    await voice_client.stop()
  else:
    await ctx.send("O bot não está tocando nada no momento")

bot.run(DISCORD_TOKEN)