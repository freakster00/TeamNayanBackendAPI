import json
from channels.generic.websocket import AsyncWebsocketConsumer

class HazardStream(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        # Assuming the text_data contains the video frame as a string (you may need to adapt this)
        video_frame = json.loads(text_data)
        
        # Process the video frame, initialize video writer, etc.
        print('Received video frame:', video_frame)
        
        # Send acknowledgment back to the client if needed
        await self.send(text_data=json.dumps({'message': 'Video frame received'}))
