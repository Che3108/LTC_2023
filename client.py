#!/usr/bin/python3

import requests


URL = 'http://185.246.65.175:8008/upload'
ARHIVE_name = '/content/DATA_Files (1).zip'

files = [
    ('file', (ARHIVE_name, open(ARHIVE_name, 'rb'))),
]
response = requests.post(URL, files=files)
print(response.text)
