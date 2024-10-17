# 🌐 Project Overview

This project is the **Telegram keyword parser bot** that monitors specified Telegram channels for messages containing user-defined keywords.
It uses `Telethon` and `Aiogram` for interacting with the [Telegram API](https://core.telegram.org/) and sending notifications to a specified user.

## 🚀 Key Features
- 🔍 Keyword Monitoring: Tracks new messages across multiple channels and checks for matching keywords.
- 💬 Notification Bot: Sends a Telegram notification to a specified user when a keyword match is found.
- 📦 Channel Management: Automatically marks messages as read once they are processed.
- 🐍 Asynchronous Processing: Utilizes Python's asyncio for efficient, non-blocking message retrieval.

## 💻 Technologies Used
- [**Python 3.12**](https://www.python.org/): The main language used for building the project.
- [**Telethon: Library**](https://docs.telethon.dev/en/stable/index.html): for working with the Telegram API.
- [**Aiogram**](https://docs.aiogram.dev/en/stable/index.html): Telegram bot framework to handle user notifications.
- [**pip-tools**](https://github.com/jazzband/pip-tools): For managing Python dependencies.
- [**Colorama & Termcolor**](https://github.com/tartley/colorama): For terminal coloring and enhanced logging.

## 🛠️ Setup Instructions

### 📋 Prerequisites
- A `.env` file in the root directory containing the following environment variables:
  
    ```env
    API_ID=<your_telegram_api_id>
    API_HASH=<your_telegram_api_hash>
    CHANNELS_LINKS=<comma_separated_channel_links>
    KEYWORDS=<comma_separated_keywords>

    BOT_TOKEN=<your_bot_token>
    YOUR_TELEGRAM_ID=<your_user_id>
    ```

### 🚀 Running the Application
1. Clone the repository:

    ```bash
    git clone https://github.com/Nikilandgelo/tg_parser_by_keywords.git
    cd tg_parser_by_keywords
    ```
2. Set up a virtual environment:

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
    ```
3. Install dependencies: Ensure that `pip-tools` is installed first to manage the dependencies:

   ```bash
   pip install pip-tools
   pip-compile -U
   pip-sync
    ```
4. Run the bot:

   ```bash
    
   python3 main.py
    
    ```
