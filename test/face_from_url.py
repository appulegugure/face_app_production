"""import"""
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

single_face_image_url = "https://2019.images.forbesjapan.media/articles/28000/28737/photos/410x615/287372b32bafc0a65daabbbb31509e5349859.jpg"
single_image_name = os.path.basename(single_face_image_url)
# We use detection model 3 to get better performance.
detected_faces = face_client.face.detect_with_url(url=single_face_image_url, detection_model='detection_03')

face_ids_and_react = []

if not detected_faces:
    raise Exception('No face detected from image {}'.format(single_image_name))
else:
    for face in detected_faces:
        face_ids_and_react.append({'faceID': face.face_id, 'react': face.face_rectangle})
        print('face_ids_and_react:', face_ids_and_react)
