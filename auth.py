import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/gmail.readonly"]

# TOKEN AND LOGIN PROCESS ======================================================
def authorization():
    creds = None

    base_dir = os.path.dirname(os.path.abspath(__file__))
    json_path = os.path.join(base_dir, "gitignore", "token.json")

    base_dir1 = os.path.dirname(os.path.abspath(__file__))
    json_path1 = os.path.join(base_dir1, "gitignore", "credentials.json")

    if os.path.exists(json_path):
        creds = Credentials.from_authorized_user_file(json_path, SCOPES)
    
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(json_path1, SCOPES)
            creds = flow.run_local_server(port=0)
        with open(json_path, "w") as token:
            token.write(creds.to_json())
    return creds