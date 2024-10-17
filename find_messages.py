from telethon.tl.types import Channel
from telethon import TelegramClient
from asyncio import create_task, gather
from telethon.functions import messages
from aiogram import Bot
import logging
from termcolor import colored


async def proceed_new_messages(client: TelegramClient, channels: list[Channel],
                               keywords: list[str], bot: Bot,
                               target_user_id: str):
    result = await client(messages.GetPeerDialogsRequest(peers=channels))
    tasks: list = []
    for index, channel in enumerate(channels):
        if result.dialogs[index].unread_count == 0:
            continue
        logging.info(
            colored(f'Found new messages in {channel.title}.', 'green')
        )
        kwargs: dict[str] = locals()
        kwargs['channel'] = channel
        kwargs['last_readed_id'] = result.dialogs[index].read_inbox_max_id
        task = create_task(find_messages(**kwargs))
        tasks.append(task)
    await gather(*tasks)


async def find_messages(client: TelegramClient, channel: Channel,
                        last_readed_id: int, keywords: list[str],
                        bot: Bot, target_user_id: str, **kwargs):
    async for message in client.iter_messages(channel):
        if last_readed_id >= message.id:
            break
        try:
            if any(keyword.lower() in message.message.lower()
                   for keyword in keywords):
                logging.info(
                    colored(f'New matching message in {channel.title}!',
                            'green')
                )
                message_link: str = (f"https://t.me/{channel.username}"
                                     f"/{message.id}")
                text: str = (
                    f"New matching message in {channel.title}, relative to"
                    f" your keywords - {','.join(keywords)}:\n\n"
                    f"{message.message}\n\nLink: {message_link}"
                )
                await bot.send_message(chat_id=target_user_id, text=text)
        except AttributeError:
            logging.warning(
                colored((f'Skipping the message in {channel.title}'
                         f' it has no text.'), 'yellow')
            )
        finally:
            await client.send_read_acknowledge(channel, message)
            logging.info(
                colored(f'Marked message as read in {channel.title}.',
                        'magenta')
            )
