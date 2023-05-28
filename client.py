#!/usr/bin/python3

import requests
import pandas as pd


URL = 'http://62.109.6.118:8008/upload'
ARHIVE_name = '/content/DATA_Files (1).zip'

files = [
    ('file', (ARHIVE_name, open(ARHIVE_name, 'rb'))),
]
response = requests.post(URL, files=files)
print(response.text)
