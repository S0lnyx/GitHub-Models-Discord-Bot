import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
import azure_module

load_dotenv
token = os.getenv("TOKEN")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.command()
async def ping(ctx):
    await ctx.send('I am here.')

@bot.command()
async def ai(ctx, *, request_text):
    await ctx.send(azure_module.response_req(request_text))

bot.run(token)