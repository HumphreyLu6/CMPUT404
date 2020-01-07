import requests

var = requests.get("https://raw.githubusercontent.com/HumphreyLu6/CMPUT404/master/lab1/lab1.py")

print(var.content)