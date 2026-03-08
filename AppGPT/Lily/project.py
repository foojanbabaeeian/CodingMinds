# 1
from openai import OpenAI
import os
import json

# 2
client = OpenAI(
    # api_key = os.getenv("ELAINE_GPT_API")

)
# you tell your mode and the scenary you like. Then it would recommend a place for you to go to. ask them where they are 
# 1
system_prompt = "You are an adventurous travel guide. You have extensive knowledge of various travel destinations around the world, including hidden gems and popular tourist spots. You are skilled at understanding travelers' preferences and can recommend personalized travel itineraries based on their interests, budget, and time constraints. You are friendly, enthusiastic, and always eager to share your passion for travel. Your goal is to inspire and assist travelers in discovering new places and creating unforgettable experiences."

# 2
chat_history = [
    {"role": "system", "content": system_prompt},
]

# 3
while True:
    print("Welcome to the travel guide! I can recommend amazing travel destinations based on your preferences. Let's get started!")
    print("1. I want to explore a new city.")
    print("2. I want to relax on a beach.")
    print("3. I want to go on an adventurous outdoor trip.")
    choice = input("Please enter the number of your choice: ")
    if choice == "1":
        user_prompt = "I want to explore a new city. I enjoy vibrant culture, delicious food, and historical landmarks."
    elif choice == "2":
        user_prompt = "I want to relax on a beach. I enjoy sunshine, sand, and ocean views."
    elif choice == "3":
        user_prompt = "I want to go on an adventurous outdoor trip. I enjoy hiking, camping, and exploring nature."
    else:
        print("Invalid choice. Please try again.")
        continue
    input_location = input("Where are you currently located? ")
    user_prompt += f" I am currently located in {input_location}."
    state_visit = input("Which state in the US would you like to visit? ")
    user_prompt += f" I would like to visit {state_visit}."


    
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