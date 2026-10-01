from ollama import chat

response = chat(
    model="llama3.2",
    messages=[
        {
            "role": "user",
            "content": "what is sql, in one line "
        }
    ]
)

print(response)