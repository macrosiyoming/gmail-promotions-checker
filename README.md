# gmail-promotions-checker
a python script capable of checking discounts, sales, and promo codes automatically so you don't miss out any deal!

tags: python, gmail, gemini, oauth, api

==================

HOW TO USE:
- please install all the dependencies in the requirements.txt
- please upload token.json (from OAuth of GMail API) and api.py (Gemini API)
- go to main.py, run the code
- it will prompt you to sign in with your Google Account, select the desired email
- it will give you a comprehensible report regarding missed promotional details

==================

HOW IT WORKS:
- the project has 4 main python files: main, auth, fetch, and analyzer
- main focuses on running the 3 files
- auth focuses on the GMail OAuth access
- fetch focuses on getting the emails into local files
- analyzer focuses on Gemini API on analyzing email data for potential missed promotion sales

==================

TIMELINE:
- DONE - fetch encoded email data from gmail api and store data
- DONE - use ai api to analyze email data
- DONE - return potential savings
- DONE - add error testcases
- SOON - saas startup launch