from time import sleep

from tg_bot.create_bot import loop, dp
import requests
from celery import shared_task


@shared_task
def create_newsletter(users, new_user):
    for user in users:
        sleep(1)
        # print(user)
        print(requests.get('https://api.github.com/events'))
        # loop.run_until_complete(
        #     dp.bot.send_message(
        #         chat_id=915711775,
        #         text=f'У нас новый друг {new_user}'
        #     )
        # )
