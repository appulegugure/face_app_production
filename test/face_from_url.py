"""import"""
import glob
import os

from azure.cognitiveservices.vision.face import FaceClient
from dotenv import load_dotenv
from msrest.authentication import CognitiveServicesCredentials

# To install this module, run:
# python -m pip install Pillow

"""load env"""
load_dotenv()

"""define KEY and ENDPOINT"""
KEY = os.environ.get("KEY")
ENDPOINT = os.environ.get("ENDPOINT")

"""Create Face Client instance"""
face_client = FaceClient(ENDPOINT, CognitiveServicesCredentials(KEY))
"""
image_url = 'https://www3.nhk.or.jp/news/html/20210612/K10013081171_2106120544_2106120546_01_02.jpg'

face_ids_and_react = []

faces = face_client.face.detect_with_url(url=image_url, detection_model='detection_03')
for face in faces:
    face_ids_and_react.append({'faceID': face.face_id, 'react': face.face_rectangle})
    print('face_ids_and_react:', face_ids_and_react)
"""

test_image_array = glob.glob('../test_image_dir/face_api_test1.png')
image = open('../test_image_dir/face_api_test1.png', 'r+b')

# We use detection model 3 to get better performance.
print('____point 1____')
detected_faces = face_client.face.detect_with_stream(image, detection_model='detection_03')
print('____point 2____')

face_ids_and_react = []

if not detected_faces:
    raise Exception('No face detected from image {}')
else:
    for face in detected_faces:
        face_ids_and_react.append({'faceID': face.face_id, 'react': face.face_rectangle})
        print('face_ids_and_react:', face_ids_and_react)
