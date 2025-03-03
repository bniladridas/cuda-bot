# Use an official CUDA-enabled Python runtime as a parent image
FROM nvidia/cuda:11.8.0-cudnn8-runtime-ubuntu22.04

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    && pip3 install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . .

# Make port 80 available to the world outside this container
EXPOSE 80

# Run bot.py when the container launches
CMD ["python3", "bot.py"]
