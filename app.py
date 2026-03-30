import os
from groq import Groq

client = Groq( api_key= os.getenv("GROQ_API_KEY"))

messages = [
    {"role": "system", "content": "You are a helpful AI assistant"}
]

while True:
    user_input = input("You:")

    if user_input.lower() in ["exit", "quit"]:
        print("Goodbye!")
        break
    
    messages.append({"role": "user", "content": user_input})

    response  = client.chat.completions.create(
        model = "llama-3.3-70b-versatile",
        messages = messages
    )

    ai_reply = response.choices[0].message.content
    messages.append({"role": "assistant", "content": ai_reply})
    print("AI:", ai_reply)
