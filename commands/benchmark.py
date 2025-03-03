import discord
from discord.ext import commands
import torch
import time

class Benchmark(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="benchmark")
    async def benchmark(self, ctx):
        if not torch.cuda.is_available():
            await ctx.send("No GPU available for benchmarking")
            return

        # Run a simple matrix multiplication benchmark
        start_time = time.time()
        a = torch.randn(1000, 1000).cuda()
        b = torch.randn(1000, 1000).cuda()
        torch.matmul(a, b)
        elapsed_time = time.time() - start_time

        await ctx.send(f"Matrix multiplication benchmark completed in {elapsed_time:.4f} seconds")

async def setup(bot):
    await bot.add_cog(Benchmark(bot))
