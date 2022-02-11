"""import"""
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
・Create Face Client instance　-> face_client

"""

"""load env"""
load_dotenv()

"""define KEY and ENDPOINT"""
KEY = os.environ.get("KEY")
ENDPOINT = os.environ.get("ENDPOINT")

"""Create Face Client instance"""
face_client = FaceClient(ENDPOINT, CognitiveServicesCredentials(KEY))


def main():
    pass


if __name__ == '__main__':
    main()
