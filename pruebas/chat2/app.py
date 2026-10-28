from ollama import chat

stream = chat(
  model='llama3.2:3b',
  messages=[{'role': 'user', 'content': 'cuantas casillas tiene un teclado de ajedrez, si pongo un grarno de arroz en una casilla y en el siguiente el doble, llendome asi con cuanto arroz terminaria?'}],
  stream=True,
)

in_thinking = False
content = ''
thinking = ''
for chunk in stream:
  if chunk.message.thinking:
    if not in_thinking:
      in_thinking = True
      print('Thinking:\n', end='', flush=True)
    print(chunk.message.thinking, end='', flush=True)
    # accumulate the partial thinking 
    thinking += chunk.message.thinking
  elif chunk.message.content:
    if in_thinking:
      in_thinking = False
      print('\n\nAnswer:\n', end='', flush=True)
    print(chunk.message.content, end='', flush=True)
    # accumulate the partial content
    content += chunk.message.content

  # append the accumulated fields to the messages for the next request
  new_messages = [{ role: 'user', thinking: thinking, content: content }]