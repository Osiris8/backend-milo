import os
from mistralai import Mistral
from dotenv import load_dotenv


load_dotenv()

api_key = os.getenv("MISTRAL_API_KEY")

model = "mistral-large-latest"

client = Mistral(api_key=api_key)

def ask_mistralai(prompt):
    chat_response = client.chat.complete(
    model= model,
    messages = [
        {
            "role": "user",
            "content": prompt,
        },
    ]
)
    return(chat_response.choices[0].message.content)

