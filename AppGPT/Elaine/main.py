# 1
from openai import OpenAI
import os

# 2
client = OpenAI(
    api_key = os.getenv("ELAINE_GPT_API")
)

# 3
user_prompt = "Can you make a story with the context of 'Penguin surfing on Seal', make it really fun and use narattive and be creative. "

# 4
response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "user", "content": user_prompt}
    ]
)

# 5
print(response.choices[0].message.content)