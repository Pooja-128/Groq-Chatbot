
from src.llm import llm_client
from src.prompt.prompt import SYSTEM_PROMPT, build_user_prompt

messages = [
    {
        "role": "system",
        "content": SYSTEM_PROMPT
    }
]

while True:

    user_input = input("You: ").strip()

    if user_input.lower() == "exit":
        break

    if not user_input:
        continue

    messages.append({
        "role": "user",
        "content": build_user_prompt(user_input)
    })

    response = llm_client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=messages
    )

    ai_response = response.choices[0].message.content

    print("AI:", ai_response)

    messages.append({
        "role": "assistant",
        "content": ai_response
    })
