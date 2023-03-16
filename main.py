#!/usr/bin/env python3
import requests

username = input("Enter a username: ")
url = input("Enter webhook: ")

def chat():
    output = input("Msg: ")
    data = {
        "content" : output,
        "username" : username
    }
    try:
        result = requests.post(url, json = data)
        result.raise_for_status()
    except Exception as e:
        print(e)
        pass

while True:
    chat()
