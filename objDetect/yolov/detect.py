from ultralytics import YOLO
import requests
from PIL import Image
import numpy as np
from io import BytesIO

model = YOLO('yolov8x.pt')

def peopleCounter(imageUrl):
    image_url = imageUrl

    response = requests.get(image_url)
    image = Image.open(BytesIO(response.content))
    results = model(image)
    cls_values = results[0].boxes.cls.cpu().numpy().flatten()
    counter = np.count_nonzero(cls_values == 0)
    return counter

# totalPeople=peopleCounter("https://www.shutterstock.com/image-photo/perfect-team-group-three-cheerful-260nw-1478368496.jpg")
# print(totalPeople)