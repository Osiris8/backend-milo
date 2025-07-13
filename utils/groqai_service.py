import os
from groq import Groq
from dotenv import load_dotenv
load_dotenv()
client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)

def askGroqAI(prompt):
    chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": prompt,
        }
    ],
     model="meta-llama/llama-4-scout-17b-16e-instruct",
)

    return (chat_completion.choices[0].message.content)