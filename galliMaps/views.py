from django.shortcuts import render
from rest_framework.views import APIView
from django.http import JsonResponse
import requests
import json
class Gallimap(APIView):

    def post(self,request):
        requestBody=json.loads(request.body)
        srclatitude=requestBody['srclatitude']
        srclongitude=requestBody['srclongitude']

        dstlatitude=requestBody['dstlatitude']
        dstlongitude=requestBody['dstlongitude']

        accessToken=""
        url=f"https://route-init.gallimap.com/api/v1/routing?mode=walking&srcLat={srclatitude}&srcLng={srclongitude}&dstLat={dstlatitude}&dstLng={dstlongitude}&accessToken={accessToken}"
        x = requests.get(url)
        
        responseJson=x.json()
        coordinates=responseJson["data"]["data"][0]["latlngs"]
        
        output=list()
        for i in range(0,len(coordinates)):
            
            entry=dict()
            entry['lat']=coordinates[i][1]
            entry['lon']=coordinates[i][0]
            output.append(entry)

        return JsonResponse({
            "Data":output
        })
        




