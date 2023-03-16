#!/usr/bin/env python3
import requests

url = input("Enter webhook: ")

def chat():
    output = input("Msg: ")
    data = {
        "content" : output,
        "username" : "1337#0679"
    }
    try:
        result = requests.post(url, json = data)
        result.raise_for_status()
    except Exception as e:
        print(e)
        pass

while True:
    chat()
