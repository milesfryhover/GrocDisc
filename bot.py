# bot.py
import os
import pickle
import discord
from dotenv import load_dotenv

GROCERY_LIST_FILE = 'grocery_list.pkl'

# load grocery list from memory
def load_list():
    """
    Loads a grocery list from a pickle cache file, if it exists and contains valid data.

    :return: A list of grocery items if the cache file exists and is valid; otherwise, an empty list.
    """
    print('Loading grocery list from pickle cache')
    if os.path.exists(GROCERY_LIST_FILE):
        try:
            with open(GROCERY_LIST_FILE, 'rb') as file:
                cache_data = pickle.load(file)
                if isinstance(cache_data, list):
                    return cache_data
        except (EOFError, pickle.UnpicklingError):
            pass
    return []

def save_list(l):
    """
    :param l: List of grocery items to be saved.
    :return: None
    """
    print('Saving grocery list to pickle cache')
    with open(GROCERY_LIST_FILE, 'wb') as file:
        pickle.dump(l, file)

grocery_list = load_list()

# Create an instance of Intents
intents = discord.Intents.default()
intents.message_content = True  # Enable the specific intents you need
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    """
    Triggered when the bot has successfully connected to Discord and is ready.
    It prints a message indicating the bot's connection status.

    :return: None
    """
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    """
    :param message: The message received from the Discord server.
    :return: None
    """
    if message.author == client.user:
        return

    if message.content.startswith('!love '):
        print('Sending love to Ais!')
        await message.channel.send('I love you!')

    elif message.content.startswith('!add '):
        print('Adding items to the grocery list')
        items = message.content[len('!add '):].split(',')
        grocery_list.extend(item.strip() for item in items)
        save_list(grocery_list)
        await message.channel.send('Added to the grocery list!')


    elif message.content.startswith('!list'):
        print('Sending grocery list to channel')
        if not grocery_list:
            await message.channel.send('The grocery list is empty.')
        else:
            formatted_list = '\n'.join(f'- {item}' for item in grocery_list)
            await message.channel.send(formatted_list)

    elif message.content.startswith('!remove '):
        print('Removing items from the grocery list')
        items_to_remove = message.content[len('!remove '):].split(',')
        items_to_remove = [item.strip() for item in items_to_remove]

        not_found_items = []
        for item in items_to_remove:
            if item in grocery_list:
                while item in grocery_list:
                    grocery_list.remove(item)
            else:
                not_found_items.append(item)

        save_list(grocery_list)

        if not_found_items:
            await message.channel.send(f"Could not find the following items: {', '.join(not_found_items)}")
        else:
            await message.channel.send('Items removed from list!')

    elif message.content.startswith('!removeAll'):
        print('Removing all items from the grocery list')
        grocery_list.clear()
        save_list(grocery_list)
        await message.channel.send('All items removed from cache!')

    elif message.content.startswith('!help '):
        print('Sending help message')
        help_message = (
            "Supported Commands:\n"
            "- `!add <item1>, <item2>, ...`: Adds the specified items to the list.\n"
            "- `!list`: Lists all items currently in the list.\n"
            "- `!remove <item1>, <item2>, ...`: Removes the specified items from the list. If an item cannot be found, it will notify which items were not found.\n"
            "- `!help`: Displays this help message.\n"
            "- `!love`: Just a reminder :).\n"
        )
        await message.channel.send(help_message)

load_dotenv()
# Ensure your token is stored securely as an environment variable
token = os.getenv('DISCORD_BOT_TOKEN')  # Set your token as an environment variable
if token:
    client.run(token)
else:
    print("Error: Discord bot token not found. Set it as an environment variable.")