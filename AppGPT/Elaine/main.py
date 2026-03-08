# 1
from openai import OpenAI
import os
import json

# 2
client = OpenAI(
    # api_key = os.getenv("ELAINE_GPT_API")
)

# 1
system_prompt = "You are a creative storyteller. Make it really fun and use narrative. Keep it short and sweet, but make it really engaging. Use descriptive language and vivid imagery to bring the story to life. Make sure to include a clear beginning, middle, and end. The story should be suitable for all ages and should leave the reader with a sense of wonder and excitement. I want the story to be really short and build on itself every time"

# 2
chat_history = [
    {"role": "system", "content": system_prompt},
]

# 3
while True:
    user_prompt = input("What kind of story would you like to hear? ")
    
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