> [!CAUTION]
> Please be aware that using this bot to scrape messages or automate actions on Telegram may violate Telegram's policies, even if you are not engaging in spam, illegal activities, or violating their Terms of Service (ToS). Telegram has been actively restricting accounts that exhibit bot-like behavior as part of their fight against abuse and spam. This could lead to:
> - **Temporary or permanent account bans**
> - **Loss of access to your account, without guaranteed support from Telegram**
> - **Potential risks to account safety and privacy**
>
> Use this bot at your own risk, and be cautious of the potential consequences of automated interactions on Telegram. It is advisable to follow all of Telegram's guidelines and avoid any activity that could be perceived as spammy or suspicious.

# 🌐 Project Overview

This project is the **Telegram keyword parser bot** that scans specified channels for messages containing user-defined keywords and sends notifications via a bot.
It is built using `Telethon` for interacting with Telegram channels and `Aiogram` for bot interactions. The project leverages `Docker` for containerization, ensuring easy setup and deployment.

## 🚀 Key Features
- 🛠 Asynchronous message handling using `aiogram` and `Telethon`.
- 🔍 Keyword-based message filtering from multiple channels.
- 💬 Automatic notifications via Telegram bot for matched messages.
- 🐍 `Python 3.13` and `pip-tools` for managing dependencies.
- 🐋 Dockerized environment: easily set up and run the application in a containerized environment using `Docker` and `Docker Compose`.

## 💻 Technologies Used
| [**Python 3.13**](https://www.python.org/)      | [**Telethon: Library**](https://docs.telethon.dev/en/stable/index.html) | [**Aiogram**](https://docs.aiogram.dev/en/stable/index.html) | [**pip-tools**](https://github.com/jazzband/pip-tools) | [**Colorama & Termcolor**](https://github.com/tartley/colorama) |  [**Docker**](https://docs.docker.com/)      | 
| ----------------------------------------------- | ----------------------------------------------------------------------- | ------------------------------------------------------------ | ------------------------------------------------------ | --------------------------------------------------------------- | -------------------------------------------- |
| The main language used for building the project | For working with the Telegram API                                       | Telegram bot framework to handle user notifications          | For managing Python dependencies                       | For terminal coloring and enhanced logging                      | For seamless containerization and deployment |

## 🛠️ Setup Instructions

### 📋 Prerequisites
- `Docker` and `Docker Compose` installed on your machine.
- A `.env` file in the root directory containing the following environment variables:
  
    ```env
    CHANNELS_LINKS=<comma_separated_channel_links>
    KEYWORDS=<comma_separated_keywords>

    API_ID=<your_telegram_api_id>
    API_HASH=<your_telegram_api_hash>
    TELEGRAM_PHONE_NUMBER=<your_telegram_phone_number>
    TELEGRAM_PASSWORD=<your_telegram_password>

    BOT_TOKEN=<your_bot_token>
    YOUR_TELEGRAM_ID=<your_user_id>
    
    SESSION_NAME=<your_session_name>
    ```

### 🚀 Running the Application
1. Clone the repository:

    ```bash
    git clone https://github.com/Nikilandgelo/tg_parser_by_keywords.git
    cd tg_parser_by_keywords
    ```
2. Authenticate your Telegram account:

   ```bash
   docker compose run app --auth
    ```
3. Start the bot in detached mode:

   ```bash
   docker compose up -d
    ```
