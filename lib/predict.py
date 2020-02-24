import sys, os

from google.cloud import automl
from google.auth.credentials import Credentials
from google.oauth2 import service_account

PROJECT_ID = 'REPLACE WITH YOUR PROJECT_ID
MODEL_ID = 'REPLACE WITH YOUR MODEL_ID'

def get_prediction(content):
    prediction_client = automl.PredictionServiceClient.from_service_account_file(os.path.dirname(__file__) + '/service.json')
    name = 'projects/{}/locations/us-central1/models/{}'.format(PROJECT_ID, MODEL_ID)
    payload = {'image': {'image_bytes': content }}
    params = {'score_threshold': '0.1'}
    return prediction_client.predict(name, payload, params)
