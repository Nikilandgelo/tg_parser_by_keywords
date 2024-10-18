import logging
from os import getenv

from termcolor import colored


def check_env() -> dict | None:
    try:
        url_channels: list[str] = [
            channel.strip() for channel in getenv("CHANNELS_LINKS").split(",")
        ]
        keywords: list[str] = [
            keyword.strip() for keyword in getenv("KEYWORDS").split(",")
        ]
        api_id: str | None = getenv("API_ID")
        api_hash: str | None = getenv("API_HASH")
        tg_phone_number: str | None = getenv("TELEGRAM_PHONE_NUMBER")
        tg_password: str | None = getenv("TELEGRAM_PASSWORD")

        bot_token: str | None = getenv("BOT_TOKEN")
        target_user_id: str | None = getenv("YOUR_TELEGRAM_ID")
        if None in (
            api_id,
            api_hash,
            tg_phone_number,
            tg_password,
            bot_token,
            target_user_id,
        ):
            raise ValueError
        return {
            "channels": url_channels,
            "keywords": keywords,
            "api_id": api_id,
            "api_hash": api_hash,
            "tg_phone_number": tg_phone_number,
            "tg_password": tg_password,
            "bot_token": bot_token,
            "target_user_id": target_user_id,
        }
    except AttributeError as e:
        logging.error(
            colored(
                (
                    "Please, pass telegram channels links and keywords"
                    " in .env file."
                ),
                "red",
            )
        )
    except ValueError as e:
        logging.error(
            colored(
                ("Please, pass all telegram credentials in .env file."), "red"
            )
        )
    return None
