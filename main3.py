"""import"""
import glob
import json
import os
import sys
import time
# To install this module, run:
# python -m pip install Pillow
import uuid

from PIL import Image
from azure.cognitiveservices.vision.face import FaceClient
from azure.cognitiveservices.vision.face.models import TrainingStatusType
from dotenv import load_dotenv
from msrest.authentication import CognitiveServicesCredentials

# original module
import draw_module as draw

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
    japan_g = face_client.person_group_person.create(PERSON_GROUP_ID, "japan")
    container.append({'person': 'japan', 'data': {'name': 'FUMIO KISHIDA', 'person_ID': japan_g.person_id}})
    print("person_group_person person_id {}".format(japan_g.person_id))
    # Define man friend
    america_g = face_client.person_group_person.create(PERSON_GROUP_ID, "america")
    container.append({'person': 'america', 'data': {'name': 'JOE BIDEN', 'person_ID': america_g.person_id}})
    print("person_group_person person_id {}".format(america_g.person_id))
    # Define child friend
    igirisu_g = face_client.person_group_person.create(PERSON_GROUP_ID, "igirisu")
    container.append({'person': 'igirisu', 'data': {'name': 'BORIS JOHNSON', 'person_ID': igirisu_g.person_id}})
    print("person_group_person person_id {}".format(igirisu_g.person_id))
    # Define
    flance_g = face_client.person_group_person.create(PERSON_GROUP_ID, "flance")
    container.append({'person': 'flance', 'data': {'name': 'EMMANUEL MACRON', 'person_ID': flance_g.person_id}})
    print("person_group_person person_id {}".format(flance_g.person_id))
    # Define
    italy_g = face_client.person_group_person.create(PERSON_GROUP_ID, "italy")
    container.append({'person': 'italy', 'data': {'name': 'MARIO DRAGHI', 'person_ID': italy_g.person_id}})
    print("person_group_person person_id {}".format(italy_g.person_id))
    # Define
    canada_g = face_client.person_group_person.create(PERSON_GROUP_ID, "canada")
    container.append({'person': 'canada', 'data': {'name': 'JUSTIN TRUDEAU', 'person_ID': canada_g.person_id}})
    print("person_group_person person_id {}".format(canada_g.person_id))
    # Define
    doitu_g = face_client.person_group_person.create(PERSON_GROUP_ID, "doitu")
    container.append({'person': 'doitu', 'data': {'name': 'OLAF SCHOLZ', 'person_ID': doitu_g.person_id}})
    print("person_group_person person_id {}".format(doitu_g.person_id))
    # Find all jpeg images of friends in working directory

    """ルートから　*jpgを取得　ファイル名からグループを振り分けるためifでフィルター"""
    # -->> from url file
    with open('image_dir/naikaku_list/g7_member_list.json') as f:
        jsn = json.load(f)

    japan = [file for file in jsn['g7memberlist']['japan']]
    america = [file for file in jsn['g7memberlist']['america']]
    igirisu = [file for file in jsn['g7memberlist']['igirisu']]
    flance = [file for file in jsn['g7memberlist']['flance']]
    italy = [file for file in jsn['g7memberlist']['italy']]
    canada = [file for file in jsn['g7memberlist']['canada']]
    doitu = [file for file in jsn['g7memberlist']['doitu']]

    print(japan)
    print(america)
    print(igirisu)
    # image array 確認
    print('container:', container)
    print('japan:', japan)
    print('america:', america)
    print('igirisu:', igirisu)
    print('flance:', flance)
    print('italy:', italy)
    print('canada:', canada)
    print('canada:', doitu)
    """.add_face_from_streamを通して画像ファイルを追加していく"""
    # Add to a woman person
    for image in japan:
        # w = open(image, 'r+b')
        face_client.person_group_person.add_face_from_url(PERSON_GROUP_ID, japan_g.person_id, image)

    # Add to a man person
    for image in america:
        # m = open(image, 'r+b')
        face_client.person_group_person.add_face_from_url(PERSON_GROUP_ID, america_g.person_id, image)

    # Add to a child person
    for image in igirisu:
        # ch = open(image, 'r+b')
        face_client.person_group_person.add_face_from_url(PERSON_GROUP_ID, igirisu_g.person_id, image)

    for image in flance:
        # ch = open(image, 'r+b')
        face_client.person_group_person.add_face_from_url(PERSON_GROUP_ID, flance_g.person_id, image)

    for image in italy:
        # ch = open(image, 'r+b')
        face_client.person_group_person.add_face_from_url(PERSON_GROUP_ID, italy_g.person_id, image)

    for image in canada:
        # ch = open(image, 'r+b')
        face_client.person_group_person.add_face_from_url(PERSON_GROUP_ID, canada_g.person_id, image)

    for image in doitu:
        # ch = open(image, 'r+b')
        face_client.person_group_person.add_face_from_url(PERSON_GROUP_ID, doitu_g.person_id, image)

    print('-------------------------------------savepoint-------------------------------------')
    '''
    Train PersonGroup
    '''
    print()
    print('Training the person group...')
    # Train the person group
    face_client.person_group.train(PERSON_GROUP_ID)

    while True:
        training_status = face_client.person_group.get_training_status(PERSON_GROUP_ID)
        print("Training status: {}.".format(training_status.status))
        print()
        if training_status.status is TrainingStatusType.succeeded:
            break
        elif training_status.status is TrainingStatusType.failed:
            face_client.person_group.delete(person_group_id=PERSON_GROUP_ID)
            sys.exit('Training the person group has failed.')
        time.sleep(5)

    '''
    Identify a face against a defined PersonGroup
    '''
    # Group image for testing against
    test_image_array = glob.glob('test_image_dir/face_api_test7.png')
    image = open(test_image_array[0], 'r+b')
    # image = "test_image_dir/287372b32bafc0a65daabbbb31509e5349859.jpg"
    # img = open(image, 'r+b')

    print('Pausing for 60 seconds to avoid triggering rate limit on free account...')
    time.sleep(60)

    # Detect faces
    # face_ids_and_react は　検出された顔のfaceid と react を格納するコンテナ
    face_ids_and_react = []
    # We use detection model 3 to get better performance.
    faces = face_client.face.detect_with_stream(image, detection_model='detection_03')
    for face in faces:
        face_ids_and_react.append({'faceID': face.face_id, 'react': face.face_rectangle})
        print('face_ids_and_react:', face_ids_and_react)
    # Identify faces
    results = face_client.face.identify([faceIDs['faceID'] for faceIDs in face_ids_and_react[:10]], PERSON_GROUP_ID)
    # results = face_client.face.identify([faceIDs['faceID'] for faceIDs in face_ids_and_react], PERSON_GROUP_ID)

    print('result:', results)

    # results のadditional ﾌﾟﾛﾊﾟﾃｨにreact データを追加
    for i in results:
        for u in face_ids_and_react:

            # print(i)
            # print(u)
            # print(i.face_id)
            # print(u['faceID'])

            if i.face_id == u['faceID']:
                add_pro = {'react': u['react']}
                # i.additional_properties.append(add_pro)
                # i['additional_properties'] = add_pro
                i.additional_properties.update(add_pro)

    print(results[0])

    # open draw base image
    img = Image.open(test_image_array[0])

    # person filter list
    personlist_g = ['japan', 'america', 'flance', 'canada', 'italy', 'doitu', 'igirisu']

    for rest in results:
        for cont in container:
            print(cont)
            # 人物フィルター
            if cont['person'] in personlist_g:
                # if cont['person'] == 'igirisu'or cont['person'] == "flance" or cont['person'] == "canada":
                if len(rest.candidates) > 0:
                    if rest.candidates[0].person_id == cont['data']['person_ID']:
                        # if rest.candidates.person_id == cont['data']['person_ID']:
                        # if rest.candidates[0].person_id == cont["person_ID"]:
                        print('------')
                        print(cont['data']["name"])
                        print(rest.additional_properties['react'])
                        messag = rest.additional_properties['react']
                        print(messag)
                        draw.drawFaceRectangles_ver2(test_image_array[0], rest.additional_properties['react'], img,
                                                     cont['data']["name"])
                    # draw.drawText(test_image_array[0])

    img.show()

    # for cont in container:
    #    if results[0].candidates[0].person_id == cont["person_ID"]:
    #        print(cont["name"])

    print('Identifying faces in {}'.format(os.path.basename(image.name)))
    if not results:
        print('No person identified in the person group for faces from {}.'.format(os.path.basename(image.name)))
    for person in results:
        if len(person.candidates) > 0:
            print('Person for face ID {} is identified in {} with a confidence of {}.'.format(person.face_id,
                                                                                              os.path.basename(
                                                                                                  image.name),
                                                                                              person.candidates[
                                                                                                  0].confidence))  # Get topmost confidence score
        else:
            print('No person identified for face ID {} in {}.'.format(person.face_id, os.path.basename(image.name)))


if __name__ == '__main__':
    main()

# 写真リストを動的に
# image draw変更
# 後で消します
