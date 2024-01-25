import json
from openpyxl import Workbook, load_workbook
from azure.core.credentials import AzureKeyCredential
from azure.ai.formrecognizer import DocumentAnalysisClient
import time
from tkinter import *
from tkinter.filedialog import askopenfilenames

credentials = json.load(open('credentials.json'))
API_KEY = credentials['API_KEY']
ENDPOINT = credentials['ENDPOINT']
document_analysis_client = DocumentAnalysisClient(ENDPOINT, AzureKeyCredential(API_KEY))


with open('sample-layout.pdf', "rb") as file:
    poller = document_analysis_client.begin_analyze_document(model_id="prebuilt-document", document=file)
    result = poller.result()
    print("----Key-value pairs found in document----")
    for kv_pair in result.key_value_pairs:
        if kv_pair.key and kv_pair.value:
            print("Key '{}': Value: '{}'".format(kv_pair.key.content, kv_pair.value.content))
        else:
            print("Key '{}': Value:".format(kv_pair.key.content))

    print("----------------------------------------")