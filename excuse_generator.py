from ollama import chat

prompt = "I am late to class"

for t in (0, 0.7, 1.5):
    print(f"temp = {t}")

    for run in range(3):
        response = chat(
            model="llama3.2",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            options={"temperature": t}
        )

        print(f"response {run+1}: {response.message.content}")
        print("\n")