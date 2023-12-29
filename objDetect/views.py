from rest_framework.response import Response
from rest_framework.views import APIView
import json
from objDetect.yolov.detect import peopleCounter

class ImageDetect(APIView):

    def get(self,request,format=None):
        body=json.loads(request.body)
        imageUrl=body['ImageUrl']
        count=peopleCounter(imageUrl)
        return Response({
            "Success":"True",
            "Message":count
        })
