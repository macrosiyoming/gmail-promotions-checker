import os.path

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

  try:
    # Call the Gmail API
    service = build("gmail", "v1", credentials=creds)
    results = (
      service.users().messages().list(userId="me", labelIds=["CATEGORY_PROMOTIONS" and "UNREAD"]).execute()
    )
    messages = results.get("messages", [])

    if not messages:
      print("No messages found.")
      return

    print("Messages:")
    for message in messages:
      print(f'Message ID: {message["id"]}')
      msg = (
        service.users().messages().get(userId="me", id=message["id"]).execute()
      )
      print(f'  Subject: {msg["payload"]}')

  except HttpError as error:
    # TODO(developer) - Handle errors from gmail API.
    print(f"An error occurred: {error}")


if __name__ == "__main__":
  main()



'''
Message ID: 19dec664e9f39add
  Subject: dict_keys(['id', 'threadId', 'labelIds', 'snippet', 'payload', 'sizeEstimate', 'historyId', 'internalDate'])
Message ID: 19ddb831850732fe
  Subject: dict_keys(['id', 'threadId', 'labelIds', 'snippet', 'payload', 'sizeEstimate', 'historyId', 'internalDate'])
Message ID: 19dc905943bfbc0c
  Subject: dict_keys(['id', 'threadId', 'labelIds', 'snippet', 'payload', 'sizeEstimate', 'historyId', 'internalDate'])
Message ID: 19dc859b8ec97d4f
  Subject: dict_keys(['id', 'threadId', 'labelIds', 'snippet', 'payload', 'sizeEstimate', 'historyId', 'internalDate'])
Message ID: 19dc387797649779
  S

'''