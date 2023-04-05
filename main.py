#!/usr/bin/env python3
import requests

def main():
    # Set global variables
    global commands, username, avatarURL, url

    # Define list of commands 
    commands = str("\nList of commands:\n    :help Lists commands\n    :delete Deletes the webhook\n    :exit Exits the script\n")
    print(commands)

    # Requests inputs before starting
    username = input("Enter a username: ")
    avatarURL = input("Enter link to profile picture: ")
    url = input("Enter webhook: ")
    print("")

    chat()


def chat():
    # Get user input
    content = input("% ")

    # Create dictionary with input data
    data = {
        "content" : content,
        "username" : username,
        "avatar_url" : avatarURL
    }

    # Check if input is a command
    if content == ":help":
        print(commands)
    elif content == ":exit":
        exit()
    elif content == ":delete":
        try:
            # Send delete request to webhook URL
            requests.delete(url)
            print("Successful!")
            exit()
        except Exception as f:
            # Print error message if delete request fails
            print(f)

    else:
        # Send post request with input data to webhook URL
        try:
            result = requests.post(url, json = data)
            result.raise_for_status()
            
        # Print error message if post request fails
        except Exception as e:
            print(e)
            pass

    # Continuously execute chat() until KeyboardInterrupt or :exit
    while True:
        chat()
    
main()
