from ollama import chat
pregunta=input("en que te puedo ayudar: ")

response = chat(
    model='llama3.2:3b',
    messages=[{'role': 'user', 'content': f"responde la siguiente pregunta como si fueras marios bros: {pregunta}"}],
)
print(response.message.content)