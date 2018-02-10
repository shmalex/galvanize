import telnetlib
import threading
import csv
import requests
import codecs
import json

t = input()

message = t
payload = json.dumps({"text": "New Device!:" + message})

SLACK = "https://hooks.slack.com/services/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"

r = requests.post(
    SLACK,
    data=payload,
    headers={'Content-Type': 'application/json'}
)

print(r.status_code)