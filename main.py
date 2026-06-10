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

def main():
  """Shows basic usage of the Gmail API.
  Lists the user's Gmail labels.
  """
  creds = None
  # The file token.json stores the user's access and refresh tokens, and is
  # created automatically when the authorization flow completes for the first
  # time.
  if os.path.exists("token.json"):
    creds = Credentials.from_authorized_user_file("token.json", SCOPES)
  # If there are no (valid) credentials available, let the user log in.
  if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
      creds.refresh(Request())
    else:
      flow = InstalledAppFlow.from_client_secrets_file(
          "credentials.json", SCOPES
      )
      creds = flow.run_local_server(port=0)
    # Save the credentials for the next run
    with open("token.json", "w") as token:
      token.write(creds.to_json())

  # WHERE ALL THE CODE STARTS
  try:
    # Call the Gmail API
    service = build("gmail", "v1", credentials=creds)
    results = (
      service.users().messages().list(userId="me", labelIds=["CATEGORY_PROMOTIONS", "UNREAD"]).execute()
    )
    raw = results.get("messages", [])

    if not raw:
      print("No messages found.")
      return

    messages = {}

    for message in raw:
      msg = (
        service.users().messages().get(userId="me", id=message["id"]).execute()
      )
      if "parts" in msg["payload"]:
        base64Str = msg["payload"]["parts"][0]['body']['data']
      else:
        base64Str = msg["payload"]['body']['data']
      base64Bytes = base64Str.encode()

      messageBytes = base64.urlsafe_b64decode(base64Bytes)
      finalMessage = messageBytes.decode()
      for i in (msg["payload"]["headers"]):
        if i["name"] == "Subject":
          subject = i["value"]

      for i in (msg["payload"]["headers"]):
        if i["name"] == "From":
          sender = i["value"]

      messages[message["id"]] = [finalMessage, sender, subject]
      print(f'Email listed!')
      time.sleep(0.5)
    
    with open('emails.json', 'w') as fp:
      json.dump(messages, fp, indent=4)

  except HttpError as error:
    # TODO(developer) - Handle errors from gmail API.
    print(f"An error occurred: {error}")

if __name__ == "__main__":
  main()