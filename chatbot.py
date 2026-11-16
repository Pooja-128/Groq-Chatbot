import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(
    api_key = os.getenv("GROQ_API_KEY")
)


messages = [
    {
        "role":"system", 
        "content":"You are a helpful AI assistant."
        }
]

while True:

    user_input = input("You: ")

    if user_input.lower() == "exit":
        break 

    messages.append({
        "role": "user",
        "content": user_input
    })

    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=messages    
    )

    ai_response = response.choices[0].message.content

    print("AI:",ai_response)

    messages.append({
        "role": "assistant",
        "content": ai_response
    })