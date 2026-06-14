import os
import json
from markdown import markdown

from analyzePrompt import prompt
from analyzePrompt2 import prompt2
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
        model="gemini-3.5-flash",
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

    print("Created analyzedEmails.json!")

with open('gitignore/analyzedEmails.json') as user_file:
    analyzedEmails = user_file.read()

def returnText(analyzedEmails):
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=(prompt2 + analyzedEmails),
    )

    base_dir = os.path.dirname(os.path.abspath(__file__))
    json_path = os.path.join(base_dir, "gitignore", "report.md")

    # export report to external md
    with open(json_path, 'w') as fp:
        fp.write(response.text)
    
    print("Created report.md!")
