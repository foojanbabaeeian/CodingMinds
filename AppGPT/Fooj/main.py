# 1
from openai import OpenAI
import os 

# funny customer review maker 
# 2
client = OpenAI(
    api_key = os.getenv("LILY_GPT_API")
)
while True:
# 3
    product = input("What product do you want to make funny reviews for? ")

    user_prompt = f"Make the most useless funny customer reviews for a specific product.  I want you to be as funny as possible and give ratings that are either 1 or 5 stars.  The product is a {product}.  I want you to be really creative and make the reviews as funny as possible.  Make sure to include the rating for each review.  Make sure to include the name of the reviewer for each review.  Make sure to include the date of the review for each review.  Make sure to include the title of the review for each review.  Make sure to include the content of the review for each review.  Make sure to include the pros and cons of the product for each review. "

    # 4
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "user", "content": user_prompt}
        ]
    )

    # 5
    print(response.choices[0].message.content)