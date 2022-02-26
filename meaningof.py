#!/usr/bin/python3

import requests
import json
import sys

n = len(sys.argv)

for i in range(1, n):
    word = sys.argv[i]

api_url = str("https://api.dictionaryapi.dev/api/v2/entries/en_US/" + word)

req = requests.get(api_url)

df = req.json()
print(df[0]["word"])

