# from django.test import TestCase

# Create your tests here.
import json
import requests

data={'classes': [{"name":"其他包装饮用水（天然水）"}]}
r = requests.patch('http://127.0.0.1:8000/goods/5/', json=data)

print(r.text)