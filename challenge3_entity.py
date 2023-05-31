from pip._vendor import requests
from pprint import pprint

subscription_key = "2d7724d67ffe45b5a1433cca50adb02a"
endpoint = "https://language-aihackathon321.cognitiveservices.azure.com/"
entities_url = endpoint + "/text/analytics/v2.1/entities"

documents = {"documents": [
    {"id": "1", "language": "en",
     "text": "Microsoft was founded by Bill Gates and Paul Allen on April 4, 1975, to develop and sell "
             "BASIC interpreters for the Altair 8800."},
    {"id": "2", "language": "es",
     "text": "La sede principal de Microsoft se encuentra en la ciudad de Redmond, a 21 kilómetros de "
             "Seattle."}
]}

headers = {"Ocp-Apim-Subscription-Key": subscription_key}
response = requests.post(entities_url, headers=headers, json=documents)
entities = response.json()
pprint(entities)