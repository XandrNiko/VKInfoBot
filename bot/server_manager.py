from bot.server import Server

from config import vk_api_token

server = Server(vk_api_token, 214131328, 'test_server')
server.start()
