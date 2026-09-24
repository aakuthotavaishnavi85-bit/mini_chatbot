from ollama import chat 
bad="tell me about dogs?"
good=" list 5 types of dog breeds and explain about it briefly? "
response=chat(
    model="llama3.2",
    messages=[
        {
            "role":"user",
            "content":bad
        },
        {
            "role":"user",
            "content":good
        }

    ]
    )
print(response.message.content)