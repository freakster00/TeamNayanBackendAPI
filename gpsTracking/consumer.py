import json
from channels.generic.websocket import AsyncWebsocketConsumer
import jwt,time

class MyGpsTracker(AsyncWebsocketConsumer):
    http_user_and_session = True
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        headers = self.scope['headers']
        print(headers)
        token_to_verify = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzAzNjQ5NjczLCJpYXQiOjE3MDM2NDkzNzMsImp0aSI6Ijc4ZThiOWYwZjA3ODQ1YjRhNTdhMjc2ZDc0MDkyNmNhIiwidXNlcl9pZCI6Mn0.P642ZTAepfYu7l9nBTP-82UBW9fAyVtuTfH2EpZCCeQ"
        
        your_secret_key="django-insecure-i9sk5081s^y__1317$spj^vbl$15+6e^go3f4)sflf0ter4qq!"
        jwtStatus=is_jwt_valid(token_to_verify,your_secret_key)
        if jwtStatus:
            jsonBody=json.loads(text_data)
            latitude=jsonBody['latitude']
            longitude=jsonBody['longitude']

            response_data = {
                "Success":True,
                "Message":"Location Updated"
            }

            
            await self.send(text_data=json.dumps(response_data))
        else:
            response_data={
                "Success":False,
                "Message":"Authentication Failed"
            }
            await self.send(text_data=json.dumps(response_data))

   

    

def is_jwt_valid(token, secret_key):
    try:
        # Verify the signature using the secret key
        jwt.decode(token, secret_key, algorithms=['HS256'])

        # Optionally, check token claims (expiration, issuer, audience, etc.)
        # Example: Check if the token is not expired
        current_time = time.time()
        decoded_payload = jwt.decode(token, options={"verify_signature": False})
        if 'exp' in decoded_payload and decoded_payload['exp'] < current_time:
            return False

        # Add more claim checks as needed

        # If all checks pass, return True
        return True

    except jwt.PyJWTError:
        # Return False for any decoding or verification errors
        return False


    

