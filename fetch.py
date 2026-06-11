import os
import base64
import json
import time

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# MAIN CODE ======================================================
def getEmails(creds):
    try:
    # calling gmail api
        service = build("gmail", "v1", credentials=creds)
        results = (service.users().messages().list(userId="me", labelIds=["CATEGORY_PROMOTIONS", "UNREAD"]).execute())
        raw = results.get("messages", [])
        messages = {}

    # check if any message exists
        if not raw:
            print("No messages found.")
            return

        # loop raw emails
        for message in raw:
            msg = (service.users().messages().get(userId="me", id=message["id"]).execute())

            # encoding email to base64
            if "parts" in msg["payload"]:
                base64Str = msg["payload"]["parts"][0]['body']['data']
            else:
                base64Str = msg["payload"]['body']['data']
            base64Bytes = base64Str.encode()
            
            # decoding base64 to actual readable email
            messageBytes = base64.urlsafe_b64decode(base64Bytes)
            finalMessage = messageBytes.decode()

            # find subject and sender in dictionaries
            for i in (msg["payload"]["headers"]):
                if i["name"] == "Subject":
                    subject = i["value"]
            for i in (msg["payload"]["headers"]):
                if i["name"] == "From":
                    sender = i["value"]

            messages[message["id"]] = [finalMessage, sender, subject]
            print(f'Email listed!')
            time.sleep(0.5)

        base_dir = os.path.dirname(os.path.abspath(__file__))
        json_path = os.path.join(base_dir, "gitignore", "emails.json")

        # export messages into dictionary lists in new json file
        with open(json_path, 'w') as fp:
            json.dump(messages, fp, indent=4)

    # ERROR RESPONSE ======================================================
    except HttpError as error:
        # TODO(developer) - Handle errors from gmail API.
        print(f"An error occurred: {error}")