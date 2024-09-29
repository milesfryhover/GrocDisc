# Grocery List Discord Bot

## Overview

The Grocery List Discord Bot is a simple yet efficient bot designed to manage a grocery list through a Discord server. It uses Discord's bot API to interact in real-time and allows users to add items, list the current grocery items, remove specific items, or clear the entire list.

I wrote this bot specifically for use with my partner, so I've sprinkled a few cute messages here and there for them to find. :) 

## Features

- **Add Items to Grocery List**: Add items to your grocery list directly from the chat.
- **List Grocery Items**: View all items currently in your grocery list.
- **Remove Specific Items**: Remove specific items from your grocery list.
- **Clear the List**: Clear all items from your grocery list.
- **Help Command**: Provides a list of supported commands.

## Installation

1. **Clone the Repository**:
    \```
    git clone https://github.com/yourusername/grocery-list-discord-bot.git
    cd grocery-list-discord-bot
    \```

2. **Install Dependencies**:
    Make sure you have Python installed. Then, run:
    \```
    pip install -r requirements.txt
    \```

3. **Set Up Environment Variables**:
    Create a `.env` file in the root directory and add your Discord bot token:
    \```
    DISCORD_BOT_TOKEN=your_token_here
    \```

## Usage

Run the bot using the Python script:
\```
python bot.py
\```

## Commands

- **Add Items**:
    `!add <item1>, <item2>, ...`
    Example: `!add apples, bananas, oranges`

- **List Items**:
    `!list`
    Shows a formatted list of all items in the grocery list.

- **Remove Items**:
    `!remove <item1>, <item2>, ...`
    Removes the specified items from the list. Notifies if certain items were not found.

- **Clear All Items**:
    `!removeAll`
    Clears the entire grocery list.

- **Help**:
    `!help`
    Displays the list of supported commands.

- **Love**:
    `!love`
    A fun command that sends a loving message in the chat.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

1. Fork the repository.
2. Create your feature branch (`git checkout -b feature/AmazingFeature`).
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`).
4. Push to the branch (`git push origin feature/AmazingFeature`).
5. Open a pull request.

## Acknowledgements

- [discord.py](https://github.com/Rapptz/discord.py) for the Discord bot framework.
- [dotenv](https://pypi.org/project/python-dotenv/) for managing environment variables.

For any issues or feature requests, please open an issue in this repository.

Happy grocery shopping! 🛒