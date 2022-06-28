import random

import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor

from commander import Commander


class Server:
    def __init__(self, api_token, group_id, server_name: str = 'Empty'):
        self.server_name = server_name
        self.group_id = group_id

        self.vk = vk_api.VkApi(token=api_token)
        self.long_pool = VkLongPoll(self.vk, group_id=self.group_id, wait=90)
        self.vk_api = self.vk.get_api()
        self.users = {}

    def send_msg(self, send_id, message):
        return self.vk_api.messages.send(peer_id=send_id,
                                         message=message,
                                         random_id=random.randint(0, 2048),
                                         keyboard=open('keyboard.json', 'r', encoding='UTF-8').read())

    def start(self):
        for event in self.long_pool.listen():
            if event.type == VkEventType.MESSAGE_NEW and event.to_me:
                message = event.text
                user_id = event.user_id

                if user_id not in self.users:
                    self.users[user_id] = Commander()

                self.send_msg(user_id, self.users[user_id].input(message))
