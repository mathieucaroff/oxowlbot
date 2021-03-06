"""
This type stub file was generated by pyright.
"""

class ApplicationCommunicator:
    """
    Runs an ASGI application in a test mode, allowing sending of
    messages to it and retrieval of messages it sends.
    """
    def __init__(self, application, scope):
        self.application = ...
        self.scope = ...
        self.input_queue = ...
        self.output_queue = ...
        self.future = ...
    
    async def wait(self, timeout=...):
        """
        Waits for the application to stop itself and returns any exceptions.
        """
        ...
    
    def stop(self, exceptions: bool = ...):
        ...
    
    def __del__(self):
        ...
    
    async def send_input(self, message):
        """
        Sends a single message to the application
        """
        ...
    
    async def receive_output(self, timeout=...):
        """
        Receives a single message from the application, with optional timeout.
        """
        ...
    
    async def receive_nothing(self, timeout=..., interval=...):
        """
        Checks that there is no message to receive in the given time.
        """
        ...
    


