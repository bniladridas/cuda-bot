import discord
from discord.ext import commands

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="help", description="Get information about the bot's features")
    async def help(self, ctx):
        embed = discord.Embed(title="CUDA Unleashed Help", color=0x00ffff)
        embed.add_field(name="/gpu_stats", value="Fetch real-time GPU statistics including CUDA core usage, VRAM consumption, and GPU temperature", inline=False)
        embed.add_field(name="/benchmark", value="Run AI model performance tests using PyTorch and TensorFlow", inline=False)
        embed.add_field(name="/help", value="Get information about the bot's features", inline=False)
        
        await ctx.respond(embed=embed)

def setup(bot):
    bot.add_cog(Help(bot))
