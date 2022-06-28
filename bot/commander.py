from command_enum import Command


class Commander:
    def __init__(self):
        self.url_beginner_guide = 'https://vk.com/@rwp_rwp-novichku-v-revolucionnoi-rabochei-partii'

    def input(self, message: str):
        if message in Command.beginner_guide.value:
            return 'Че то там'

        if message in Command.activity.value:
            return '...'

        return 'None'
