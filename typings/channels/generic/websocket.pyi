"""
This type stub file was generated by pyright.
"""

from ..consumer import AsyncConsumer, SyncConsumer
from typing import Any, Optional

class WebsocketConsumer(SyncConsumer):
    """
    Base WebSocket consumer. Provides a general encapsulation for the
    WebSocket handling model that other applications can build on.
    """
    groups = ...
    def __init__(self, *args, **kwargs):
        ...
    
    def websocket_connect(self, message):
        """
        Called when a WebSocket connection is opened.
        """
        ...
    
    def connect(self):
        ...
    
    def accept(self, subprotocol: Optional[Any] = ...):
        """
        Accepts an incoming socket
        """
        ...
    
    def websocket_receive(self, message):
        """
        Called when a WebSocket frame is received. Decodes it and passes it
        to receive().
        """
        ...
    
    def receive(self, text_data: Optional[Any] = ..., bytes_data: Optional[Any] = ...):
        """
        Called with a decoded WebSocket frame.
        """
        ...
    
    def send(self, text_data: Optional[Any] = ..., bytes_data: Optional[Any] = ..., close: bool = ...):
        """
        Sends a reply back down the WebSocket
        """
        ...
    
    def close(self, code: Optional[Any] = ...):
        """
        Closes the WebSocket from the server end
        """
        ...
    
    def websocket_disconnect(self, message):
        """
        Called when a WebSocket connection is closed. Base level so you don't
        need to call super() all the time.
        """
        ...
    
    def disconnect(self, code):
        """
        Called when a WebSocket connection is closed.
        """
        ...
    


class JsonWebsocketConsumer(WebsocketConsumer):
    """
    Variant of WebsocketConsumer that automatically JSON-encodes and decodes
    messages as they come in and go out. Expects everything to be text; will
    error on binary data.
    """
    def receive(self, text_data: Optional[Any] = ..., bytes_data: Optional[Any] = ..., **kwargs):
        ...
    
    def receive_json(self, content, **kwargs):
        """
        Called with decoded JSON content.
        """
        ...
    
    def send_json(self, content, close: bool = ...):
        """
        Encode the given content as JSON and send it to the client.
        """
        ...
    
    @classmethod
    def decode_json(cls, text_data):
        ...
    
    @classmethod
    def encode_json(cls, content):
        ...
    


class AsyncWebsocketConsumer(AsyncConsumer):
    """
    Base WebSocket consumer, async version. Provides a general encapsulation
    for the WebSocket handling model that other applications can build on.
    """
    groups = ...
    def __init__(self, *args, **kwargs):
        ...
    
    async def websocket_connect(self, message):
        """
        Called when a WebSocket connection is opened.
        """
        ...
    
    async def connect(self):
        ...
    
    async def accept(self, subprotocol: Optional[Any] = ...):
        """
        Accepts an incoming socket
        """
        ...
    
    async def websocket_receive(self, message):
        """
        Called when a WebSocket frame is received. Decodes it and passes it
        to receive().
        """
        ...
    
    async def receive(self, text_data: Optional[Any] = ..., bytes_data: Optional[Any] = ...):
        """
        Called with a decoded WebSocket frame.
        """
        ...
    
    async def send(self, text_data: Optional[Any] = ..., bytes_data: Optional[Any] = ..., close: bool = ...):
        """
        Sends a reply back down the WebSocket
        """
        ...
    
    async def close(self, code: Optional[Any] = ...):
        """
        Closes the WebSocket from the server end
        """
        ...
    
    async def websocket_disconnect(self, message):
        """
        Called when a WebSocket connection is closed. Base level so you don't
        need to call super() all the time.
        """
        ...
    
    async def disconnect(self, code):
        """
        Called when a WebSocket connection is closed.
        """
        ...
    


class AsyncJsonWebsocketConsumer(AsyncWebsocketConsumer):
    """
    Variant of AsyncWebsocketConsumer that automatically JSON-encodes and decodes
    messages as they come in and go out. Expects everything to be text; will
    error on binary data.
    """
    async def receive(self, text_data: Optional[Any] = ..., bytes_data: Optional[Any] = ..., **kwargs):
        ...
    
    async def receive_json(self, content, **kwargs):
        """
        Called with decoded JSON content.
        """
        ...
    
    async def send_json(self, content, close: bool = ...):
        """
        Encode the given content as JSON and send it to the client.
        """
        ...
    
    @classmethod
    async def decode_json(cls, text_data):
        ...
    
    @classmethod
    async def encode_json(cls, content):
        ...
    


