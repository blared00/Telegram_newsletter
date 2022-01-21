from time import sleep

from .create_bot import loop, dp


def create_newsletter(users, new_user):
    for user in users:
        sleep(1)
        loop.run_until_complete(
            dp.bot.send_message(
                chat_id=915711775,
                text=f'У нас новый друг {new_user}'
            )
        )