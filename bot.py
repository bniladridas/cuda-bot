import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
import asyncio
import config

load_dotenv()

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="/", intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')
    print(f'Using CUDA device: {config.CUDA_DEVICE}')

async def load_extensions():
    await bot.load_extension('commands.gpu_stats')
    await bot.load_extension('commands.benchmark')
    await bot.load_extension('commands.help')
    await bot.load_extension('commands.condition')

async def main():
    async with bot:
        await load_extensions()
        await bot.start(os.getenv('DISCORD_TOKEN'))

if __name__ == "__main__":
    asyncio.run(main())
