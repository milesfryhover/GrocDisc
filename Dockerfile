# Use an official Python runtime as a parent image
FROM python:3.12.3-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the requirements file into the container
COPY requirements.txt ./

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Set environment variables
ARG DISCORD_BOT_TOKEN
ENV DISCORD_BOT_TOKEN=${DISCORD_BOT_TOKEN}

# Command to run the bot
CMD ["python", "./bot.py"]