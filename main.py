"""import"""
import json
import os

# To install this module, run:
# python -m pip install Pillow
from azure.cognitiveservices.vision.face import FaceClient
from dotenv import load_dotenv
from msrest.authentication import CognitiveServicesCredentials

"""
initial section

・load env
・define Key and Endpoint 
・Create Face Client instance　-> face_client <object>
・Create image url from json file　-> jsn <dic>

"""

"""load env"""
load_dotenv()

"""define KEY and ENDPOINT"""
KEY = os.environ.get("KEY")
ENDPOINT = os.environ.get("ENDPOINT")

"""Create Face Client instance"""
face_client = FaceClient(ENDPOINT, CognitiveServicesCredentials(KEY))

"""Create image url from json file"""
with open('image_list.json') as f:
    jsn = json.load(f)

""" ---------- TEST section START ---------- """

"""prepare URL and file name"""
# Detect a face in an image that contains a single face
single_face_image_url = jsn["single_img_url"]["sample3"]
single_image_name = os.path.basename(single_face_image_url)

"""  -- Create detected_faces_client --  """
# We use detection model 3 to get better performance.
detected_faces = face_client.face.detect_with_url(url=single_face_image_url, detection_model='detection_03')
if not detected_faces:
    raise Exception('No face detected from image {}'.format(single_image_name))
else:
    count = 1
    for detect_face in detected_faces:
        print(detect_face)
        count += 1
    print('{}人検出'.format(count - 1))

""" ---------------- END ------------------ """


def main():
    pass


if __name__ == '__main__':
    main()
