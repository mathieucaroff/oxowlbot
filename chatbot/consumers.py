import json

from channels.generic.websocket import AsyncWebsocketConsumer

from questionbot.main import Questionbot


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.bot = Questionbot()
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]

        json_data = json.dumps({"author": "self", "text": message})

        await self.send(text_data=json_data)

        answer = await self.bot.process(message)

        json_data = json.dumps({"author": "bot", **answer.asdict()})

        await self.send(text_data=json_data)
