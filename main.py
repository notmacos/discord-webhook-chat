#!/usr/bin/env python3
import requests

print("""List of commands:
:delete Deletes the webhook
:exit Exits the script""")
      
username = input("\nEnter a username: ")
url = input("Enter webhook: ")

def chat():
    output = input("Msg: ")
    data = {
        "content" : output,
        "username" : username
    }

    if output == ":exit":
        exit()
    elif output == ":delete":
        try:
            requests.delete(f"{url}")
            print("Successful!")
            exit()
        except Exception as f:
            print(f)

    else:
        try:
            result = requests.post(url, json = data)
            result.raise_for_status()
        except Exception as e:
            print(e)
            pass

while True:
    chat()