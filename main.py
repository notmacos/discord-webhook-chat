#!/usr/bin/env python3
import requests

print("""List of commands:
:delete Deletes the webhook
:exit Exits the script""")
      
# Requests inputs before starting
username = input("\nEnter a username: ")
avatarURL = input("Enter link to profile picture: ")
url = input("Enter webhook: ")


def chat():
    content = input("% ")
    data = {
        "content" : content,
        "username" : username,
        "avatar_url" : avatarURL
    }

    # Verifying content
    if content == ":exit":
        exit()
    elif content == ":delete":
        try:
            requests.delete(f"{url}")
            print("Successful!")
            exit()
        except Exception as f:
            print(f)

    else:
        # Posts content to webhook
        try:
            result = requests.post(url, json = data)
            result.raise_for_status()
            
        # Prints error if post fails
        except Exception as e:
            print(e)
            pass

# Forever executes chat() until Keyboard Interrupt or :exit
while True:
    chat()