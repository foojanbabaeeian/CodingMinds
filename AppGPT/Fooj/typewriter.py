import json
from openai import OpenAI
import os 

client = OpenAI(
    api_key = os.getenv("GRACE_GPT_API")
)

# 1
system_prompt = """
Be as mean as you can and fight with me as if you are my enemy.
"""

# 2
chat_history = [
    {"role": "system", "content": system_prompt},
]

# 3
while True:
    user_prompt = input("What do you want to ask? ")
    
    # 4
    chat_history.append(
        {"role": "user", "content": user_prompt},
    )
    
    response = client.chat.completions.create(
        model="gpt-4o",
        messages = chat_history
    )

    assistant_response = response.choices[0].message.content
    print(assistant_response)
    print()

    # 5
    chat_history.append(
        {"role": "assistant", "content": assistant_response}
    )