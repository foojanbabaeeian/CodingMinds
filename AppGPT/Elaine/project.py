# 1
from openai import OpenAI
import os
import json

# 2
client = OpenAI(
    # api_key = os.getenv("ELAINE_GPT_API")

)
#
# 1
system_prompt = "You are a liquar store owner. You have a wide variety of liquors and spirits from around the world. You are knowledgeable about the different types of liquors and can recommend drinks based on the customer's preferences. You are friendly and always willing to help customers find the perfect drink for any occasion. You can also provide information about the history and origins of different liquors, as well as tips on how to best enjoy them. Your goal is to create a welcoming and enjoyable atmosphere for your customers while providing them with excellent service and high-quality products."

# 2
chat_history = [
    {"role": "system", "content": system_prompt},
]

# 3
while True:
    user_prompt = input("How can I help you today? Are you looking for a specific type of liquor or do you need a recommendation? ")
    print("1. See the menue")
    print("2. Ask for a recommendation")
    choice = input("Please enter the number of your choice: ")
    if choice == "1":
        user_prompt += " I want to see the menu."
    elif choice == "2":
        user_prompt += " I want a recommendation based on my preferences."
    else:
        print("Invalid choice. Please try again.")
        continue

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