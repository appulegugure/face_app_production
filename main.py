"""import"""
import glob
import json
import os
# To install this module, run:
# python -m pip install Pillow
import uuid

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
"""#
# Detect a face in an image that contains a single face
single_face_image_url = jsn["single_img_url"]["sample3"]
single_image_name = os.path.basename(single_face_image_url)
#"""
"""  -- Create detected_faces_client --  """
"""#
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
#"""

""" ---------------- END ------------------ """


def main():
    """Create PERSON GROUP ID"""
    PERSON_GROUP_ID = str(uuid.uuid4())

    # PERSON_GROUP_ID 確認
    print('Person group:', PERSON_GROUP_ID)

    """ Create container """
    container = []

    # PERSON_GROUP_ID 確認
    print('container:', container)

    """Define person groupをを作成"""
    face_client.person_group.create(person_group_id=PERSON_GROUP_ID, name=PERSON_GROUP_ID)

    # face_client　確認
    print('face client:', face_client)

    """person group の中のpersonを作る"""
    # Define woman friend
    woman = face_client.person_group_person.create(PERSON_GROUP_ID, "Woman")
    container.append({'person': 'Woman', 'data': {'name': 'Woman', 'person_ID': woman.person_id}})
    print("person_group_person person_id {}".format(woman.person_id))
    # Define man friend
    man = face_client.person_group_person.create(PERSON_GROUP_ID, "Man")
    container.append({'person': 'Man', 'data': {'name': 'Man', 'person_ID': man.person_id}})
    print("person_group_person person_id {}".format(man.person_id))
    # Define child friend
    child = face_client.person_group_person.create(PERSON_GROUP_ID, "Child")
    container.append({'person': 'Child', 'data': {'name': 'child', 'person_ID': child.person_id}})
    print("person_group_person person_id {}".format(child.person_id))
    # Find all jpeg images of friends in working directory

    """ルートから　*jpgを取得　ファイル名からグループを振り分けるためifでフィルター"""
    # -->>
    woman_images = [file for file in glob.glob('image_dir/*.jpg') if file.startswith("image_dir/m")]
    man_images = [file for file in glob.glob('image_dir/*.jpg') if file.startswith("image_dir/w")]
    child_images = [file for file in glob.glob('image_dir/*.jpg') if file.startswith("image_dir/ch")]

    # image array 確認
    print('container:', container)
    print('woman_images:', woman_images)
    print('man_images:', man_images)
    print('child_images:', child_images)

if __name__ == '__main__':
    main()
