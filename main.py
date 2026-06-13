import auth
import fetch
import analyzer

def main():
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    creds = auth.authorization() # auth.py

    # The fetch.py's task is to store email content to local email.json files.
    # Creds variable is called for the credentials from auth.py
    fetch.getEmails(creds)

    # AI analyzes which emails contains offers, extracts codes, and lists
    # additional information regarding the promotional email.
    # NOT TESTED IN MAIN.PY
    analyzer.analysis(analyzer.emails)
    
if __name__ == "__main__":
    main()