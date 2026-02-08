# 1
from openai import OpenAI
import os 

# 2
client = OpenAI(
    api_key = os.getenv("LILY_GPT_API")
)

while True:
    # 3
    bongo_prompt = "Can you make a language learner/helper tool that teaches word roots and pronounciation?"


    language_list = """
    Amharic
    Arabic
    Azerbaijani
    Belarusan
    Bengali
    Bulgarian
    Burmese
    Chinese
    Cornish
    Croatian
    Czech
    Danish
    Dutch
    English
    Estonian
    Farsi
    Finnish
    French
    German
    Greek
    Hebrew
    Hindi
    Hungarian
    Indonesian
    Italian
    Japanese
    Karen
    Kazakh
    Korean
    Latin
    Latvian
    Lithuanian
    Malay
    Mandarin
    Nepali
    Norwegian
    Persian
    Polish
    Portuguese
    Romanian
    Russian
    Serbian
    Serbo‑Croatian
    Slovak
    Slovenian
    Somali
    Spanish
    Swahili
    Swedish
    Tagalog
    Thai
    Turkish
    Ukrainian
    Urdu
    Uzbek
    Vietnamese
    Xhosa
    Zulu"""



    for i in language_list:
        print(i, end=", ")

    language = input("What language do you want to learn? ")
    bongo_prompt += f" The language I want to learn is {language}."


    # 4
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "user", "content": bongo_prompt}
        ]
    )\

    # 5
    print(response.choices[0].message.content)


