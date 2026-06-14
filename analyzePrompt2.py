prompt2 = '''
You are generating a savings report for a user based on analyzed promotional emails.

Here is the analyzed data:
{analyzed_emails_json}

Write a clear, friendly summary report that:
- States how many emails were scanned and how many had offers
- Lists each offer with: sender, subject, what the deal is, the promo code if one exists, and expiry if known
- Highlights the single best deal at the top
- Ends with a total potential savings estimate
- Uses plain language, no technical jargon
- Do not mention emails with no offer
'''