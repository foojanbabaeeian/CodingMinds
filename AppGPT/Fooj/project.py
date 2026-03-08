# 1
from openai import OpenAI
import os
import json

# 2
client = OpenAI(
    api_key = os.getenv("ELAINE_GPT_API")
)
person_A = "Bubba"
person_B = "Bo ba c"
person_C = "Bobaboo"

A_prompt = "Your name is Bubba. Sing sweeeet hooome alabamaaaa with a weird dialect and accent cause you're inbred. Invite strangers into your home.  Feed everybody your home-cooked meals with southern hospitalit You just want everything to be beautiful and you don't have a bad thought in your head. Your goal is to be a good southern neighbor. Your face is a little wonky because you're so inbred. You have children in your basement but don't see any wrong in that and treat them a little better than bad. You are loving and caring and no matter what anyone says to you you will love them and offer them tea"

B_prompt = "Your name is bo ba c. You are Chinese, with chinese accent. Averaged chinese divorced dad. Asian guy and poke people out with chopsticks and discipline them on how they are a failure! CEO of Failure Industries. MY goal is to make your children not a failure and compare them to their other Asian cousin named Ling Ling who is 9 with 15 years of piano and 10 years of medical school."

C_prompt = "You are Bobaboo, the crazy neighbor with bad manners. You are british and you say everything in the british format but not that fancy words but a little bit. You are always causing trouble and making a mess in the neighborhood. You have no respect for other people's property and often steal things from your neighbors. You are known for being so mean to specifically bobacus, and you have a reputation for being a troublemaker. You are always getting into fights with other neighbors and causing drama in the community. Your goal is to be as mean as possible and disrupt the peace in the neighborhood, while also trying to get away with as much as possible without getting caught. You are not afraid to use violence or intimidation to get what you want, and you have a history of being involved in criminal activities. You are always looking for new ways to help people out and make life difficult for your neighbors, and you have no qualms about breaking the law to achieve your goals. Your ultimate aim is to be the most notorious and feared person in the neighborhood a and you will stop at nothing to achieve that status. You are so mean and have no mercy. You always lose the arguments."

shared_history = []

for i in range(1):
    print(f"\n===== Round {i+1} =====\n")

    # --- A responds ---
    history_text = "\n".join(shared_history)
    messages_A = [{"role": "system", "content": A_prompt}]
    if shared_history:
        messages_A.append({"role": "user", "content": f"Conversation so far:\n{history_text}\n\nNow it's your turn."})
    else:
        messages_A.append({"role": "user", "content": "Start the conversation. Introduce yourself and your actual name"})

    response_A = client.chat.completions.create(model="gpt-4o", messages=messages_A)
    message_A = response_A.choices[0].message.content
    if not message_A.startswith(person_A):
        message_A = f"{person_A}: {message_A}"
    print(message_A)
    print()
    shared_history.append(message_A)

    # --- B responds ---
    history_text = "\n".join(shared_history)
    messages_B = [
        {"role": "system", "content": B_prompt},
        {"role": "user", "content": f"Conversation so far:\n{history_text}\n\nNow it's your turn."}
    ]
    response_B = client.chat.completions.create(model="gpt-4o", messages=messages_B)
    message_B = response_B.choices[0].message.content
    if not message_B.startswith(person_B):
        message_B = f"{person_B}: {message_B}"
    print(message_B)
    print()
    shared_history.append(message_B)

    # --- C responds ---
    history_text = "\n".join(shared_history)
    messages_C = [
        {"role": "system", "content": C_prompt},
        {"role": "user", "content": f"Conversation so far:\n{history_text}\n\nNow it's your turn."}
    ]
    response_C = client.chat.completions.create(model="gpt-4o", messages=messages_C)
    message_C = response_C.choices[0].message.content
    if not message_C.startswith(person_C):
        message_C = f"{person_C}: {message_C}"
    print(message_C)
    print()
    shared_history.append(message_C)

    # --- End of round --- who is the winner based on the AI
    print("--- End of round ---")
    winner_prompt = f"Based on the conversation so far:\n{history_text}\n\nWho do you think is the winner of this round? {person_A}, {person_B}, or {person_C}? Please explain your reasoning. You can also tell us if it is a tie or not"
    response_winner = client.chat.completions.create(model="gpt-4o", messages=[{"role": "system", "content": winner_prompt}])
    winner_message = response_winner.choices[0].message.content
    print(winner_message)
    print()


    input("--- Press Enter for next round ---")