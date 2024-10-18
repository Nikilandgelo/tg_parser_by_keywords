import logging
import os

from telethon import TelegramClient
from telethon.errors.rpcerrorlist import (
    PasswordHashInvalidError,
    PhoneNumberInvalidError,
)
from termcolor import colored


class Client:

    def __init__(self, api_id, api_hash):
        self.session_name = "searching_for_messages"
        self.api_id = api_id
        self.api_hash = api_hash

    def create_user_session(self, tg_phone_number, tg_password):
        client = TelegramClient(self.session_name, self.api_id, self.api_hash)
        try:
            client.start(tg_phone_number, tg_password)
            logging.info(
                colored(
                    (
                        "Successfully logged in! Now you can just run the"
                        " command 'docker compose exec -d app python main.py'"
                        " and all will be working by its own."
                    ),
                    "green",
                )
            )
        except RuntimeError as error:
            logging.error(colored(error, "red"))
        except TypeError:
            logging.error(
                colored("Your phone number must contain only numbers.", "red")
            )
        except (PasswordHashInvalidError, PhoneNumberInvalidError):
            logging.error(
                colored(
                    (
                        "Wrong phone number or password. "
                        "Please pass your correct credentials."
                    ),
                    "red",
                )
            )

    async def get_user_client(self) -> TelegramClient:
        session_file: str = f"{self.session_name}.session"

        if os.path.exists(session_file):
            logging.info(
                colored(
                    (
                        f"Session file '{session_file}' found."
                        " Loading session..."
                    ),
                    "green",
                )
            )
            return TelegramClient(session_file, self.api_id, self.api_hash)
        else:
            raise FileNotFoundError(
                colored(
                    (
                        f"Session file '{session_file}' not found! "
                        "Please authenticate first with --auth argument."
                    ),
                    "red",
                )
            )
