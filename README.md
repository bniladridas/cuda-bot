# CUDA Bot

A Discord bot for monitoring and benchmarking GPU performance using CUDA.

## Prerequisites

1. NVIDIA GPU with CUDA support
2. Docker and Docker Compose installed
3. Python 3.10 or higher
4. Discord bot token

## Setup

1. Clone this repository
2. Create a `.env` file with your Discord token:
   ```
   DISCORD_TOKEN=your_token_here
   ```
3. Build and run the container:
   ```bash
   docker-compose up --build
   ```

## Features

- GPU statistics monitoring
- CUDA performance benchmarking
- Help command for bot usage

## Usage

- `/gpu_stats` - Get current GPU statistics
- `/benchmark` - Run CUDA performance benchmark
- `/help` - Get help with bot commands
- `/condition` - Get the current condition of the bot

## Notes

- Ensure NVIDIA drivers and CUDA toolkit are properly installed
- GPU functionality requires NVIDIA Container Toolkit
