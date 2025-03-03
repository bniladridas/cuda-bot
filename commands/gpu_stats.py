import discord
from discord.ext import commands
import torch

class GPUStats(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="gpu_stats")
    async def gpu_stats(self, ctx):
        if not torch.cuda.is_available():
            await ctx.send("No GPU available")
            return

        stats = {
            "device_name": torch.cuda.get_device_name(0),
            "memory_allocated": torch.cuda.memory_allocated(0),
            "memory_reserved": torch.cuda.memory_reserved(0),
            "utilization": torch.cuda.utilization(0)
        }

        message = "\n".join(f"{k}: {v}" for k, v in stats.items())
        await ctx.send(f"GPU Stats:\n```{message}```")

async def setup(bot):
    await bot.add_cog(GPUStats(bot))
