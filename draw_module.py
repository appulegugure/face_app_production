"""import"""
"""
import asyncio
import io
import glob
import os
import sys
import time
import uuid
"""

"""
from dotenv import load_dotenv
import json
from urllib.parse import urlparse
"""
# To install this module, run:
# python -m pip install Pillow
from PIL import Image, ImageDraw

"""
from azure.cognitiveservices.vision.face import FaceClient
from msrest.authentication import CognitiveServicesCredentials
from azure.cognitiveservices.vision.face.models import TrainingStatusType, Person
"""


def getRectangle(faceDictionary):
    rect = faceDictionary.face_rectangle
    left = rect.left
    top = rect.top
    right = left + rect.width
    bottom = top + rect.height

    return ((left, top), (right, bottom))


def getRectangle_ver2(faceDictionary):
    rect = faceDictionary
    left = rect.left
    top = rect.top
    right = left + rect.width
    bottom = top + rect.height

    return ((left, top), (right, bottom))

"""
def drawFaceRectangles():
    # Download the image from the url
    response = requests.get(single_face_image_url)
    img = Image.open(BytesIO(response.content))

    # For each face returned use the face rectangle and draw a red box.
    print('Drawing rectangle around face... see popup for results.')
    draw = ImageDraw.Draw(img)
    for face in detected_faces:
        draw.rectangle(getRectangle(face), outline='red')

    # Display the image in the default image browser.
    img.show()
"""

def drawFaceRectangles_ver2(image_11, array_11):
    img = Image.open(image_11)
    # For each face returned use the face rectangle and draw a red box.
    print('Drawing rectangle around face... see popup for results.')
    draw = ImageDraw.Draw(img)
    draw.rectangle(getRectangle_ver2(array_11), outline='red')

    # Display the image in the default image browser.
    img.show()
