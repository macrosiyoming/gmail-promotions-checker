prompt = """
You are analyzing a batch of promotional emails. For each email, extract discount and offer information.

Here are the emails:

{for each email, something like:}
---
Email ID: {id}
Subject: {subject}
Sender: {sender}
Body: {body}
---

Return ONLY a JSON array, one object per email, in the same order as given, with this structure:

{
  "id": "the email id, copied exactly as given",
  "subject": "copied exactly as given",
  "sender": "copied exactly as given",
  "has_offer": true or false,
  "offer_type": "promo_code" or "conditional_discount" or "none",
  "code": "the actual code if one exists, otherwise null",
  "discount_description": "plain description, e.g. '20% off first order'",
  "estimated_value": "rough dollar estimate if calculable, otherwise null",
  "expiry": "expiry date/condition if mentioned, otherwise null"
}

Return one object per email, even if has_offer is false. Do not skip any emails. Do not include any text outside the JSON array.
"""