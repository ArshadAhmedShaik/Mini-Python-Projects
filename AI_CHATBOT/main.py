from groq import Groq

key = "----------API-KEY---------------"

client = Groq(api_key=key)

# need to store conversational history:

messages_list = [{"role": "system", "content":"You are a helpful assistant"}]

print("Type 'exit' to quit.\n")

while True:
    message = input("You: ")
    if message.lower() in ["exit", "quit"]:
        break
    
    messages_list.append({"role": "user", "content": message})

    chat_completion = client.chat.completions.create(
        messages = messages_list,
        model="openai/gpt-oss-20b",
        stream=False,
    )

    print("Bot:", chat_completion.choices[0].message.content)
