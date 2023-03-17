#!/usr/bin/env python3
import requests

def main():
    global commands, username, avatarURL, url

    # Defining command list 
    commands = str("\nList of commands:\n    :help Lists commands\n    :delete Deletes the webhook\n    :exit Exits the script\n")
    print(commands)

    # Requests inputs before starting
    username = input("Enter a username: ")
    avatarURL = input("Enter link to profile picture: ")
    url = input("Enter webhook: ")
    print("\n")

    chat()


def chat():
    content = input("% ")
    data = {
        "content" : content,
        "username" : username,
        "avatar_url" : avatarURL
    }

    # Verifying content
    if content == ":help":
        print(commands)
    elif content == ":exit":
        exit()
    elif content == ":delete":
        try:
            requests.delete(url)
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

    # Forever executes chat() until KeyboardInterrupt or :exit
    while True:
        chat()
    
main()