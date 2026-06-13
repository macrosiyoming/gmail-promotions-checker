import os
import json

from analyzePrompt import prompt
from google import genai
from gitignore.api import GEMINI_API

# calling client
client = genai.Client(api_key=GEMINI_API)

# calling email list
with open('gitignore/emails.json') as user_file:
    emails = user_file.read()

# analysis function
def analysis(emails):
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=(prompt + emails),
    )
    analyzedEmails = response.text
    analyzedEmails = analyzedEmails.removeprefix("```json")
    analyzedEmails = analyzedEmails.removesuffix("```")
    analyzedEmails = json.loads(analyzedEmails)

    base_dir = os.path.dirname(os.path.abspath(__file__))
    json_path = os.path.join(base_dir, "gitignore", "analyzedEmails.json")

    # export analyzed emails into dictionary lists in new json file
    with open(json_path, 'w') as fp:
        json.dump(analyzedEmails, fp, indent=4)

with open('gitignore/analyzedEmails.json') as user_file:
    analyzedEmails = user_file.read()

# ONGOING - turn json dictionaries to readable human report
# def returnText(emails):
#     totalSavings = 

#     for i in emails:
#         if i["has_offer"] == True:
