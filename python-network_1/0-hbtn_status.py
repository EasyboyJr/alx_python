<<<<<<< HEAD
import requests
# req = requests.get('https://alu-intranet.hbtn.io/status')
# print(req)
print(requests.__version__)
=======
"""
A module that request a URL.
"""
import requests

req = requests.get('https://alu-intranet.hbtn.io/status')
print("Body response:")
print("\t- type:", type(req.text))
print("\t- content:", req.text)
>>>>>>> 2bf429e2e0b936d31076e69a390ccbf663358937
