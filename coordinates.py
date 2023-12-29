import requests
accessToken="2b162475-6220-4849-ba09-c3a78cff7458"
url=f"https://route-init.gallimap.com/api/v1/routing?mode=walking&srcLat=27.681948537747477&srcLng=85.31882609844881&dstLat=27.6819017485212&dstLng=85.32311312236297&accessToken={accessToken}"
x = requests.get(url)
responseJson=x.json()
print(type(responseJson["data"]))
coordinates=responseJson["data"]["data"][0]["latlngs"]
print(len(coordinates))
output=list()
for i in range(0,len(coordinates)):
    print(coordinates[i])
    entry=dict()
    entry['lat']=coordinates[i][1]
    entry['lon']=coordinates[i][0]
    output.append(entry)

print(output)