import json

from channels.generic.websocket import AsyncWebsocketConsumer

from questionbot.answer import Answer
from questionbot.main import Questionbot
from questionbot.util.eprint import eprint

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

        try:
            answer = await self.bot.process(message)
        except Exception as e:
            eprint('-' * 42)
            import traceback as tb; tb.print_exc()
            eprint(f"\nCaused by message: {repr(message)}")
            eprint('=' * 42)
            answer = Answer("failure", text="I bugged\n", info=f"Server Error: {e}")

        json_data = json.dumps({"author": "bot", **answer.asdict()})

        await self.send(text_data=json_data)
