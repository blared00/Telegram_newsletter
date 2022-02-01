from time import sleep

import requests
from celery import shared_task

# from tg_bot.create_bot import dp, loop


@shared_task
def create_newsletter(users, new_user):
    for user in users:
        sleep(1)
        # print(user)
        # print(requests.get('https://api.github.com/events'))
        # loop.run_until_complete(
        #     dp.bot.send_message(
        #         chat_id=915711775,
        #         text=f'У нас новый друг {new_user}'
        #     )
        # )
        requests.post(
            url='https://api.telegram.org/bot1958198086:AAEmclu_j-YqEeG6-5n4Tob5Dn-Tk5lgqLY/sendMessage',
            data={
                'chat_id': 915711775,
                'text': f'У нас новый друг {new_user}'
            }
        )
