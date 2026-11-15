import os 
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

#Initialize GROQ client
client = Groq(
    api_key = os.getenv("GROQ_API_KEY")

)

# Send request to LLM
response = client.chat.completions.create(
    model = "openai/gpt-oss-120b",
    messages=[
        {
            "role": "user",
            "content": "What is Artificial Intelligence?"
        }
    ]
)

# Display response
print(response.choices[0].message.content)