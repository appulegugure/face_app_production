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
from PIL import ImageDraw

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


def getTextPos(faceDictionary, textsize=0, linewidth=0):
    rect = faceDictionary
    left = rect.left
    top = (rect.top - textsize - linewidth // 2)

    return (left, top)


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


def drawFaceRectangles_ver2(image_11, array_11, img, text="who are you?"):
    # img = Image.open(image_11)
    # For each face returned use the face rectangle and draw a red box.
    print('Drawing rectangle around face... see popup for results.')
    draw = ImageDraw.Draw(img)
    draw.rectangle(getRectangle_ver2(array_11), outline='red', width=4)
    textcolor = (255, 0, 0)
    rectcolor = (255, 0, 0)
    textsize = 14
    linewidth = 4
    left, top = (161, 50)  # 矩形の左上の座標(x, y)をleft, topという変数に格納
    # txpos = (left, top - textsize - linewidth // 2)
    draw.text(getTextPos(array_11, textsize, linewidth), text, fill=textcolor)
    # txw, txh = draw.textsize(text)
    # left_f, top_g = getTextPos(array_11)
    # draw.rectangle([getTextPos(array_11), (left_f + txw, top_g)], \
    # outline=rectcolor, fill=rectcolor, width=linewidth)
    # Display the image in the default image browser.
    # img.show()


def drawText(img):
    draw = ImageDraw.Draw(img)  # 矩形の描画の準備

    rectcolor = (255, 0, 0)  # 矩形の色(RGB)。red
    linewidth = 4  # 線の太さ
    draw.rectangle([(161, 50), (260, 162)], \
                   outline=rectcolor, width=linewidth)  # 矩形の描画
