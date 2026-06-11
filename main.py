import auth
import fetch

def main():
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    creds = auth.authorization() # auth.py

    # The fetch.py's task is to store email content to local email.json files.
    # Creds variable is called for the credentials from auth.py
    fetch.getEmails(creds)
    
if __name__ == "__main__":
    main()