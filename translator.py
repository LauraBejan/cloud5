import os, requests, uuid, json
from db import *
def translateText(text, to):


    if 'TRANSLATOR_TEXT_KEY' in os.environ:
        subscriptionKey = os.environ['TRANSLATOR_TEXT_KEY']
    else:
        print('Environment variable for TRANSLATOR_TEXT_KEY is not set.')
        exit()

    base_url = 'https://api.cognitive.microsofttranslator.com'
    path = '/translate?api-version=3.0'
    params = '&to={}'.format(to)
    constructed_url = base_url + path + params

    headers = {
    'Ocp-Apim-Subscription-Key': subscriptionKey,
    'Content-type': 'application/json',
    'X-ClientTraceId': str(uuid.uuid4())
    }

    body = [{
    'text' : text
    }]

    request = requests.post(constructed_url, headers=headers, json=body)
    response = request.json()

    translation =  json.dumps(response)["translations"][0]["text"]
    print(translation)
    return translation
    # , sort_keys=True, indent=4, ensure_ascii=False, separators=(',', ': '))