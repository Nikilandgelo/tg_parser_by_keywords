import logging
from asyncio import run, sleep
from os import getenv, environ

from aiogram import Bot
from colorama import just_fix_windows_console
from dotenv import load_dotenv
from telethon import TelegramClient
from telethon.tl.types import Channel
from termcolor import colored

from find_messages import proceed_new_messages


async def main():
    api_id: str | None = getenv("API_ID")
    api_hash: str | None = getenv("API_HASH")
    url_channels: list[str] = [
        channel.strip() for channel in getenv("CHANNELS_LINKS").split(",")
    ]
    keywords: list[str] = [
        keyword.strip() for keyword in getenv("KEYWORDS").split(",")
    ]
    bot_token: str | None = getenv("BOT_TOKEN")
    target_user_id: str | None = getenv("YOUR_TELEGRAM_ID")

    client = TelegramClient("searching_for_messages", api_id, api_hash)
    bot = Bot(token=bot_token)
    async with client:
        logging.info(
            colored(f"Getting {len(url_channels)} channels...", "cyan")
        )
        try:
            channels: list[Channel] = await client.get_entity(url_channels)
            while True:
                logging.info(
                    colored("Start searching for new messages!", "magenta")
                )
                await proceed_new_messages(
                    client, channels, keywords, bot, target_user_id
                )
                logging.info(colored("Time to sleep...", "cyan"))
                await sleep(300)
        except ValueError as e:
            logging.error(
                colored(
                    f"Error fetching messages from {url_channels}:\n{e}", "red"
                )
            )


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format="{asctime} - {levelname}: {message}\n",
        style="{",
    )
    just_fix_windows_console()
    load_dotenv(override=True)
    run(main())
