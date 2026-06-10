import os.path
import base64
import json
import time

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/gmail.readonly"]

'''
The file token.json stores the user's access and refresh tokens, and is
created automatically when the authorization flow completes for the first
time.
'''

def main():
  creds = None
  
  # TOKEN AND LOGIN PROCESS ======================================================
  if os.path.exists("token.json"):
    creds = Credentials.from_authorized_user_file("token.json", SCOPES)
  
  # If there are no (valid) credentials available, let the user log in.
  if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
      creds.refresh(Request())
    else:
      flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
      creds = flow.run_local_server(port=0)
    with open("token.json", "w") as token:
      token.write(creds.to_json())

  # MAIN CODE ======================================================
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
    
    # export messages into dictionary lists in new json file
    with open('emails.json', 'w') as fp:
      json.dump(messages, fp, indent=4)

  # ERROR RESPONSE ======================================================
  except HttpError as error:
    # TODO(developer) - Handle errors from gmail API.
    print(f"An error occurred: {error}")

if __name__ == "__main__":
  main()