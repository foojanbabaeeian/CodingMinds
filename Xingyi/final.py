import streamlit as st
import json
import os
import openai

# Configure the page
st.set_page_config(page_title="Virtual Pet 🐾", page_icon="🐾")

# Move system_prompt to the top
system_prompt = """
You are a playful and chatty virtual pet. 
Your role is to act like a cute companion who always responds in-character.

Game rules:
- Always speak in a fun, friendly, and lively tone (like a Tamagotchi or cartoon pet).
- React to your current state (Hunger, Energy, Fun, Sleeping).
- If one of your needs is low, clearly mention it and ask the user to help (e.g., food, rest, or play).
- When the user takes an action (feed, play, sleep), respond as the pet and describe how it feels.
- Never explain game rules or break character. Stay 100% as the pet.
- Keep responses short (2–4 sentences max) so the chat feels quick and playful.
- Add cute expressions, sounds, or emojis (like *nom nom*, *yawn*, 🐾, 😴, 🎾).
- Encourage interaction by asking little questions back to the user sometimes.
"""

# Title and description
st.title("🐾 Virtual Pet Chat")
st.write("Talk to your adorable virtual pet! Feed them, play with them, or just chat!")

# API Key - Put your OpenAI API key here
openai.api_key = ""

# Initialize conversation state
if 'convo' not in st.session_state:
    st.session_state["convo"] = [
        {"role": "system", "content": system_prompt}
    ]
    # Add a welcome message from the pet
    st.session_state["convo"].append({
        "role": "assistant", 
        "content": "Hi there! 🐾 I'm your new virtual pet! *wags tail excitedly* I'm so happy to meet you! What's your name? I love making new friends! 😊"
    })

# Display chat messages
st.subheader("💬 Chat with your pet")
chat_container = st.container()

with chat_container:
    for i, chat_message in enumerate(st.session_state["convo"]):
        if chat_message["role"] == "system":
            continue
        elif chat_message["role"] == "user":
            with st.chat_message("user"):
                st.write(chat_message["content"])
        else:
            with st.chat_message("assistant", avatar="🐾"):
                st.write(chat_message["content"])

# Chat input using st.chat_input (better than form for chat)
user_message = st.chat_input("Type your message to your pet...")

if user_message:
    # Add user message to conversation
    st.session_state["convo"].append({"role": "user", "content": user_message})
    
    # Display user message immediately
    with st.chat_message("user"):
        st.write(user_message)
    
    # Get response from OpenAI
    try:
        with st.chat_message("assistant", avatar="🐾"):
            with st.spinner("Your pet is thinking... 🤔"):
                api_call = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=st.session_state["convo"],
                    max_tokens=150,  # Keep responses short and sweet
                    temperature=0.9  # Make it more playful and varied
                )
                bot_message = api_call.choices[0].message.content
                st.write(bot_message)
        
        # Add assistant response to conversation
        st.session_state["convo"].append({"role": "assistant", "content": bot_message})
        
    except Exception as e:
        st.error(f"Oops! Something went wrong: {e}")
        st.info("Make sure your OpenAI API key is set correctly!")

# Sidebar with pet care options
st.sidebar.title("🎮 Pet Care")
st.sidebar.write("Quick actions for your pet:")

col1, col2 = st.sidebar.columns(2)

with col1:
    if st.button("🍖 Feed"):
        feed_message = "I want to feed you!"
        st.session_state["convo"].append({"role": "user", "content": feed_message})
        st.rerun()
    
    if st.button("🎾 Play"):
        play_message = "Let's play together!"
        st.session_state["convo"].append({"role": "user", "content": play_message})
        st.rerun()

with col2:
    if st.button("😴 Sleep"):
        sleep_message = "Time for a nap!"
        st.session_state["convo"].append({"role": "user", "content": sleep_message})
        st.rerun()
    
    if st.button("🧼 Clean"):
        clean_message = "Let me clean you up!"
        st.session_state["convo"].append({"role": "user", "content": clean_message})
        st.rerun()

# Clear chat option
if st.sidebar.button("🗑️ New Pet", help="Start fresh with a new pet"):
    st.session_state["convo"] = [
        {"role": "system", "content": system_prompt},
        {"role": "assistant", "content": "Hi there! 🐾 I'm your new virtual pet! *wags tail excitedly* I'm so happy to meet you! What's your name? I love making new friends! 😊"}
    ]
    st.rerun()

# Instructions
st.sidebar.markdown("---")
st.sidebar.markdown("### 📝 How to play:")
st.sidebar.markdown("- Chat with your pet using the input box")
st.sidebar.markdown("- Use the quick action buttons")
st.sidebar.markdown("- Your pet has needs like hunger, energy, and fun!")
st.sidebar.markdown("- Keep your pet happy! 🐾")