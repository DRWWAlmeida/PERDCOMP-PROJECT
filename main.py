import json
from azure.core.exceptions import ResourceNotFoundError
from azure.core.credentials import AzureKeyCredential
from azure.ai.formrecognizer import FormRecognizerClient, FormTrainingClient


credentials = json.load(open('credentials.json'))
API_KEY = credentials['API_KEY']
ENDPOINT = credentials['ENDPOINT']

form_url = "https://raw.githubusercontent.com/Azure/azure-sdk-for-python/master/sdk/formrecognizer/azure-ai-formrecognizer/tests/sample_forms/forms/Form_1.jpg"
form_recognizer_client = FormRecognizerClient(ENDPOINT, AzureKeyCredential(API_KEY))
poller = form_recognizer_client.begin_recognize_content_from_url(form_url)
form_result = poller.result()
print(form_result)
