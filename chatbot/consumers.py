import json
from channels.generic.websocket import AsyncWebsocketConsumer

from .oxbot.oxbot import Oxbot

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.bot = Oxbot()
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        await self.send(text_data=json.dumps({
            'message': f"ME : {message}"
        }))

        answer = await self.bot.process(message)

        await self.send(text_data=json.dumps({
            'message': f"BOT: {answer}"
        }))
