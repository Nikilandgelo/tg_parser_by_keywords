import argparse
import logging
from asyncio import gather, run, sleep

from aiogram import Bot
from aiogram.exceptions import (
    TelegramBadRequest,
    TelegramForbiddenError,
    TelegramUnauthorizedError,
)
from colorama import just_fix_windows_console
from dotenv import load_dotenv
from telethon.tl.types import Channel
from termcolor import colored

from auth import Client
from env_checker import check_env
from find_messages import proceed_new_messages


async def main(env_variables: dict):
    tg_client = Client(
        env_variables.get("session_name"),
        env_variables.get("api_id"),
        env_variables.get("api_hash"),
    )
    bot = Bot(token=env_variables.get("bot_token"))
    target_user_id = env_variables.get("target_user_id")
    try:
        tg_client, _, _ = await gather(
            tg_client.get_user_client(),
            bot.get_me(),
            bot.send_message(target_user_id, "⚙️ Start working..."),
        )
    except (
        TelegramUnauthorizedError,
        TelegramBadRequest,
        TelegramForbiddenError,
    ):
        logging.error(
            colored(
                (
                    "Can not send you a message, check your bot token"
                    ", recipient ID and if everything right, check if bot"
                    " is not blocked by you."
                ),
                "red",
            )
        )
        return

    async with tg_client:
        url_channels = env_variables.get("channels")
        logging.info(
            colored(f"Getting {len(url_channels)} channels...", "cyan")
        )
        try:
            channels: list[Channel] = await tg_client.get_entity(url_channels)
            while True:
                logging.info(
                    colored("Start searching for new messages!", "magenta")
                )
                await proceed_new_messages(
                    tg_client,
                    channels,
                    env_variables.get("keywords"),
                    bot,
                    target_user_id,
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
    if env_variables := check_env():
        parser = argparse.ArgumentParser(
            description="Telegram Keyword Parser Bot"
        )
        parser.add_argument(
            "--auth",
            action="store_true",
            help="Run authentication for Telegram",
        )
        args = parser.parse_args()
        if args.auth:
            logging.info(
                colored("Running first-time authentication...", "cyan")
            )
            Client(
                env_variables.get("session_name"),
                env_variables.get("api_id"),
                env_variables.get("api_hash"),
            ).create_user_session(
                env_variables.get("tg_phone_number"),
                env_variables.get("tg_password"),
            )
        else:
            run(main(env_variables))
