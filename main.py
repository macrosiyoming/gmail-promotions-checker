import auth
import fetch
import analyzer

def main():
    try:
        # The file token.json stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        creds = auth.authorization() # auth.py

        # # The fetch.py's task is to store email content to local email.json files.
        # # Creds variable is called for the credentials from auth.py
        fetch.getEmails(creds=creds)

        # AI analyzes which emails contains offers, extracts codes, and lists
        # additional information regarding the promotional email.
        analyzer.analysis(emails=analyzer.emails)

        # # Asks AI to read the code and return the JSON to actual
        # # readable content report with full-on statistics.
        analyzer.returnText(analyzedEmails=analyzer.analyzedEmails)

    except KeyboardInterrupt:
        print("Interrupted — Please try again.")
    
if __name__ == "__main__":
    main()